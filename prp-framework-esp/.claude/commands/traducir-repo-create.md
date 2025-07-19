---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task, WebSearch]
description: "Genera PRPs especializados para traducción completa de repositorios usando metodología Context Engineering"
---

# /traducir-repo-create - Generador de PRPs de Traducción de Repositorio

## Purpose
Generar Product Requirement Prompts (PRPs) especializados para la traducción sistemática y de alta calidad de repositorios completos al español, aplicando ingeniería de contexto y metodologías probadas.

## Usage
```
/traducir-repo-create [nombre-repositorio] [--prioridad alta|media|baja] [--persona-scribe] [--think-hard]
```

## Arguments
- `nombre-repositorio` - Nombre del repositorio a traducir (context-engineering-intro, prps-agentic-eng, superclaude-framework)
- `--prioridad` - Nivel de prioridad para determinar profundidad de análisis
- `--persona-scribe` - Activar persona experta en documentación y localización
- `--think-hard` - Análisis profundo para traducciones complejas
- `--uc` - Modo UltraCompressed para optimización de tokens

## Execution Process

### 1. **Análisis del Repositorio**
```yaml
LEER informes ejecutivos:
  - informes-ejecutivos/[nombre-repositorio].md
  - informes-ejecutivos/00-resumen-ejecutivo-completo.md
  
OBTENER contexto de configuración:
  - configuracion/glosario-maestro.json
  - configuracion/reglas-traduccion.yaml
  - configuracion/mapeo-archivos.json
  
ANALIZAR estructura original:
  - Escanear directorio del repositorio original
  - Identificar archivos críticos según mapeo
  - Evaluar dependencias entre documentos
```

### 2. **Research y Context Engineering**
```yaml
ANÁLISIS DE COMPLEJIDAD:
  - Tiempo estimado de traducción (del informe ejecutivo)
  - Nivel de dificultad técnica
  - Dependencias críticas
  - Terminología especializada requerida

CONTEXTO TÉCNICO:
  - Patrones de traducción específicos del tipo de documentación
  - Casos de uso y ejemplos relevantes
  - Gotchas y consideraciones especiales del repositorio
  
AUDIENCIA OBJETIVO:
  - Desarrolladores hispanohablantes
  - Nivel técnico según informe ejecutivo
  - Adaptaciones culturales necesarias
```

### 3. **Generación del PRP**
Usando como base `Context-Engineering-Intro/PRPs/templates/prp_base.md`, crear PRP especializado que incluya:

#### Critical Context to Include
```yaml
DOCUMENTACIÓN DE REFERENCIA:
  - url: "informes-ejecutivos/[repositorio].md"
    why: "Análisis completo del contenido y valor educativo"
  
  - file: "configuracion/glosario-maestro.json"
    why: "Terminología técnica a preservar vs traducir"
    
  - file: "configuracion/reglas-traduccion.yaml"
    why: "Estándares de calidad y patrones de traducción"
    
  - file: "configuracion/mapeo-archivos.json"
    why: "Prioridades, dependencias y estimaciones de tiempo"

PATRONES DE TRADUCCIÓN:
  - Preservar código inline y bloques de código
  - Mantener enlaces y referencias técnicas
  - Adaptar ejemplos a contexto hispanohablante cuando sea apropiado
  - Seguir convenciones de naming establecidas

CONTEXTO DEL REPOSITORIO:
  - Propósito educativo y audiencia objetivo
  - Conceptos clave que requieren explicación cultural
  - Flujo de aprendizaje recomendado
  - Casos de uso específicos para desarrolladores hispanohablantes
```

#### Implementation Blueprint
```yaml
FASE 1 - PREPARACIÓN:
  - Crear estructura de directorios en repositorios/[repo]-esp/
  - Configurar herramientas de validación
  - Preparar glosario específico del repositorio

FASE 2 - TRADUCCIÓN POR PRIORIDAD:
  - Traducir archivos de alta prioridad primero
  - Aplicar validación terminológica en cada archivo
  - Mantener estructura y formato original
  - Preservar metadatos y frontmatter

FASE 3 - VALIDACIÓN Y CALIDAD:
  - Ejecutar validador-terminologia.py
  - Verificar consistencia de enlaces
  - Validar estructura Markdown
  - Review técnico de conceptos especializados

FASE 4 - INTEGRACIÓN:
  - Actualizar metadatos del sistema
  - Generar métricas de progreso
  - Documentar adaptaciones realizadas
```

#### Validation Loops (Ejecutables)
```bash
# Nivel 1: Validación Terminológica
python3 herramientas/validador-terminologia.py --directorio repositorios/[repo]-esp/ --glosario configuracion/glosario-maestro.json

# Nivel 2: Verificación de Estructura
find repositorios/[repo]-esp/ -name "*.md" -exec markdown-link-check {} \;

# Nivel 3: Consistencia de Formato
remark repositorios/[repo]-esp/ --use remark-lint --use remark-preset-lint-recommended

# Nivel 4: Métricas de Calidad
python3 herramientas/sincronizador-versiones.py --status

# Nivel 5: Review de Completitud
diff -r --brief [repo-original]/ repositorios/[repo]-esp/ --exclude="*.md" | wc -l
# Resultado esperado: Solo archivos .md deberían diferir
```

### 4. **Template PRP Específico**

```markdown
# PRP: Traducción Completa de [Repositorio]

## Goal
Traducir completamente el repositorio [nombre] al español de España, manteniendo la calidad técnica, estructura educativa y valor para desarrolladores hispanohablantes, siguiendo metodología de Context Engineering.

## Why
- **Impacto educativo**: [Extraer del informe ejecutivo]
- **Audiencia objetivo**: [Definir según análisis]
- **ROI estratégico**: [Tiempo vs beneficio proyectado]

## What
Traducción completa que preserve:
- ✅ Exactitud técnica de conceptos
- ✅ Estructura de aprendizaje progresivo  
- ✅ Funcionalidad de enlaces y referencias
- ✅ Valor educativo para desarrolladores
- ✅ Adaptación cultural apropiada

### Success Criteria
- [ ] [X] archivos críticos traducidos según mapeo
- [ ] >95% consistencia terminológica automática
- [ ] 100% enlaces funcionales preservados
- [ ] Validación técnica por desarrollador hispanohablante
- [ ] Tiempo de traducción dentro de estimación ([X] horas)

## All Needed Context

### Documentación de Referencia
[Incluir contexto específico del repositorio]

### Estructura Original vs Traducida
[Mapping detallado de archivos]

### Terminología Especializada
[Glosario específico del repositorio con ejemplos]

### Gotchas y Consideraciones Especiales
[Aspectos técnicos críticos del repositorio específico]

## Implementation Blueprint
[Plan detallado fase por fase]

## Validation Loop
[Comandos ejecutables específicos]

## Final Checklist
- [ ] Todos los archivos críticos traducidos
- [ ] Validación terminológica exitosa
- [ ] Estructura preservada
- [ ] Enlaces funcionales
- [ ] Review técnico completado
- [ ] Métricas de calidad generadas
- [ ] Documentación de adaptaciones
```

### 5. **Quality Scoring**
Evaluar el PRP generado en escala 1-10 basado en:
- Completitud del contexto (25%)
- Validación ejecutable (25%) 
- Claridad de implementación (25%)
- Adaptación al repositorio específico (25%)

### 6. **Output**
Guardar como: `PRPs/traduccion-[repositorio]-completa.md`

## Personas Auto-activation
- **scribe**: Experto en documentación técnica y localización (PRINCIPAL)
- **architect**: Para decisiones de estructura y organización
- **qa**: Para criterios de validación y calidad
- **mentor**: Para adaptación educativa al contexto hispanohablante

## Integration with Existing Tools
- Utiliza glosario maestro existente para consistencia
- Integra con validador-terminologia.py para automatización
- Respeta estructura de metadatos establecida
- Aprovecha métricas baseline ya generadas

## Examples
```bash
# Crear PRP para Context Engineering (repositorio base)
/traducir-repo-create context-engineering-intro --prioridad alta --persona-scribe

# Crear PRP para repositorio avanzado  
/traducir-repo-create superclaude-framework --prioridad alta --think-hard

# Crear PRP optimizado para tokens
/traducir-repo-create prps-agentic-eng --uc --persona-scribe
```

## Anti-Patterns to Avoid
- ❌ No generar PRP genérico - debe ser específico del repositorio
- ❌ No ignorar informe ejecutivo - es contexto crítico
- ❌ No obviar validaciones - son esenciales para calidad
- ❌ No traducir sin glosario - terminología debe ser consistente
- ❌ No saltarse análisis de dependencias - afecta orden de traducción