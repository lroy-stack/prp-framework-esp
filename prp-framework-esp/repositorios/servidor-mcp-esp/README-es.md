# Generador de Servidores MCP - Caso de Uso de Ingeniería de Contexto

Este caso de uso demuestra cómo utilizar la **Ingeniería de Contexto** y el **proceso PRP (Prompt de Requisitos de Producto)** para construir servidores del Protocolo de Contexto de Modelo (MCP) listos para producción. Proporciona un template probado y flujo de trabajo para crear servidores MCP con autenticación GitHub OAuth, integración de base de datos y despliegue en Cloudflare Workers.

> Un PRP es PRD + inteligencia de código curada + agente/runbook—el paquete mínimo viable que necesita una IA para enviar código listo para producción en el primer intento.

## 🎯 Lo Que Aprenderás

Este caso de uso te enseña cómo:

- **Usar el proceso PRP** para construir sistemáticamente servidores MCP complejos
- **Aprovechar la ingeniería de contexto especializada** para desarrollo MCP
- **Seguir patrones probados** desde un template de servidor MCP listo para producción
- **Implementar autenticación segura** con GitHub OAuth y control de acceso basado en roles
- **Desplegar en Cloudflare Workers** con monitoreo y manejo de errores

## 📋 Cómo Funciona - El Proceso PRP para Servidores MCP

### 1. Define Tu Servidor MCP (initial.md)

Comienza describiendo el servidor MCP exacto que quieres construir en `PRPs/INITIAL.md`:

```markdown
## FEATURE:
Queremos crear un servidor MCP meteorológico que proporcione datos meteorológicos
en tiempo real con caché y limitación de velocidad.

## ADDITIONAL FEATURES:
- Integración con API de OpenWeatherMap
- Caché Redis para rendimiento
- Limitación de velocidad por usuario
- Acceso a datos meteorológicos históricos
- Búsqueda de ubicación y autocompletado

## OTHER CONSIDERATIONS:
- Gestión de claves API para servicios externos
- Manejo adecuado de errores para fallos de API
- Validación de coordenadas para consultas de ubicación
```

### 2. Genera Tu PRP

Usa el comando PRP especializado para MCP para crear un plan de implementación completo:

```bash
/prp-mcp-create INITIAL.md
```

**Lo que hace esto:**
- Lee tu solicitud de funcionalidad
- Investiga los patrones de código base MCP existentes
- Estudia patrones de autenticación e integración de base de datos
- Crea un PRP completo en `PRPs/tu-nombre-servidor.md`
- Incluye todo el contexto, bucles de validación y tareas paso a paso

> Es importante después de que tu PRP se genere validar todo! Con el framework PRP, estás destinado a ser parte del proceso para asegurar la calidad de todo el contexto! Una ejecución es solo tan buena como tu PRP. Usa /prp-mcp-create como un punto de partida sólido.

### 3. Ejecuta Tu PRP

Usa el comando de ejecución MCP especializado para construir tu servidor:

```bash
/prp-mcp-execute PRPs/tu-nombre-servidor.md
```

**Lo que hace esto:**
- Carga el PRP completo con todo el contexto
- Crea un plan de implementación detallado usando TodoWrite
- Implementa cada componente siguiendo patrones probados
- Ejecuta validación completa (TypeScript, tests, despliegue)
- Asegura que tu servidor MCP funcione de extremo a extremo

## 🏗️ Ingeniería de Contexto Específica para MCP

Este caso de uso incluye componentes de ingeniería de contexto especializados diseñados específicamente para desarrollo de servidores MCP:

### Comandos Slash Especializados

Ubicados en `.claude/commands/`:

- **`/prp-mcp-create`** - Genera PRPs específicamente para servidores MCP
- **`/prp-mcp-execute`** - Ejecuta PRPs MCP con validación completa

Estas son versiones especializadas de los comandos genéricos en el `.claude/commands/` raíz, pero adaptadas para patrones de desarrollo MCP.

### Template PRP Especializado

El template `PRPs/templates/prp_mcp_base.md` incluye:

- **Patrones específicos de MCP** para registro de herramientas y autenticación
- **Configuración de Cloudflare Workers** para despliegue
- **Patrones de integración GitHub OAuth**
- **Seguridad de base de datos** y protección contra inyección SQL
- **Bucles de validación completos** desde TypeScript hasta producción

### Documentación AI

La carpeta `PRPs/ai_docs/` contiene:

- **`mcp_patterns.md`** - Patrones básicos de desarrollo MCP y prácticas de seguridad
- **`claude_api_usage.md`** - Cómo integrar con la API de Anthropic para características impulsadas por LLM

## 🔧 Arquitectura del Template

Este template proporciona un servidor MCP completo y listo para producción con:

### Componentes Principales

```
src/
├── index.ts                 # Servidor MCP autenticado principal
├── index_sentry.ts         # Versión con monitoreo Sentry
├── simple-math.ts          # Ejemplo MCP básico (sin autenticación)
├── github-handler.ts       # Implementación completa GitHub OAuth
├── database.ts             # PostgreSQL con patrones de seguridad
├── utils.ts                # Ayudantes OAuth y utilidades
├── workers-oauth-utils.ts  # Sistema de cookies firmadas HMAC
└── tools/                  # Sistema de registro de herramientas modular
    └── register-tools.ts   # Registro central de herramientas
```

### Herramientas de Ejemplo

La carpeta `examples/` muestra cómo crear herramientas MCP:

- **`database-tools.ts`** - Herramientas de base de datos de ejemplo con patrones adecuados
- **`database-tools-sentry.ts`** - Mismas herramientas con monitoreo Sentry

### Características Clave

- **🔐 GitHub OAuth** - Flujo de autenticación completo con control de acceso basado en roles
- **🗄️ Integración de Base de Datos** - PostgreSQL con pooling de conexiones y seguridad
- **🛠️ Herramientas Modulares** - Separación limpia de responsabilidades con registro central
- **☁️ Cloudflare Workers** - Despliegue global en el edge con Durable Objects
- **📊 Monitoreo** - Integración Sentry opcional para producción
- **🧪 Testing** - Validación completa desde TypeScript hasta despliegue

## 🚀 Inicio Rápido

### Prerequisitos

- Node.js y npm instalados
- Cuenta de Cloudflare (tier gratuito funciona)
- Cuenta de GitHub para OAuth
- Base de datos PostgreSQL (local o hospedada)

### Paso 1: Clonar y Configurar

```bash
# Clonar el template de ingeniería de contexto
git clone https://github.com/coleam00/Context-Engineering-Intro.git
cd Context-Engineering-Intro/use-cases/mcp-server

# Instalar dependencias
npm install

# Instalar Wrangler CLI globalmente
npm install -g wrangler

# Autenticar con Cloudflare
wrangler login
```

### Paso 2: Configurar Entorno

```bash
# Crear archivo de entorno
cp .dev.vars.example .dev.vars

# Editar .dev.vars con tus credenciales
# - Credenciales de app GitHub OAuth
# - String de conexión de base de datos
# - Clave de encriptación de cookies
```

### Paso 3: Define Tu Servidor MCP

Edita `PRPs/INITIAL.md` para describir los requisitos específicos de tu servidor MCP:

```markdown
## FEATURE:
Describe exactamente lo que tu servidor MCP debería hacer - sé específico sobre
funcionalidad, fuentes de datos e interacciones de usuario.

## ADDITIONAL FEATURES:
- Lista características específicas más allá de operaciones CRUD básicas
- Incluye integraciones con APIs externas
- Menciona cualquier requisito especial

## OTHER CONSIDERATIONS:
- Requisitos de autenticación
- Consideraciones de rendimiento
- Requisitos de seguridad
- Necesidades de limitación de velocidad
```

### Paso 4: Generar y Ejecutar PRP

```bash
# Generar PRP completo
/prp-mcp-create INITIAL.md

# Ejecutar el PRP para construir tu servidor
/prp-mcp-execute PRPs/tu-nombre-servidor.md
```

### Paso 5: Probar y Desplegar

```bash
# Probar localmente
wrangler dev

# Probar con MCP Inspector
npx @modelcontextprotocol/inspector@latest
# Conectar a: http://localhost:8792/mcp

# Desplegar a producción
wrangler deploy
```

## 🔍 Archivos Clave para Entender

Para entender completamente este caso de uso, examina estos archivos:

### Componentes de Ingeniería de Contexto

- **`PRPs/templates/prp_mcp_base.md`** - Template PRP especializado para MCP
- **`.claude/commands/prp-mcp-create.md`** - Generación PRP específica para MCP
- **`.claude/commands/prp-mcp-execute.md`** - Ejecución específica para MCP

### Patrones de Implementación

- **`src/index.ts`** - Servidor MCP completo con autenticación
- **`examples/database-tools.ts`** - Patrones de creación y registro de herramientas
- **`src/tools/register-tools.ts`** - Sistema de registro de herramientas modular

### Configuración y Despliegue

- **`wrangler.jsonc`** - Configuración de Cloudflare Workers
- **`.dev.vars.example`** - Template de variables de entorno
- **`CLAUDE.md`** - Directrices de implementación y patrones

## 📈 Métricas de Éxito

Cuando uses exitosamente este proceso, lograrás:

- **Implementación Rápida** - Tener rápidamente un Servidor MCP con iteraciones mínimas
- **Listo para Producción** - Autenticación segura, monitoreo y manejo de errores
- **Arquitectura Escalable** - Separación limpia de responsabilidades y diseño modular
- **Testing Completo** - Validación desde TypeScript hasta despliegue en producción

## 🤝 Contribuir

Este caso de uso demuestra el poder de la Ingeniería de Contexto para desarrollo de software complejo. Para mejorarlo:

1. **Agregar nuevos ejemplos de servidores MCP** para mostrar diferentes patrones
2. **Mejorar los templates PRP** con contexto más completo
3. **Mejorar bucles de validación** para mejor detección de errores
4. **Documentar casos extremos** y errores comunes

El objetivo es hacer que el desarrollo de servidores MCP sea predecible y exitoso a través de ingeniería de contexto completa.

---

**¿Listo para construir tu servidor MCP?** Comienza editando `PRPs/INITIAL.md` y ejecuta `/prp-mcp-create INITIAL.md` para generar tu plan de implementación completo.