---
name: "Plantilla PRP Servidor MCP"
description: Esta plantilla está diseñada para proporcionar un servidor Model Context Protocol (MCP) listo para producción usando los patrones probados de esta base de código.
---

## Propósito

Plantilla optimizada para que agentes de IA implementen servidores Model Context Protocol (MCP) listos para producción con autenticación OAuth de GitHub, integración de base de datos y despliegue en Cloudflare Workers usando los patrones probados de esta base de código.

## Principios Fundamentales

1. **El Contexto es Rey**: Incluir TODOS los patrones MCP necesarios, flujos de autenticación y configuraciones de despliegue
2. **Bucles de Validación**: Proporcionar tests ejecutables desde compilación TypeScript hasta despliegue de producción
3. **Seguridad Primero**: Construir con autenticación, autorización y protección contra inyección SQL integrada
4. **Listo para Producción**: Incluir monitoreo, manejo de errores y automatización de despliegue

---

## Objetivo

Construir un servidor MCP (Model Context Protocol) listo para producción con:

- [FUNCIONALIDAD MCP ESPECÍFICA] - describir las herramientas y recursos específicos a implementar
- Autenticación OAuth GitHub con control de acceso basado en roles
- Despliegue Cloudflare Workers con monitoreo
- [CARACTERÍSTICAS ADICIONALES] - cualquier característica específica más allá de la autenticación/base de datos base

## Por Qué

- **Productividad del Desarrollador**: Habilitar acceso seguro de asistente IA a [DATOS/OPERACIONES ESPECÍFICAS]
- **Seguridad Empresarial**: OAuth GitHub con sistema de permisos granular
- **Escalabilidad**: Despliegue edge global de Cloudflare Workers
- **Integración**: [CÓMO ESTO ENCAJA CON SISTEMAS EXISTENTES]
- **Valor del Usuario**: [BENEFICIOS ESPECÍFICOS PARA USUARIOS FINALES]

## Qué

### Características del Servidor MCP

**Herramientas MCP Principales:**

- Las herramientas están organizadas en archivos modulares y registradas vía `src/tools/register-tools.ts`
- Cada característica/dominio obtiene su propio archivo de registro de herramientas (ej., `database-tools.ts`, `analytics-tools.ts`)
- [LISTAR HERRAMIENTAS ESPECÍFICAS] - ej., "queryDatabase", "listTables", "executeOperations"
- La autenticación de usuario y validación de permisos ocurre durante el registro de herramientas
- Manejo comprensivo de errores y logging
- [HERRAMIENTAS ESPECÍFICAS DEL DOMINIO] - herramientas específicas para tu caso de uso

**Autenticación y Autorización:**

- Integración OAuth 2.0 GitHub con sistema de aprobación de cookies firmadas
- Control de acceso basado en roles (usuarios solo lectura vs privilegiados)
- Propagación de contexto de usuario a todas las herramientas MCP
- Gestión de sesión segura con cookies firmadas HMAC

**Integración de Base de Datos:**

- Pool de conexiones PostgreSQL con limpieza automática
- Protección contra inyección SQL y validación de consultas
- Separación de operaciones lectura/escritura basada en permisos de usuario
- Sanitización de errores para prevenir fuga de información

**Despliegue y Monitoreo:**

- Cloudflare Workers con Durable Objects para gestión de estado
- Integración opcional Sentry para seguimiento de errores y monitoreo de rendimiento
- Configuración basada en entorno (desarrollo vs producción)
- Logging en tiempo real y alertas

### Criterios de Éxito

- [ ] Servidor MCP pasa validación con MCP Inspector
- [ ] Flujo OAuth GitHub funciona de extremo a extremo (autorización → callback → acceso MCP)
- [ ] Compilación TypeScript exitosa sin errores
- [ ] Servidor de desarrollo local inicia y responde correctamente
- [ ] Despliegue de producción a Cloudflare Workers exitoso
- [ ] Autenticación previene acceso no autorizado a operaciones sensibles
- [ ] Manejo de errores proporciona mensajes amigables sin filtrar detalles del sistema
- [ ] [CRITERIOS DE ÉXITO ESPECÍFICOS DEL DOMINIO]

## Todo el Contexto Necesario

### Documentación y Referencias (LECTURA OBLIGATORIA)

```yaml
# PATRONES MCP CRÍTICOS - Leer primero
- docfile: PRPs/ai_docs/mcp_patterns.md
  why: Patrones principales desarrollo MCP, prácticas seguridad y manejo errores

# Ejemplos código críticos
- docfile: PRPs/ai_docs/claude_api_usage.md
  why: Cómo usar la API Anthropic para obtener respuesta de un LLM

# SISTEMA REGISTRO HERRAMIENTAS - Entender enfoque modular
- file: src/tools/register-tools.ts
  why: Registro central mostrando cómo todas las herramientas son importadas y registradas - ESTUDIAR este patrón

# HERRAMIENTAS MCP EJEMPLO - Mirar aquí cómo crear y registrar nuevas herramientas
- file: examples/database-tools.ts
  why: Herramientas ejemplo para servidor MCP Postgres mostrando mejores prácticas para creación y registro herramientas

- file: examples/database-tools-sentry.ts
  why: Herramientas ejemplo para servidor MCP Postgres pero con integración Sentry para monitoreo producción

# PATRONES BASE CÓDIGO EXISTENTE - Estudiar estas implementaciones
- file: src/index.ts
  why: Servidor MCP completo con autenticación, base datos y herramientas - REFLEJAR este patrón

- file: src/github-handler.ts
  why: Implementación flujo OAuth - USAR este patrón exacto para autenticación

- file: src/database.ts
  why: Seguridad base datos, pool conexiones, validación SQL - SEGUIR estos patrones

- file: wrangler.jsonc
  why: Configuración Cloudflare Workers - COPIAR este patrón para despliegue

# DOCUMENTACIÓN OFICIAL MCP
- url: https://modelcontextprotocol.io/docs/concepts/tools
  why: Registro herramientas MCP y patrones definición esquemas

- url: https://modelcontextprotocol.io/docs/concepts/resources
  why: Implementación recursos MCP si es necesario

# Agregar documentación relacionada al caso uso del usuario según sea necesario abajo
```

### Árbol Base Código Actual (Ejecutar `tree -I node_modules` en raíz proyecto)

```bash
# INSERTAR SALIDA TREE REAL AQUÍ
/
├── src/
│   ├── index.ts                 # Servidor MCP principal autenticado ← ESTUDIAR ESTO
│   ├── index_sentry.ts         # Versión monitoreo Sentry
│   ├── simple-math.ts          # Ejemplo MCP básico ← BUEN PUNTO PARTIDA
│   ├── github-handler.ts       # Implementación OAuth ← USAR ESTE PATRÓN
│   ├── database.ts             # Utilidades base datos ← PATRONES SEGURIDAD
│   ├── utils.ts                # Auxiliares OAuth
│   ├── workers-oauth-utils.ts  # Sistema seguridad cookies
│   └── tools/                  # Sistema registro herramientas
│       └── register-tools.ts   # Registro central herramientas ← ENTENDER ESTO
├── PRPs/
│   ├── templates/prp_mcp_base.md  # Esta plantilla
│   └── ai_docs/                   # Guías implementación ← LEER TODO
├── examples/                   # Implementaciones ejemplo herramientas
│   ├── database-tools.ts       # Ejemplo herramientas base datos ← SEGUIR PATRÓN
│   └── database-tools-sentry.ts # Con monitoreo Sentry
├── wrangler.jsonc              # Config Cloudflare ← COPIAR PATRONES
├── package.json                # Dependencias
└── tsconfig.json               # Config TypeScript
```

### Árbol Base Código Deseado (Archivos agregar/modificar) relacionado al caso uso del usuario según necesario abajo

```bash

```

### Gotchas Conocidos y Patrones Críticos MCP/Cloudflare

```typescript
// CRÍTICO: Cloudflare Workers requieren patrones específicos
// 1. SIEMPRE implementar limpieza para Durable Objects
export class YourMCP extends McpAgent<Env, Record<string, never>, Props> {
  async cleanup(): Promise<void> {
    await closeDb(); // CRÍTICO: Cerrar conexiones base datos
  }

  async alarm(): Promise<void> {
    await this.cleanup(); // CRÍTICO: Manejar alarmas Durable Object
  }
}

// 2. SIEMPRE validar SQL para prevenir inyección (usar patrones existentes)
const validation = validateSqlQuery(sql); // desde src/database.ts
if (!validation.isValid) {
  return createErrorResponse(validation.error);
}

// 3. SIEMPRE verificar permisos antes operaciones sensibles
const ALLOWED_USERNAMES = new Set(["admin1", "admin2"]);
if (!ALLOWED_USERNAMES.has(this.props.login)) {
  return createErrorResponse("Permisos insuficientes");
}

// 4. SIEMPRE usar wrapper withDatabase para gestión conexión
return await withDatabase(this.env.DATABASE_URL, async (db) => {
  // Operaciones base datos aquí
});

// 5. SIEMPRE usar Zod para validación input
import { z } from "zod";
const schema = z.object({
  param: z.string().min(1).max(100),
});

// 6. Compilación TypeScript requiere coincidencia exacta interfaces
interface Env {
  DATABASE_URL: string;
  GITHUB_CLIENT_ID: string;
  GITHUB_CLIENT_SECRET: string;
  OAUTH_KV: KVNamespace;
  // Agregar tus variables entorno aquí
}
```

## Plan de Implementación

### Modelos de Datos y Tipos

Definir interfaces TypeScript y esquemas Zod para seguridad de tipos y validación.

```typescript
// Props autenticación usuario (heredados de OAuth)
type Props = {
  login: string; // Username GitHub
  name: string; // Nombre para mostrar
  email: string; // Dirección email
  accessToken: string; // Token acceso GitHub
};

// Esquemas input herramientas MCP (personalizar para tus herramientas)
const YourToolSchema = z.object({
  param1: z.string().min(1, "Parámetro no puede estar vacío"),
  param2: z.number().int().positive().optional(),
  options: z.object({}).optional(),
});

// Interface entorno (agregar tus variables)
interface Env {
  DATABASE_URL: string;
  GITHUB_CLIENT_ID: string;
  GITHUB_CLIENT_SECRET: string;
  OAUTH_KV: KVNamespace;
  // TU_VAR_ENV_ESPECÍFICA: string;
}

// Niveles permisos (personalizar para tu caso uso)
enum Permission {
  READ = "read",
  WRITE = "write",
  ADMIN = "admin",
}
```

### Lista de Tareas (Completar en orden)

```yaml
Tarea 1 - Configuración Proyecto:
  COPIAR wrangler.jsonc a wrangler-[nombre-servidor].jsonc:
    - MODIFICAR campo name a "[nombre-servidor]"
    - AGREGAR cualquier nueva variable entorno a sección vars
    - MANTENER configuración OAuth y base datos existente

  CREAR archivo .dev.vars (si no existe):
    - AGREGAR GITHUB_CLIENT_ID=tu_client_id
    - AGREGAR GITHUB_CLIENT_SECRET=tu_client_secret
    - AGREGAR DATABASE_URL=postgresql://...
    - AGREGAR COOKIE_ENCRYPTION_KEY=tu_clave_32_bytes
    - AGREGAR cualquier variable entorno específica dominio

Tarea 2 - App OAuth GitHub:
  CREAR nueva app OAuth GitHub:
    - ESTABLECER URL homepage: https://tu-worker.workers.dev
    - ESTABLECER URL callback: https://tu-worker.workers.dev/callback
    - COPIAR client ID y secret a .dev.vars

  O REUSAR app OAuth existente:
    - ACTUALIZAR URL callback si usando subdominio diferente
    - VERIFICAR client ID y secret en entorno

Tarea 3 - Implementación Servidor MCP:
  CREAR src/[nombre-servidor].ts O MODIFICAR src/index.ts:
    - COPIAR estructura clase desde src/index.ts
    - MODIFICAR nombre servidor y versión en constructor McpServer
    - LLAMAR registerAllTools(server, env, props) en método init()
    - MANTENER patrones autenticación y base datos idénticos

  CREAR módulos herramientas:
    - CREAR nuevos archivos herramientas siguiendo patrón examples/database-tools.ts
    - EXPORTAR funciones registro que acepten (server, env, props)
    - USAR esquemas Zod para validación input
    - IMPLEMENTAR manejo errores apropiado con createErrorResponse
    - AGREGAR verificación permisos durante registro herramientas

  ACTUALIZAR registro herramientas:
    - MODIFICAR src/tools/register-tools.ts para importar tus nuevas herramientas
    - AGREGAR llamada tu función registro en registerAllTools()

Tarea 4 - Integración Base Datos (si necesario):
  USAR patrones base datos existentes desde src/database.ts:
    - IMPORTAR withDatabase, validateSqlQuery, isWriteOperation
    - IMPLEMENTAR operaciones base datos con validación seguridad
    - SEPARAR operaciones lectura vs escritura basado en permisos usuario
    - USAR formatDatabaseError para mensajes error amigables

Tarea 5 - Configuración Entorno:
  CONFIGURAR namespace Cloudflare KV:
    - EJECUTAR: wrangler kv namespace create "OAUTH_KV"
    - ACTUALIZAR wrangler.jsonc con ID namespace retornado

  ESTABLECER secretos producción:
    - EJECUTAR: wrangler secret put GITHUB_CLIENT_ID
    - EJECUTAR: wrangler secret put GITHUB_CLIENT_SECRET
    - EJECUTAR: wrangler secret put DATABASE_URL
    - EJECUTAR: wrangler secret put COOKIE_ENCRYPTION_KEY

Tarea 6 - Testing Local:
  PROBAR funcionalidad básica:
    - EJECUTAR: wrangler dev
    - VERIFICAR servidor inicia sin errores
    - PROBAR flujo OAuth: http://localhost:8792/authorize
    - VERIFICAR endpoint MCP: http://localhost:8792/mcp

Tarea 7 - Despliegue Producción:
  DESPLEGAR a Cloudflare Workers:
    - EJECUTAR: wrangler deploy
    - VERIFICAR éxito despliegue
    - PROBAR flujo OAuth producción
    - VERIFICAR accesibilidad endpoint MCP
```

### Detalles Implementación por Tarea

```typescript
// Tarea 3 - Patrón Implementación Servidor MCP
export class YourMCP extends McpAgent<Env, Record<string, never>, Props> {
  server = new McpServer({
    name: "Nombre Tu Servidor MCP",
    version: "1.0.0",
  });

  // CRÍTICO: Siempre implementar limpieza
  async cleanup(): Promise<void> {
    try {
      await closeDb();
      console.log("Conexiones base datos cerradas exitosamente");
    } catch (error) {
      console.error("Error durante limpieza base datos:", error);
    }
  }

  async alarm(): Promise<void> {
    await this.cleanup();
  }

  async init() {
    // PATRÓN: Usar registro herramientas centralizado
    registerAllTools(this.server, this.env, this.props);
  }
}

// Tarea 3 - Patrón Módulo Herramientas (ej., src/tools/your-feature-tools.ts)
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { Props } from "../types";
import { z } from "zod";

const PRIVILEGED_USERS = new Set(["admin1", "admin2"]);

export function registerYourFeatureTools(server: McpServer, env: Env, props: Props) {
  // Herramienta 1: Disponible para todos usuarios autenticados
  server.tool(
    "tuHerramientaBasica",
    "Descripción de tu herramienta básica",
    YourToolSchema, // Esquema validación Zod
    async ({ param1, param2, options }) => {
      try {
        // PATRÓN: Implementación herramienta con manejo errores
        const result = await performOperation(param1, param2, options);

        return {
          content: [
            {
              type: "text",
              text: `**Éxito**\n\nOperación completada\n\n**Resultado:**\n\`\`\`json\n${JSON.stringify(result, null, 2)}\n\`\`\``,
            },
          ],
        };
      } catch (error) {
        return createErrorResponse(`Operación falló: ${error.message}`);
      }
    },
  );

  // Herramienta 2: Solo para usuarios privilegiados
  if (PRIVILEGED_USERS.has(props.login)) {
    server.tool(
      "herramientaPrivilegiada",
      "Herramienta administrativa para usuarios privilegiados",
      { action: z.string() },
      async ({ action }) => {
        // Implementación
        return {
          content: [
            {
              type: "text",
              text: `Acción admin '${action}' ejecutada por ${props.login}`,
            },
          ],
        };
      },
    );
  }
}

// Tarea 3 - Actualizar Registro Herramientas (src/tools/register-tools.ts)
import { registerYourFeatureTools } from "./your-feature-tools";

export function registerAllTools(server: McpServer, env: Env, props: Props) {
  // Registros existentes
  registerDatabaseTools(server, env, props);
  
  // Agregar tu nuevo registro
  registerYourFeatureTools(server, env, props);
}

// PATRÓN: Exportar proveedor OAuth con endpoints MCP
export default new OAuthProvider({
  apiHandlers: {
    "/sse": YourMCP.serveSSE("/sse") as any,
    "/mcp": YourMCP.serve("/mcp") as any,
  },
  authorizeEndpoint: "/authorize",
  clientRegistrationEndpoint: "/register",
  defaultHandler: GitHubHandler as any,
  tokenEndpoint: "/token",
});
```

### Puntos de Integración

```yaml
CLOUDFLARE_WORKERS:
  - wrangler.jsonc: Actualizar nombre, variables entorno, bindings KV
  - Secretos entorno: Credenciales OAuth GitHub, URL base datos, clave encriptación
  - Durable Objects: Configurar binding agente MCP para persistencia estado

GITHUB_OAUTH:
  - App GitHub: Crear con URL callback coincidiendo tu dominio Workers
  - Credenciales cliente: Almacenar como secretos Cloudflare Workers
  - URL Callback: Debe coincidir exactamente: https://tu-worker.workers.dev/callback

BASE_DATOS:
  - Conexión PostgreSQL: Usar patrones pool conexiones existentes
  - Variable entorno: DATABASE_URL con string conexión completo
  - Seguridad: Usar validateSqlQuery e isWriteOperation para todo SQL

VARIABLES_ENTORNO:
  - Desarrollo: Archivo .dev.vars para testing local
  - Producción: Secretos Cloudflare Workers para despliegue
  - Requeridas: GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, DATABASE_URL, COOKIE_ENCRYPTION_KEY

ALMACENAMIENTO_KV:
  - Estado OAuth: Usado por proveedor OAuth para gestión estado
  - Namespace: Crear con `wrangler kv namespace create "OAUTH_KV"`
  - Configuración: Agregar ID namespace a bindings wrangler.jsonc
```

## Puerta de Validación

### Nivel 1: TypeScript y Configuración

```bash
# CRÍTICO: Ejecutar PRIMERO - corregir errores antes proceder
npm run type-check                 # Compilación TypeScript
wrangler types                     # Generar tipos Cloudflare Workers

# Esperado: Sin errores TypeScript
# Si errores: Corregir problemas tipos, interfaces faltantes, problemas import
```

### Nivel 2: Testing Desarrollo Local

```bash
# Iniciar servidor desarrollo local
wrangler dev

# Probar flujo OAuth (debe redirigir a GitHub)
curl -v http://localhost:8792/authorize

# Probar endpoint MCP (debe retornar info servidor)
curl -v http://localhost:8792/mcp

# Esperado: Servidor inicia, OAuth redirige a GitHub, MCP responde con info servidor
# Si errores: Verificar salida consola, verificar variables entorno, corregir configuración
```

### Nivel 3: Probar unitariamente cada característica, función y archivo, siguiendo patrones testing existentes si están ahí.

```bash
npm run test
```

Ejecutar tests unitarios con comando anterior (Vitest) para asegurar que toda funcionalidad esté funcionando.

### Nivel 4: Testing Integración Base Datos (si aplicable)

```bash
# Probar conexión base datos
curl -X POST http://localhost:8792/mcp \
  -H "Content-Type: application/json" \
  -d '{"method": "tools/call", "params": {"name": "listTables", "arguments": {}}}'

# Probar validación permisos
# Probar protección inyección SQL y otros tipos seguridad si aplicable
# Probar manejo errores para fallas base datos

# Esperado: Operaciones base datos funcionan, permisos aplicados, errores manejados graciosamente, etc.
# Si errores: Verificar DATABASE_URL, configuración conexión, lógica permisos
```

## Lista Verificación Validación Final

### Funcionalidad Principal

- [ ] Compilación TypeScript: `npm run type-check` pasa
- [ ] Tests unitarios pasan: `npm run test` pasa
- [ ] Servidor local inicia: `wrangler dev` ejecuta sin errores
- [ ] Endpoint MCP responde: `curl http://localhost:8792/mcp` retorna info servidor
- [ ] Flujo OAuth funciona: Autenticación redirige y completa exitosamente

---

## Anti-Patrones a Evitar

### Específicos MCP

- ❌ No saltarse validación input con Zod - siempre validar parámetros herramientas
- ❌ No olvidar implementar método cleanup() para Durable Objects
- ❌ No hardcodear permisos usuario - usar sistemas permisos configurables

### Proceso Desarrollo

- ❌ No saltarse bucles validación - cada nivel captura problemas diferentes
- ❌ No adivinar configuración OAuth - probar flujo completo
- ❌ No desplegar sin monitoreo - implementar logging y seguimiento errores
- ❌ No ignorar errores TypeScript - corregir todos problemas tipos antes despliegue