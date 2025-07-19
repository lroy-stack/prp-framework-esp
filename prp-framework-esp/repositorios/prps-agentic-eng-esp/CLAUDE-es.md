# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) cuando trabaja con código en este repositorio.

## Naturaleza del Proyecto

Este es un repositorio de **Framework PRP (Product Requirement Prompt)**, no un proyecto de software tradicional. El concepto central: **"PRP = PRD + inteligencia curada de la base de código + agente/runbook"** - diseñado para permitir que agentes de IA entreguen código listo para producción en el primer intento.

## Arquitectura Core

### Sistema Dirigido por Comandos

- **28+ comandos preconfigurados de Claude Code** en `.claude/commands/`
- Comandos organizados por función:
  - `PRPs/` - Flujos de trabajo de creación y ejecución de PRP
  - `development/` - Utilidades core de desarrollo (prime-core, onboarding, debug)
  - `code-quality/` - Comandos de revisión y refactorización
  - `rapid-development/experimental/` - Creación paralela de PRP y herramientas de hackathon
  - `git-operations/` - Resolución de conflictos y operaciones inteligentes de git

### Metodología Basada en Templates

- **Templates PRP** en `PRPs/templates/` siguen formato estructurado con bucles de validación
- **Enfoque Rico en Contexto**: Cada PRP debe incluir documentación comprensiva, ejemplos y problemas conocidos
- **Diseño Validation-First**: Cada PRP contiene puertas de validación ejecutables (sintaxis, pruebas, integración)

### Curación de Documentación IA

- `PRPs/ai_docs/` contiene documentación curada de Claude Code para inyección de contexto
- `claude_md_files/` proporciona ejemplos específicos de CLAUDE.md por framework

## Comandos de Desarrollo

### Ejecución PRP

```bash
# Modo interactivo (recomendado para desarrollo)
uv run PRPs/scripts/prp_runner.py --prp [prp-name] --interactive

# Modo headless (para CI/CD)
uv run PRPs/scripts/prp_runner.py --prp [prp-name] --output-format json

# JSON streaming (para monitoreo en tiempo real)
uv run PRPs/scripts/prp_runner.py --prp [prp-name] --output-format stream-json
```

### Comandos Clave de Claude

- `/prp-base-create` - Generar PRPs comprensivos con investigación
- `/prp-base-execute` - Ejecutar PRPs contra la base de código
- `/prp-planning-create` - Crear documentos de planificación con diagramas
- `/prime-core` - Preparar Claude con contexto del proyecto
- `/review-staged-unstaged` - Revisar cambios de git usando metodología PRP

## Patrones Críticos de Éxito

### La Metodología PRP

1. **El Contexto es Rey**: Incluye TODA la documentación necesaria, ejemplos y advertencias
2. **Bucles de Validación**: Proporciona pruebas/lints ejecutables que la IA puede ejecutar y corregir
3. **Denso en Información**: Usa palabras clave y patrones de la base de código
4. **Éxito Progresivo**: Comienza simple, valida, luego mejora

### Requisitos de Estructura PRP

- **Objetivo**: Estado final específico y deseos
- **Por qué**: Valor de negocio e impacto del usuario
- **Qué**: Comportamiento visible del usuario y requisitos técnicos
- **Todo el Contexto Necesario**: URLs de documentación, ejemplos de código, problemas conocidos, patrones
- **Blueprint de Implementación**: Pseudocódigo con detalles críticos y listas de tareas
- **Bucle de Validación**: Comandos ejecutables para sintaxis, pruebas, integración

### Puertas de Validación (Deben ser Ejecutables)

```bash
# Nivel 1: Sintaxis y Estilo
ruff check --fix && mypy .

# Nivel 2: Pruebas Unitarias
uv run pytest tests/ -v

# Nivel 3: Integración
uv run uvicorn main:app --reload
curl -X POST http://localhost:8000/endpoint -H "Content-Type: application/json" -d '{...}'

# Nivel 4: Despliegue
# servidores mcp, u otras formas creativas de auto-validación
```

## Anti-Patrones a Evitar

- L No crear prompts de contexto mínimo - el contexto es todo - el PRP debe ser comprensivo y auto-contenido, referenciar documentación y ejemplos relevantes.
- L No omitir pasos de validación - son críticos para el éxito en un intento - Mientras mejor sea la IA ejecutando el bucle de validación, más probable es que tenga éxito.
- L No ignorar el formato estructurado PRP - está probado en batalla
- L No crear nuevos patrones cuando los templates existentes funcionan
- L No hardcodear valores que deberían ser configuración
- L No capturar todas las excepciones - sé específico

## Trabajando con Este Framework

### Al Crear nuevos PRPs

1. **Proceso de Contexto**: Los nuevos PRPs deben consistir en secciones de contexto, ¡El Contexto es Rey!
2.

### Al Ejecutar PRPs

1. **Cargar PRP**: Leer y entender todo el contexto y requisitos
2. **ULTRATHINK**: Crear plan comprensivo, dividir en todos, usar subagentes, batch tool etc revisar prps/ai_docs/
3. **Ejecutar**: Implementar siguiendo el blueprint
4. **Validar**: Ejecutar cada comando de validación, corregir fallas
5. **Completar**: Asegurar que todos los ítems de checklist estén hechos

### Uso de Comandos

- Leer el directorio .claude/commands
- Acceder vía prefijo `/` en Claude Code
- Los comandos se auto-documentan con marcadores de posición de argumentos
- Usar comandos de creación paralela para desarrollo rápido
- Aprovechar comandos existentes de revisión y refactorización

## Comprensión de la Estructura del Proyecto

```
PRPs-agentic-eng/
.claude/
  commands/           # 28+ comandos de Claude Code
  settings.local.json # Permisos de herramientas
PRPs/
  templates/          # Templates PRP con validación
  scripts/           # Runner PRP y utilidades
  ai_docs/           # Documentación curada de Claude Code
   *.md               # PRPs activos y de ejemplo
 claude_md_files/        # Ejemplos específicos de CLAUDE.md por framework
 pyproject.toml         # Configuración de paquete Python
```

Recuerda: Este framework es sobre **éxito de implementación en un intento a través de contexto comprensivo y validación**. Cada PRP debería contener el contexto exacto para que un agente de IA implemente exitosamente código funcionando en un solo intento.