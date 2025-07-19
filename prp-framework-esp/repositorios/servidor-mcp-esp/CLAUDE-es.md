# Servidor MCP con OAuth de GitHub - Guía de Implementación

Esta guía proporciona patrones de implementación y estándares para construir servidores MCP (Model Context Protocol) con autenticación OAuth de GitHub usando Node.js, TypeScript y Cloudflare Workers. Para QUÉ construir, consulta los documentos PRP (Product Requirement Prompt).

## Principios Fundamentales

**IMPORTANTE: DEBES seguir estos principios en todos los cambios de código y generaciones de PRP:**

### KISS (Keep It Simple, Stupid)

- La simplicidad debe ser un objetivo clave en el diseño
- Elige soluciones directas sobre complejas siempre que sea posible
- Las soluciones simples son más fáciles de entender, mantener y depurar

### YAGNI (You Aren't Gonna Need It)

- Evita construir funcionalidad por especulación
- Implementa características solo cuando son necesarias, no cuando anticipas que podrían ser útiles en el futuro

### Principio Abierto/Cerrado

- Las entidades de software deben estar abiertas para extensión pero cerradas para modificación
- Diseña sistemas para que nueva funcionalidad pueda agregarse con cambios mínimos al código existente

## Gestión de Paquetes y Herramientas

**CRÍTICO: Este proyecto usa npm para gestión de paquetes Node.js y Wrangler CLI para desarrollo en Cloudflare Workers.**

### Comandos npm Esenciales

```bash
# Instalar dependencias desde package.json
npm install

# Agregar una dependencia
npm install package-name

# Agregar dependencia de desarrollo
npm install --save-dev package-name

# Remover un paquete
npm uninstall package-name

# Actualizar dependencias
npm update

# Ejecutar scripts definidos en package.json
npm run dev
npm run deploy
npm run type-check
```

### Comandos Wrangler CLI Esenciales

**CRÍTICO: Usa Wrangler CLI para todo el desarrollo, testing y despliegue en Cloudflare Workers.**

```bash
# Autenticación
wrangler login          # Iniciar sesión en cuenta Cloudflare
wrangler logout         # Cerrar sesión de Cloudflare
wrangler whoami         # Verificar usuario actual

# Desarrollo y Testing
wrangler dev           # Iniciar servidor de desarrollo local (puerto 8787 por defecto)

# Despliegue
wrangler deploy        # Desplegar Worker a Cloudflare
wrangler deploy --dry-run  # Probar despliegue sin realmente desplegar

# Configuración y Tipos
wrangler types         # Generar tipos TypeScript desde configuración Worker
```

## Arquitectura del Proyecto

**IMPORTANTE: Este es un servidor MCP de Cloudflare Workers con autenticación OAuth de GitHub para acceso seguro a base de datos.**

### Estructura Actual del Proyecto

```
/
├── src/                          # Código fuente TypeScript
│   ├── index.ts                  # Servidor MCP principal (estándar)
│   ├── index_sentry.ts          # Servidor MCP con Sentry habilitado
│   ├── simple-math.ts           # Ejemplo MCP básico (sin auth)
│   ├── github-handler.ts        # Implementación flujo OAuth GitHub
│   ├── database.ts              # Conexión PostgreSQL y utilidades
│   ├── utils.ts                 # Funciones auxiliares OAuth
│   ├── workers-oauth-utils.ts   # Sistema aprobación basado en cookies
│   └── tools/                   # Sistema registro de herramientas
│       └── register-tools.ts    # Registro centralizado de herramientas
├── PRPs/                        # Product Requirement Prompts
│   ├── README.md
│   └── templates/
│       └── prp_mcp_base.md
├── examples/                    # Creación ejemplo de herramientas + registro - NUNCA editar o importar desde esta carpeta
│   ├── database-tools.ts        # Herramientas ejemplo para servidor Postgres MCP mostrando mejores prácticas para creación y registro de herramientas
│   └── database-tools-sentry.ts # Herramientas ejemplo para servidor Postgres MCP pero con integración Sentry para monitoreo de producción
├── wrangler.jsonc              # Configuración principal Cloudflare Workers
├── wrangler-simple.jsonc       # Configuración ejemplo matemática simple
├── package.json                # Dependencias npm y scripts
├── tsconfig.json               # Configuración TypeScript
├── worker-configuration.d.ts   # Tipos Cloudflare generados
└── CLAUDE.md                   # Esta guía de implementación
```

### Propósitos de Archivos Clave (SIEMPRE AGREGAR NUEVOS ARCHIVOS AQUÍ)

**Archivos de Implementación Principal:**

- `src/index.ts` - Servidor MCP de producción con OAuth GitHub + PostgreSQL
- `src/index_sentry.ts` - Igual que el anterior con integración de monitoreo Sentry

**Autenticación y Seguridad:**

- `src/github-handler.ts` - Flujo completo OAuth 2.0 de GitHub
- `src/workers-oauth-utils.ts` - Sistema de aprobación con cookies firmadas HMAC
- `src/utils.ts` - Auxiliares para intercambio de tokens OAuth y construcción de URLs

**Integración de Base de Datos:**

- `src/database.ts` - Pool de conexiones PostgreSQL, validación SQL, seguridad

**Registro de Herramientas:**

- `src/tools/register-tools.ts` - Sistema de registro centralizado que importa y registra todas las herramientas

**Archivos de Configuración:**

- `wrangler.jsonc` - Configuración Worker principal con Durable Objects, KV, bindings AI
- `wrangler-simple.jsonc` - Configuración ejemplo simple
- `tsconfig.json` - Configuración compilador TypeScript para Cloudflare Workers

## Comandos de Desarrollo

### Comandos de Flujo de Trabajo Principal

```bash
# Configuración y Dependencias
npm install                  # Instalar todas las dependencias
npm install --save-dev @types/package  # Agregar dependencia dev con tipos

# Desarrollo
wrangler dev                # Iniciar servidor desarrollo local
npm run dev                 # Alternativa vía script npm

# Verificación de Tipos y Validación
npm run type-check          # Ejecutar verificación compilador TypeScript
wrangler types              # Generar tipos Cloudflare Worker
npx tsc --noEmit           # Verificar tipos sin compilar

# Testing
npx vitest                  # Ejecutar tests unitarios (si configurado)

# Calidad de Código
npx prettier --write .      # Formatear código
npx eslint src/            # Linter código TypeScript
```

### Configuración de Entorno

**Configuración Variables de Entorno:**

```bash
# Crear archivo .dev.vars para desarrollo local basado en .dev.vars.example
cp .dev.vars.example .dev.vars

# Secretos de producción (vía Wrangler)
wrangler secret put GITHUB_CLIENT_ID
wrangler secret put GITHUB_CLIENT_SECRET
wrangler secret put COOKIE_ENCRYPTION_KEY
wrangler secret put DATABASE_URL
wrangler secret put SENTRY_DSN
```

## Contexto de Desarrollo MCP

**IMPORTANTE: Este proyecto construye servidores MCP listos para producción usando Node.js/TypeScript en Cloudflare Workers con autenticación OAuth de GitHub.**

### Stack Tecnológico MCP

**Tecnologías Principales:**

- **@modelcontextprotocol/sdk** - SDK oficial MCP TypeScript
- **agents/mcp** - Framework agente MCP para Cloudflare Workers
- **workers-mcp** - Capa de transporte MCP para Workers
- **@cloudflare/workers-oauth-provider** - Implementación servidor OAuth 2.1

**Plataforma Cloudflare:**

- **Cloudflare Workers** - Runtime serverless (aislados V8)
- **Durable Objects** - Objetos con estado para persistencia agente MCP
- **KV Storage** - Gestión estado OAuth y sesiones

### Arquitectura Servidor MCP

Este proyecto implementa servidores MCP como Cloudflare Workers con tres patrones principales:

**1. Servidor MCP de Base de Datos Autenticado (`src/index.ts`):**

```typescript
export class MyMCP extends McpAgent<Env, Record<string, never>, Props> {
  server = new McpServer({
    name: "PostgreSQL Database MCP Server",
    version: "1.0.0",
  });

  // Herramientas MCP disponibles basadas en permisos de usuario
  // - listTables (todos los usuarios)
  // - queryDatabase (todos los usuarios, solo lectura)
  // - executeDatabase (solo usuarios privilegiados)
}
```

**2. Servidor MCP Monitoreado (`src/index_sentry.ts`):**

- Misma funcionalidad que el anterior con instrumentación Sentry
- Trazado distribuido para llamadas de herramientas MCP
- Seguimiento de errores con IDs de evento
- Monitoreo de rendimiento

### Comandos de Desarrollo MCP

**Desarrollo Local y Testing:**

```bash
# Iniciar servidor MCP principal (con OAuth)
wrangler dev                    # Disponible en http://localhost:8792/mcp
```

### Integración Claude Desktop

**Para Desarrollo Local:**

```json
{
  "mcpServers": {
    "database-mcp": {
      "command": "npx",
      "args": ["mcp-remote", "http://localhost:8792/mcp"],
      "env": {}
    }
  }
}
```

**Para Despliegue de Producción:**

```json
{
  "mcpServers": {
    "database-mcp": {
      "command": "npx",
      "args": ["mcp-remote", "https://your-worker.workers.dev/mcp"],
      "env": {}
    }
  }
}
```

### Conceptos Clave MCP para Este Proyecto

- **Herramientas**: Operaciones de base de datos (listTables, queryDatabase, executeDatabase)
- **Autenticación**: OAuth GitHub con control de acceso basado en roles
- **Transporte**: Soporte dual para protocolos HTTP (`/mcp`) y SSE (`/sse`)
- **Estado**: Durable Objects mantienen contexto de usuario autenticado
- **Seguridad**: Protección inyección SQL, validación permisos, sanitización errores

## Integración de Base de Datos y Seguridad

**CRÍTICO: Este proyecto proporciona acceso seguro a base de datos PostgreSQL a través de herramientas MCP con permisos basados en roles.**

### Arquitectura de Base de Datos

**Gestión de Conexiones (`src/database.ts`):**

```typescript
// Pool de conexiones singleton con límites Cloudflare Workers
export function getDb(databaseUrl: string): postgres.Sql {
  if (!dbInstance) {
    dbInstance = postgres(databaseUrl, {
      max: 5, // Máx 5 conexiones para Workers
      idle_timeout: 20,
      connect_timeout: 10,
      prepare: true, // Habilitar statements preparados
    });
  }
  return dbInstance;
}

// Wrapper de conexión con manejo de errores
export async function withDatabase<T>(databaseUrl: string, operation: (db: postgres.Sql) => Promise<T>): Promise<T> {
  const db = getDb(databaseUrl);
  // Ejecutar operación con timing y manejo de errores
}
```

### Implementación de Seguridad

**Protección Inyección SQL:**

```typescript
export function validateSqlQuery(sql: string): { isValid: boolean; error?: string } {
  const dangerousPatterns = [
    /;\s*drop\s+/i,
    /;\s*delete\s+.*\s+where\s+1\s*=\s*1/i,
    /;\s*truncate\s+/i,
    // ... más patrones
  ];
  // Validación basada en patrones para seguridad
}

export function isWriteOperation(sql: string): boolean {
  const writeKeywords = ["insert", "update", "delete", "create", "drop", "alter"];
  return writeKeywords.some((keyword) => sql.trim().toLowerCase().startsWith(keyword));
}
```

**Control de Acceso (`src/index.ts`):**

```typescript
const ALLOWED_USERNAMES = new Set<string>([
  'coleam00'  // Solo estos usernames de GitHub pueden ejecutar operaciones de escritura
]);

// Disponibilidad de herramientas basada en permisos de usuario
if (ALLOWED_USERNAMES.has(this.props.login)) {
  // Registrar herramienta executeDatabase para usuarios privilegiados
  this.server.tool("executeDatabase", ...);
}
```

### Implementación Herramientas MCP

**Sistema de Registro de Herramientas:**

Las herramientas ahora están organizadas de forma modular con registro centralizado:

1. **Registro de Herramientas (`src/tools/register-tools.ts`):**
   - Registro central que importa todos los módulos de herramientas
   - Llama funciones de registro individuales
   - Pasa servidor, entorno y props de usuario a cada módulo

2. **Patrón de Implementación de Herramientas:**
   - Cada característica/dominio tiene su propio archivo de herramientas (ej., `database-tools.ts`)
   - Las herramientas se exportan como funciones de registro
   - Las funciones de registro reciben instancia de servidor, entorno y props de usuario
   - La verificación de permisos ocurre durante el registro

**Ejemplo Registro de Herramientas:**

```typescript
// src/tools/register-tools.ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { Props } from "../types";
import { registerDatabaseTools } from "../../examples/database-tools";

export function registerAllTools(server: McpServer, env: Env, props: Props) {
  // Registrar herramientas de base de datos
  registerDatabaseTools(server, env, props);
  
  // Futuras herramientas pueden registrarse aquí
  // registerAnalyticsTools(server, env, props);
  // registerReportingTools(server, env, props);
}
```

**Ejemplo Módulo de Herramientas (`examples/database-tools.ts`):**

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { Props } from "../types";

const ALLOWED_USERNAMES = new Set<string>(['coleam00']);

export function registerDatabaseTools(server: McpServer, env: Env, props: Props) {
  // Herramienta 1: Disponible para todos los usuarios autenticados
  server.tool(
    "listTables",
    "Obtener lista de todas las tablas en la base de datos",
    ListTablesSchema,
    async () => {
      // Implementación
    }
  );

  // Herramienta 2: Disponible para todos los usuarios autenticados
  server.tool(
    "queryDatabase",
    "Ejecutar consulta SQL de solo lectura",
    QueryDatabaseSchema,
    async ({ sql }) => {
      // Implementación con validación
    }
  );

  // Herramienta 3: Solo para usuarios privilegiados
  if (ALLOWED_USERNAMES.has(props.login)) {
    server.tool(
      "executeDatabase",
      "Ejecutar cualquier statement SQL (privilegiado)",
      ExecuteDatabaseSchema,
      async ({ sql }) => {
        // Implementación
      }
    );
  }
}
```

**Herramientas de Base de Datos Disponibles en examples:**

1. **`listTables`** - Descubrimiento de esquema (todos los usuarios autenticados)
2. **`queryDatabase`** - Consultas SQL de solo lectura (todos los usuarios autenticados)
3. **`executeDatabase`** - Operaciones de escritura (solo usuarios privilegiados)

## Implementación OAuth de GitHub

**CRÍTICO: Este proyecto implementa flujo seguro OAuth 2.0 de GitHub con sistema de aprobación basado en cookies firmadas.**

### Arquitectura Flujo OAuth

**Flujo de Autenticación (`src/github-handler.ts`):**

```typescript
// 1. Solicitud de Autorización
app.get("/authorize", async (c) => {
  const oauthReqInfo = await c.env.OAUTH_PROVIDER.parseAuthRequest(c.req.raw);

  // Verificar si cliente ya aprobado vía cookie firmada
  if (await clientIdAlreadyApproved(c.req.raw, oauthReqInfo.clientId, c.env.COOKIE_ENCRYPTION_KEY)) {
    return redirectToGithub(c.req.raw, oauthReqInfo, c.env, {});
  }

  // Mostrar diálogo de aprobación
  return renderApprovalDialog(c.req.raw, { client, server, state });
});

// 2. Callback de GitHub
app.get("/callback", async (c) => {
  // Intercambiar código por token de acceso
  const [accessToken, errResponse] = await fetchUpstreamAuthToken({
    client_id: c.env.GITHUB_CLIENT_ID,
    client_secret: c.env.GITHUB_CLIENT_SECRET,
    code: c.req.query("code"),
    redirect_uri: new URL("/callback", c.req.url).href,
  });

  // Obtener información usuario GitHub
  const user = await new Octokit({ auth: accessToken }).rest.users.getAuthenticated();

  // Completar autorización con props de usuario
  return c.env.OAUTH_PROVIDER.completeAuthorization({
    props: { accessToken, email, login, name } as Props,
    userId: login,
  });
});
```

### Sistema de Seguridad de Cookies

**Cookies de Aprobación Firmadas HMAC (`src/workers-oauth-utils.ts`):**

```typescript
// Generar cookie firmada para aprobación de cliente
async function signData(key: CryptoKey, data: string): Promise<string> {
  const signatureBuffer = await crypto.subtle.sign("HMAC", key, enc.encode(data));
  return Array.from(new Uint8Array(signatureBuffer))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

// Verificar integridad de cookie
async function verifySignature(key: CryptoKey, signatureHex: string, data: string): Promise<boolean> {
  const signatureBytes = new Uint8Array(signatureHex.match(/.{1,2}/g)!.map((byte) => parseInt(byte, 16)));
  return await crypto.subtle.verify("HMAC", key, signatureBytes.buffer, enc.encode(data));
}
```

### Contexto de Usuario y Permisos

**Props de Usuario Autenticado:**

```typescript
type Props = {
  login: string; // Username GitHub
  name: string; // Nombre para mostrar
  email: string; // Dirección email
  accessToken: string; // Token acceso GitHub
};

// Disponible en herramientas MCP vía this.props
class MyMCP extends McpAgent<Env, Record<string, never>, Props> {
  async init() {
    // Acceder contexto usuario en cualquier herramienta
    const username = this.props.login;
    const hasWriteAccess = ALLOWED_USERNAMES.has(username);
  }
}
```

## Monitoreo y Observabilidad

**CRÍTICO: Este proyecto soporta integración opcional Sentry para monitoreo de producción e incluye logging por consola integrado.**

### Arquitectura de Logging

**Dos Opciones de Despliegue:**

1. **Versión Estándar (`src/index.ts`)**: Solo logging por consola
2. **Versión Sentry (`src/index_sentry.ts`)**: Instrumentación Sentry completa

### Integración Sentry (Opcional)

**Habilitar Monitoreo Sentry:**

```typescript
// src/index_sentry.ts - Listo para producción con monitoreo
import * as Sentry from "@sentry/cloudflare";

// Configuración Sentry
function getSentryConfig(env: Env) {
  return {
    dsn: env.SENTRY_DSN,
    tracesSampleRate: 1,  // 100% sampling de trazas
  };
}

// Instrumentar herramientas MCP con trazado
private registerTool(name: string, description: string, schema: any, handler: any) {
  this.server.tool(name, description, schema, async (args: any) => {
    return await Sentry.startNewTrace(async () => {
      return await Sentry.startSpan({
        name: `mcp.tool/${name}`,
        attributes: extractMcpParameters(args),
      }, async (span) => {
        // Establecer contexto de usuario
        Sentry.setUser({
          username: this.props.login,
          email: this.props.email,
        });

        try {
          return await handler(args);
        } catch (error) {
          span.setStatus({ code: 2 }); // error
          return handleError(error);  // Retorna error amigable con ID de evento
        }
      });
    });
  });
}
```

**Características Sentry Habilitadas:**

- **Seguimiento de Errores**: Captura automática de excepciones con contexto
- **Monitoreo de Rendimiento**: Trazado completo de solicitudes con 100% sample rate
- **Contexto de Usuario**: Información usuario GitHub vinculada a eventos
- **Trazado de Herramientas**: Cada llamada herramienta MCP trazada con parámetros
- **Trazado Distribuido**: Flujo de solicitudes a través de Cloudflare Workers

### Patrones de Logging de Producción

**Logging por Consola (Estándar):**

```typescript
// Operaciones base de datos
console.log(`Operación base de datos completada exitosamente en ${duration}ms`);
console.error(`Operación base de datos falló después de ${duration}ms:`, error);

// Eventos autenticación
console.log(`Usuario autenticado: ${this.props.login} (${this.props.name})`);

// Ejecución herramientas
console.log(`Herramienta llamada: ${toolName} por ${this.props.login}`);
console.error(`Herramienta falló: ${toolName}`, error);
```

**Manejo de Errores Estructurado:**

```typescript
// Sanitización errores para seguridad
export function formatDatabaseError(error: unknown): string {
  if (error instanceof Error) {
    if (error.message.includes("password")) {
      return "Falló autenticación base de datos. Por favor verificar credenciales.";
    }
    if (error.message.includes("timeout")) {
      return "Conexión base de datos agotó tiempo. Por favor intentar de nuevo.";
    }
    return `Error base de datos: ${error.message}`;
  }
  return "Ocurrió error desconocido en base de datos.";
}
```

### Configuración de Monitoreo

**Monitoreo de Desarrollo:**

```bash
# Habilitar Sentry en desarrollo
echo 'SENTRY_DSN=https://your-dsn@sentry.io/project' >> .dev.vars
echo 'NODE_ENV=development' >> .dev.vars

# Usar versión con Sentry habilitado
wrangler dev --config wrangler.jsonc  # Asegurar main = "src/index_sentry.ts"
```

**Monitoreo de Producción:**

```bash
# Establecer secretos de producción
wrangler secret put SENTRY_DSN
wrangler secret put NODE_ENV  # Establecer a "production"

# Desplegar con monitoreo
wrangler deploy
```

## Estándares de Desarrollo TypeScript

**CRÍTICO: Todas las herramientas MCP DEBEN seguir mejores prácticas TypeScript con validación Zod y manejo apropiado de errores.**

### Formato de Respuesta Estándar

**TODAS las herramientas DEBEN retornar objetos de respuesta compatibles con MCP:**

```typescript
import { z } from "zod";

// Herramienta con patrones TypeScript apropiados
this.server.tool(
  "standardizedTool",
  "Herramienta siguiendo formato de respuesta estándar",
  {
    name: z.string().min(1, "Nombre no puede estar vacío"),
    options: z.object({}).optional(),
  },
  async ({ name, options }) => {
    try {
      // Input ya validado por esquema Zod
      const result = await processName(name, options);

      // Retornar respuesta de éxito estandarizada
      return {
        content: [
          {
            type: "text",
            text: `**Éxito**\n\nProcesado: ${name}\n\n**Resultado:**\n\`\`\`json\n${JSON.stringify(result, null, 2)}\n\`\`\`\n\n**Tiempo de procesamiento:** 0.5s`,
          },
        ],
      };
    } catch (error) {
      // Retornar respuesta de error estandarizada
      return {
        content: [
          {
            type: "text",
            text: `**Error**\n\nProcesamiento falló: ${error instanceof Error ? error.message : String(error)}`,
            isError: true,
          },
        ],
      };
    }
  },
);
```

### Validación de Input con Zod

**TODOS los inputs de herramientas DEBEN validarse usando esquemas Zod:**

```typescript
import { z } from "zod";

// Definir esquemas de validación
const DatabaseQuerySchema = z.object({
  sql: z
    .string()
    .min(1, "Consulta SQL no puede estar vacía")
    .refine((sql) => sql.trim().toLowerCase().startsWith("select"), {
      message: "Solo consultas SELECT están permitidas",
    }),
  limit: z.number().int().positive().max(1000).optional(),
});

// Usar en definición de herramienta
this.server.tool(
  "queryDatabase",
  "Ejecutar consulta SQL de solo lectura",
  DatabaseQuerySchema, // Esquema Zod proporciona validación automática
  async ({ sql, limit }) => {
    // sql y limit ya están validados y tipados apropiadamente
    const results = await db.unsafe(sql);
    return { content: [{ type: "text", text: JSON.stringify(results, null, 2) }] };
  },
);
```

### Patrones de Manejo de Errores

**Respuestas de error estandarizadas:**

```typescript
// Utilidad manejo de errores
function createErrorResponse(message: string, details?: any): any {
  return {
    content: [{
      type: "text",
      text: `**Error**\n\n${message}${details ? `\n\n**Detalles:**\n\`\`\`json\n${JSON.stringify(details, null, 2)}\n\`\`\`` : ''}`,
      isError: true
    }]
  };
}

// Error de permisos
if (!ALLOWED_USERNAMES.has(this.props.login)) {
  return createErrorResponse(
    "Permisos insuficientes para esta operación",
    { requiredRole: "privilegiado", userRole: "estándar" }
  );
}

// Error de validación
if (isWriteOperation(sql)) {
  return createErrorResponse(
    "Operaciones de escritura no permitidas con esta herramienta",
    { operation: "escritura", allowedOperations: ["select", "show", "describe"] }
  );
}

// Error de base de datos
catch (error) {
  return createErrorResponse(
    "Operación de base de datos falló",
    { error: formatDatabaseError(error) }
  );
}
```

### Reglas de Seguridad de Tipos

**Patrones TypeScript OBLIGATORIOS:**

1. **Tipos Estrictos**: Todos los parámetros y tipos de retorno explícitamente tipados
2. **Validación Zod**: Todos los inputs validados con esquemas Zod
3. **Manejo de Errores**: Todas las operaciones async envueltas en try/catch
4. **Contexto de Usuario**: Props tipados con información usuario GitHub
5. **Entorno**: Tipos Cloudflare Workers generados con `wrangler types`

## Preferencias de Estilo de Código

### Estilo TypeScript

- Usar anotaciones de tipo explícitas para todos parámetros de función y tipos de retorno
- Usar comentarios JSDoc para todas las funciones y clases exportadas
- Preferir async/await para todas las operaciones asíncronas
- **OBLIGATORIO**: Usar esquemas Zod para toda validación de input
- **OBLIGATORIO**: Usar manejo apropiado de errores con bloques try/catch
- Mantener funciones pequeñas y enfocadas (principio de responsabilidad única)

### Organización de Archivos

- Cada servidor MCP debe ser auto-contenido en un solo archivo TypeScript
- Statements de import organizados: built-ins Node.js, paquetes terceros, imports locales
- Usar imports relativos dentro del directorio src/
- **Importar Zod para validación y tipos apropiados para todos los módulos**

### Convenciones de Testing

- Usar MCP Inspector para testing de integración: `npx @modelcontextprotocol/inspector@latest`
- Probar con servidor de desarrollo local: `wrangler dev`
- Usar nombres y descripciones de herramientas descriptivos
- **Probar escenarios tanto de autenticación como de permisos**
- **Probar validación de input con datos inválidos**

## Notas Importantes

### Qué NO hacer

- **NUNCA** hacer commit de secretos o variables de entorno al repositorio
- **NUNCA** construir soluciones complejas cuando simples funcionarán
- **NUNCA** saltarse validación de input con esquemas Zod

### Qué SÍ hacer

- **SIEMPRE** usar modo estricto TypeScript y tipado apropiado
- **SIEMPRE** validar inputs con esquemas Zod
- **SIEMPRE** seguir los principios fundamentales (KISS, YAGNI, etc.)
- **SIEMPRE** usar Wrangler CLI para todo desarrollo y despliegue

## Flujo de Trabajo Git

```bash
# Antes de hacer commit, siempre ejecutar:
npm run type-check              # Asegurar que TypeScript compila
wrangler dev --dry-run          # Probar configuración de despliegue

# Commit con mensajes descriptivos
git add .
git commit -m "feat: agregar nueva herramienta MCP para consultas base de datos"
```

## Referencia Rápida

### Agregar Nuevas Herramientas MCP

1. **Crear nuevo módulo de herramienta** en tu proyecto (siguiendo el patrón en `examples/`):
   ```typescript
   // src/tools/your-feature-tools.ts
   export function registerYourFeatureTools(server: McpServer, env: Env, props: Props) {
     // Registrar tus herramientas aquí
   }
   ```

2. **Definir esquemas Zod** para validación de input en tu archivo de tipos

3. **Implementar manejadores de herramientas** con manejo apropiado de errores usando los patrones de examples

4. **Registrar tus herramientas** en `src/tools/register-tools.ts`:
   ```typescript
   import { registerYourFeatureTools } from "./your-feature-tools";
   
   export function registerAllTools(server: McpServer, env: Env, props: Props) {
     // Registros existentes
     registerDatabaseTools(server, env, props);
     
     // Agregar tu nuevo registro
     registerYourFeatureTools(server, env, props);
   }
   ```

5. **Actualizar documentación** si es necesario