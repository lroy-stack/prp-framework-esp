# Patrones de Desarrollo de Servidor MCP

Este documento contiene patrones probados para desarrollar servidores Model Context Protocol (MCP) usando TypeScript y Cloudflare Workers, basados en la implementación en esta base de código.

## Arquitectura Principal de Servidor MCP

### Patrón de Clase Servidor Base

```typescript
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

// Props de autenticación del flujo OAuth
type Props = {
  login: string;
  name: string;
  email: string;
  accessToken: string;
};

export class CustomMCP extends McpAgent<Env, Record<string, never>, Props> {
  server = new McpServer({
    name: "Nombre de Tu Servidor MCP",
    version: "1.0.0",
  });

  // CRÍTICO: Implementar limpieza para Durable Objects
  async cleanup(): Promise<void> {
    try {
      // Cerrar conexiones de base de datos
      await closeDb();
      console.log('Conexiones de base de datos cerradas exitosamente');
    } catch (error) {
      console.error('Error durante limpieza de base de datos:', error);
    }
  }

  // CRÍTICO: Manejador de alarma Durable Objects
  async alarm(): Promise<void> {
    await this.cleanup();
  }

  // Inicializar todas las herramientas y recursos
  async init() {
    // Registrar herramientas aquí
    this.registerTools();
    
    // Registrar recursos si es necesario
    this.registerResources();
  }

  private registerTools() {
    // Lógica registro de herramientas
  }

  private registerResources() {
    // Lógica registro de recursos
  }
}
```

### Patrón de Registro de Herramientas

```typescript
// Registro básico de herramienta
this.server.tool(
  "nombreHerramienta",
  "Descripción de la herramienta para el LLM",
  {
    param1: z.string().describe("Descripción del parámetro"),
    param2: z.number().optional().describe("Parámetro opcional"),
  },
  async ({ param1, param2 }) => {
    try {
      // Implementación de la herramienta
      const result = await performOperation(param1, param2);
      
      return {
        content: [
          {
            type: "text",
            text: `Éxito: ${JSON.stringify(result, null, 2)}`
          }
        ]
      };
    } catch (error) {
      console.error('Error de herramienta:', error);
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`,
            isError: true
          }
        ]
      };
    }
  }
);
```

### Registro de Herramientas Condicional (Basado en Permisos)

```typescript
// Disponibilidad de herramientas basada en permisos
const ALLOWED_USERNAMES = new Set<string>([
  'admin1',
  'admin2'
]);

// Registrar herramientas privilegiadas solo para usuarios autorizados
if (ALLOWED_USERNAMES.has(this.props.login)) {
  this.server.tool(
    "herramientaPrivilegiada",
    "Herramienta solo disponible para usuarios autorizados",
    { /* parámetros */ },
    async (params) => {
      // Operación privilegiada
      return {
        content: [
          {
            type: "text",
            text: `Operación privilegiada ejecutada por: ${this.props.login}`
          }
        ]
      };
    }
  );
}
```

## Patrones de Integración de Base de Datos

### Patrón de Conexión a Base de Datos

```typescript
import { withDatabase, validateSqlQuery, isWriteOperation, formatDatabaseError } from "./database";

// Operación de base de datos con gestión de conexión
async function performDatabaseOperation(sql: string) {
  try {
    // Validar consulta SQL
    const validation = validateSqlQuery(sql);
    if (!validation.isValid) {
      return {
        content: [
          {
            type: "text",
            text: `Consulta SQL inválida: ${validation.error}`,
            isError: true
          }
        ]
      };
    }

    // Ejecutar con gestión automática de conexión
    return await withDatabase(this.env.DATABASE_URL, async (db) => {
      const results = await db.unsafe(sql);
      
      return {
        content: [
          {
            type: "text",
            text: `**Resultados de Consulta**\n\`\`\`sql\n${sql}\n\`\`\`\n\n**Resultados:**\n\`\`\`json\n${JSON.stringify(results, null, 2)}\n\`\`\`\n\n**Filas retornadas:** ${Array.isArray(results) ? results.length : 1}`
          }
        ]
      };
    });
  } catch (error) {
    console.error('Error operación base de datos:', error);
    return {
      content: [
        {
          type: "text",
          text: `Error base de datos: ${formatDatabaseError(error)}`,
          isError: true
        }
      ]
    };
  }
}
```

### Manejo de Operaciones de Lectura vs Escritura

```typescript
// Verificar si operación es solo lectura
if (isWriteOperation(sql)) {
  return {
    content: [
      {
        type: "text",
        text: "Operaciones de escritura no están permitidas con esta herramienta. Usa la herramienta privilegiada si tienes permisos de escritura.",
        isError: true
      }
    ]
  };
}
```

## Patrones de Autenticación y Autorización

### Patrón de Integración OAuth

```typescript
import OAuthProvider from "@cloudflare/workers-oauth-provider";
import { GitHubHandler } from "./github-handler";

// Configuración OAuth
export default new OAuthProvider({
  apiHandlers: {
    '/sse': MyMCP.serveSSE('/sse') as any,
    '/mcp': MyMCP.serve('/mcp') as any,
  },
  authorizeEndpoint: "/authorize",
  clientRegistrationEndpoint: "/register",
  defaultHandler: GitHubHandler as any,
  tokenEndpoint: "/token",
});
```

### Verificación de Permisos de Usuario

```typescript
// Patrón de validación de permisos
function hasPermission(username: string, operation: string): boolean {
  const WRITE_PERMISSIONS = new Set(['admin1', 'admin2']);
  const READ_PERMISSIONS = new Set(['user1', 'user2', ...WRITE_PERMISSIONS]);
  
  switch (operation) {
    case 'read':
      return READ_PERMISSIONS.has(username);
    case 'write':
      return WRITE_PERMISSIONS.has(username);
    default:
      return false;
  }
}
```

## Patrones de Manejo de Errores

### Respuesta de Error Estandarizada

```typescript
// Patrón de respuesta de error
function createErrorResponse(error: Error, operation: string) {
  console.error(`Error ${operation}:`, error);
  
  return {
    content: [
      {
        type: "text",
        text: `${operation} falló: ${error.message}`,
        isError: true
      }
    ]
  };
}
```

### Formateo de Errores de Base de Datos

```typescript
// Usar el formateador de errores de base de datos integrado
import { formatDatabaseError } from "./database";

try {
  // Operación de base de datos
} catch (error) {
  return {
    content: [
      {
        type: "text",
        text: `Error base de datos: ${formatDatabaseError(error)}`,
        isError: true
      }
    ]
  };
}
```

## Patrones de Registro de Recursos

### Patrón de Recurso Básico

```typescript
// Registro de recurso
this.server.resource(
  "resource://example/{id}",
  "Descripción del recurso",
  async (uri) => {
    const id = uri.path.split('/').pop();
    
    try {
      const data = await fetchResourceData(id);
      
      return {
        contents: [
          {
            uri: uri.href,
            mimeType: "application/json",
            text: JSON.stringify(data, null, 2)
          }
        ]
      };
    } catch (error) {
      throw new Error(`Falló obtener recurso: ${error.message}`);
    }
  }
);
```

## Patrones de Testing

### Patrón de Testing de Herramientas

```typescript
// Probar funcionalidad de herramienta
async function testTool(toolName: string, params: any) {
  try {
    const result = await server.callTool(toolName, params);
    console.log(`Prueba ${toolName} pasada:`, result);
    return true;
  } catch (error) {
    console.error(`Prueba ${toolName} falló:`, error);
    return false;
  }
}
```

### Testing de Conexión de Base de Datos

```typescript
// Probar conectividad de base de datos
async function testDatabaseConnection() {
  try {
    await withDatabase(process.env.DATABASE_URL, async (db) => {
      const result = await db`SELECT 1 as test`;
      console.log('Prueba conexión base de datos pasada:', result);
    });
    return true;
  } catch (error) {
    console.error('Prueba conexión base de datos falló:', error);
    return false;
  }
}
```

## Mejores Prácticas de Seguridad

### Validación de Input

```typescript
// Siempre validar inputs con Zod
const inputSchema = z.object({
  query: z.string().min(1).max(1000),
  parameters: z.array(z.string()).optional()
});

// En manejador de herramienta
try {
  const validated = inputSchema.parse(params);
  // Usar datos validados
} catch (error) {
  return createErrorResponse(error, "Validación de input");
}
```

### Prevención de Inyección SQL

```typescript
// Usar la validación SQL integrada
import { validateSqlQuery } from "./database";

const validation = validateSqlQuery(sql);
if (!validation.isValid) {
  return createErrorResponse(new Error(validation.error), "Validación SQL");
}
```

### Control de Acceso

```typescript
// Siempre verificar permisos antes de ejecutar operaciones sensibles
if (!hasPermission(this.props.login, 'write')) {
  return {
    content: [
      {
        type: "text",
        text: "Acceso denegado: permisos insuficientes",
        isError: true
      }
    ]
  };
}
```

## Patrones de Rendimiento

### Pool de Conexiones

```typescript
// Usar el pool de conexiones integrado
import { withDatabase } from "./database";

// La función withDatabase maneja el pool de conexiones automáticamente
await withDatabase(databaseUrl, async (db) => {
  // Operaciones de base de datos
});
```

### Limpieza de Recursos

```typescript
// Implementar limpieza apropiada en Durable Objects
async cleanup(): Promise<void> {
  try {
    // Cerrar conexiones de base de datos
    await closeDb();
    
    // Limpiar otros recursos
    await cleanupResources();
    
    console.log('Limpieza completada exitosamente');
  } catch (error) {
    console.error('Error de limpieza:', error);
  }
}
```

## Errores Comunes

### 1. Implementación de Limpieza Faltante
- Siempre implementar método `cleanup()` en Durable Objects
- Manejar limpieza de conexión de base de datos apropiadamente
- Configurar manejador de alarma para limpieza automática

### 2. Vulnerabilidades de Inyección SQL
- Siempre usar `validateSqlQuery()` antes de ejecutar SQL
- Nunca concatenar input de usuario directamente en strings SQL
- Usar consultas parametrizadas cuando sea posible

### 3. Bypasses de Permisos
- Verificar permisos para cada operación sensible
- No depender solo del registro de herramientas para seguridad
- Siempre validar identidad de usuario desde props

### 4. Fuga de Información de Errores
- Usar `formatDatabaseError()` para sanitizar mensajes de error
- No exponer detalles del sistema interno en respuestas de error
- Registrar errores detallados del lado servidor, retornar mensajes genéricos al cliente

### 5. Fugas de Recursos
- Siempre usar `withDatabase()` para operaciones de base de datos
- Implementar manejo apropiado de errores en operaciones async
- Limpiar recursos en bloques finally

## Configuración de Entorno

### Variables de Entorno Requeridas

```typescript
// Definición de tipo de entorno
interface Env {
  DATABASE_URL: string;
  GITHUB_CLIENT_ID: string;
  GITHUB_CLIENT_SECRET: string;
  OAUTH_KV: KVNamespace;
  // Agregar otros bindings según sea necesario
}
```

### Patrón de Configuración Wrangler

```toml
# wrangler.toml
name = "mcp-server"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[[kv_namespaces]]
binding = "OAUTH_KV"
id = "tu-id-namespace-kv"

[env.production]
# Configuración específica de producción
```

Este documento proporciona los patrones principales para construir servidores MCP seguros y escalables usando la arquitectura probada en esta base de código.