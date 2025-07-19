---
name: "prp-mcp-create"
description: Este comando está diseñado para crear un Prompt de Requisitos de Producto (PRP) integral para construir servidores del Protocolo de Contexto de Modelo (MCP) referenciando los patrones de esta base de código que refleja las configuraciones de herramientas para los requisitos específicos del usuario.
Usage: /prp-mcp-create ruta/al/prp.md
Example usage: /prp-mcp-create weather-server "Servidor MCP para datos meteorológicos con integración de API"
Example usage: /prp-mcp-create file-manager "Servidor MCP que refleja el task master mcp"
```
---

# Crear PRP de Servidor MCP

Crear un Prompt de Requisitos de Producto (PRP) integral para construir servidores del Protocolo de Contexto de Modelo (MCP) con autenticación, integración de base de datos y despliegue en Cloudflare Workers.

Antes de comenzar, asegúrate de leer estos archivos clave para obtener una comprensión sobre el objetivo del PRP:
PRPs/README.md
PRPs/templates/prp_mcp_base.md (Este PRP base ya está parcialmente completado basado en la estructura del proyecto, pero por favor termínalo específico para el caso de uso del usuario para un servidor MCP)

## Caso de uso MCP del usuario: $ARGUMENTS

## Propósito

Generar PRPs ricos en contexto específicamente diseñados para el desarrollo de servidores MCP, utilizando los patrones probados en esta base de código que es un andamiaje de una configuración de servidor MCP sobre la cual el usuario puede construir, incluyendo GitHub OAuth y despliegue listo para producción en Cloudflare Workers.

Ninguna de las herramientas existentes probablemente será reutilizada y las herramientas deben crearse para el caso de uso del usuario específicamente adaptadas a sus necesidades.

## Proceso de Ejecución

1. **Investigación y Recopilación de Contexto**
   - Crear todos claros y generar subagentes para buscar en la base de código características/patrones similares. Piensa profundamente y planifica tu enfoque
   - Recopilar documentación relevante sobre herramientas MCP, recursos y flujos de autenticación
   - Investigar patrones de herramientas existentes para entender cómo construir el caso de uso especificado por el usuario
   - Estudiar patrones de integración existentes en la base de código

2. **Generar PRP Integral**
   - Usar la plantilla especializada `PRPs/templates/prp_mcp_base.md` como base
   - Personalizar la plantilla con requisitos específicos del servidor y funcionalidad
   - Incluir todo el contexto necesario de los patrones de la base de código y ai_docs
   - Agregar bucles de validación específicos para el desarrollo de servidores MCP
   - Incluir patrones de integración de base de datos y consideraciones de seguridad

3. **Mejorar con Documentos AI**
   - El usuario podría haber agregado documentos en el directorio PRPs/ai_docs/ que deberías leer
   - Si hay documentos en el directorio PRPs/ai_docs/, revísalos y tómalos en contexto mientras construyes el PRP

## Detalles de Implementación

### Estructura PRP para Servidores MCP

El PRP generado usa la plantilla especializada `PRPs/templates/prp_mcp_base.md` e incluye:

- **Objetivo**: Descripción clara del servidor MCP a construir con autenticación e integración de base de datos
- **Contexto**: Toda la documentación necesaria incluyendo referencias de PRPs/ai_docs/ y patrones de base de código existentes
- **Blueprint de Implementación**: Tareas TypeScript paso a paso siguiendo patrones de Cloudflare Workers
- **Bucle de Validación**: Pruebas integrales específicas de MCP desde compilación hasta despliegue en producción
- **Consideraciones de Seguridad**: Flujos GitHub OAuth, patrones de acceso a base de datos y protección contra inyección SQL

### Características Clave

- **Rico en Contexto**: Incluye todos los patrones y referencias usando rutas relativas de esta base de código probada
- **Dirigido por Validación**: Validación multinivel desde sintaxis hasta despliegue en producción
- **Seguridad Primero**: Patrones integrados de autenticación y autorización
- **Listo para Producción**: Despliegue y monitoreo en Cloudflare Workers

### Áreas de Investigación

1. **Patrones del Protocolo MCP**
   - Registro y validación de herramientas
   - Servicio de recursos y caché
   - Manejo de errores y logging
   - Patrones de comunicación con clientes

2. **Integración de Autenticación**
   - Implementación GitHub OAuth
   - Sistemas de permisos de usuario
   - Gestión y validación de tokens
   - Patrones de manejo de sesiones

## Salida

Crea un archivo PRP integral en el directorio PRPs/ con:

- Todo el contexto necesario y patrones de código
- Tareas de implementación paso a paso
- Bucles de validación para desarrollo de servidores MCP

## Validación

El comando asegura:

- Todos los patrones de código referenciados existen en la base de código
- Los enlaces de documentación son válidos y accesibles
- Las tareas de implementación son específicas y ejecutables
- Los bucles de validación son integrales y ejecutables por claude code (IMPORTANTE)

## Integración con Patrones Existentes

- Usa plantilla MCP especializada de `PRPs/templates/prp_mcp_base.md`
- Sigue la estructura de directorios establecida y convenciones de nomenclatura
- Se integra con patrones de validación y herramientas existentes
- Aprovecha patrones probados de la implementación actual del servidor MCP en `src/`