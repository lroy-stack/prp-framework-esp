/* eslint-disable */
/**
 * TIPOS DE CONFIGURACIÓN PARA CLOUDFLARE WORKERS - SERVIDOR MCP
 * 
 * Generado por Wrangler ejecutando `wrangler types` (hash: 8d2a1cc85ea5f1665750373459ceb7e1)
 * Tipos de runtime generados con workerd@1.20250709.0 2025-03-10 nodejs_compat
 * 
 * IMPORTANTE: Este archivo define el entorno de tipos para el servidor MCP
 * incluyendo variables de entorno, bindings y APIs disponibles.
 */

declare namespace Cloudflare {
	/**
	 * INTERFAZ DE ENTORNO PARA SERVIDOR MCP
	 * Define todas las variables y bindings disponibles en el Worker
	 */
	interface Env {
		// Almacenamiento KV para sesiones OAuth y datos temporales
		OAUTH_KV: KVNamespace;
		
		// Configuración GitHub OAuth (configurar como secrets)
		GITHUB_CLIENT_ID: string;        // ID público de aplicación GitHub
		GITHUB_CLIENT_SECRET: string;    // Secret de aplicación GitHub (CONFIDENCIAL)
		
		// Seguridad y cifrado
		COOKIE_ENCRYPTION_KEY: string;   // Clave para cifrar cookies de sesión (CONFIDENCIAL)
		
		// Base de datos PostgreSQL
		DATABASE_URL: string;            // URL de conexión PostgreSQL (CONFIDENCIAL)
		
		// APIs externas para funcionalidades avanzadas
		PERPLEXITY_API_KEY: string;      // API key para Perplexity AI (CONFIDENCIAL)
		ANTHROPIC_API_KEY: string;       // API key para Claude/Anthropic (CONFIDENCIAL)
		
		// Monitoreo y observabilidad
		SENTRY_DSN: string;              // DSN para Sentry error tracking (CONFIDENCIAL)
		
		// Configuración de entorno
		NODE_ENV: string;                // 'development' | 'production' | 'test'
		
		// Durable Objects para persistencia de estado
		MCP_OBJECT: DurableObjectNamespace<import("./src/index").MyMCP>;
		
		// Binding para Cloudflare AI
		AI: Ai;
	}
}

/**
 * INTERFAZ GLOBAL DEL ENTORNO
 * Extiende la configuración de Cloudflare para disponibilidad global
 */
interface Env extends Cloudflare.Env {}

/**
 * NOTAS DE CONFIGURACIÓN:
 * 
 * SECRETS (configurar con wrangler secret put):
 * - GITHUB_CLIENT_SECRET: Secret OAuth de GitHub
 * - COOKIE_ENCRYPTION_KEY: Clave para cifrar cookies (generar aleatoriamente)
 * - DATABASE_URL: postgres://usuario:password@host:puerto/base_datos
 * - PERPLEXITY_API_KEY: Para funcionalidades AI avanzadas
 * - ANTHROPIC_API_KEY: Para integración Claude
 * - SENTRY_DSN: Para monitoreo de errores
 * 
 * VARIABLES PÚBLICAS (configurar en wrangler.toml):
 * - GITHUB_CLIENT_ID: ID público de aplicación GitHub
 * - NODE_ENV: Entorno de ejecución
 * 
 * BINDINGS:
 * - OAUTH_KV: Almacenamiento clave-valor para sesiones
 * - MCP_OBJECT: Durable Object para persistencia
 * - AI: APIs de Cloudflare AI
 */

// Los tipos de runtime completos de Cloudflare Workers están disponibles
// pero omitidos aquí por brevedad. El archivo original contiene ~8000 líneas
// de definiciones de tipos para APIs web estándar y APIs específicas de Workers.

/**
 * APIS PRINCIPALES DISPONIBLES EN EL SERVIDOR MCP:
 * 
 * - fetch(): API para requests HTTP
 * - KVNamespace: Almacenamiento clave-valor
 * - DurableObject: Persistencia de estado
 * - Ai: Inferencia de modelos AI
 * - crypto: APIs criptográficas
 * - console: Logging y debugging
 * - setTimeout/setInterval: Timers
 * - TextEncoder/TextDecoder: Manipulación de texto
 * - URL/URLSearchParams: Manipulación de URLs
 * - Request/Response/Headers: APIs HTTP
 * - WebSocket: Comunicación en tiempo real
 * - ReadableStream/WritableStream: Streams
 * 
 * Para documentación completa de APIs:
 * https://developers.cloudflare.com/workers/runtime-apis/
 */