---
name: "prp-mcp-execute"
description: Este comando está diseñado para crear servidores integrales del Protocolo de Contexto de Modelo (MCP) siguiendo el Prompt de Requisitos de Producto (PRP) específico pasado como argumento, referenciando los patrones de esta base de código que refleja las configuraciones de herramientas para los requisitos específicos del usuario.
Usage: /prp-mcp-execute ruta/al/prp.md
---

# Ejecutar PRP de Servidor MCP

Ejecutar un Prompt de Requisitos de Producto (PRP) integral para construir servidores del Protocolo de Contexto de Modelo (MCP) con autenticación, integración de base de datos y despliegue en Cloudflare Workers.

PRP a ejecutar: $ARGUMENTS

## Propósito

Ejecutar PRPs de servidores MCP con validación integral, pruebas y verificación de despliegue siguiendo los patrones probados de esta base de código.

## Proceso de Ejecución

1. **Cargar y Analizar PRP**
   - Leer el archivo PRP especificado completamente
   - Entender todo el contexto, requisitos y criterios de validación
   - Crear lista de tareas integral usando la herramienta TodoWrite
   - Identificar todas las dependencias y puntos de integración

2. **Recopilación de Contexto e Investigación**
   - Usar agentes Task para investigar patrones de servidores MCP existentes
   - Estudiar flujos de autenticación y patrones de integración de base de datos
   - Investigar despliegue en Cloudflare Workers y configuración de entorno
   - Recopilar toda la documentación necesaria y ejemplos de código

3. **Fase de Implementación**
   - Ejecutar todas las tareas de implementación en el orden correcto
   - Seguir patrones TypeScript de la base de código existente
   - Implementar herramientas MCP, recursos y flujos de autenticación
   - Agregar manejo integral de errores y logging

## Notas

- Usa la herramienta TodoWrite para gestión integral de tareas
- Sigue todos los patrones de la implementación probada de la base de código
- Incluye manejo integral de errores y recuperación
- Optimizado para los bucles de validación de Claude Code
- Listo para producción con monitoreo y logging
- Compatible con MCP Inspector y Claude Desktop