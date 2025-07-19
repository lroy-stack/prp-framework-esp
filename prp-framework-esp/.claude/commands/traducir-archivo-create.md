---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
description: "Genera PRPs especializados para traducción granular de archivos específicos con control de calidad técnica"
---

# /traducir-archivo-create - Generador de PRPs de Traducción de Archivo Individual

## Purpose
Generar Product Requirement Prompts (PRPs) especializados para la traducción granular de archivos específicos, permitiendo control de calidad detallado y manejo de casos especiales que requieren atención especializada.

## Usage
```
/traducir-archivo-create [ruta-archivo] [--repositorio repo] [--prioridad alta|media|baja] [--tipo readme|claude|template|ejemplo]
```

## Arguments
- `ruta-archivo` - Ruta relativa del archivo en el repositorio original (ej: README.md, PRPs/templates/prp_base.md)
- `--repositorio` - Repositorio origen (context-engineering-intro, prps-agentic-eng, superclaude-framework)
- `--prioridad` - Nivel de prioridad según mapeo de archivos
- `--tipo` - Tipo de contenido para aplicar estrategias específicas
- `--persona-scribe` - Activar experto en documentación técnica
- `--think-hard` - Análisis profundo para archivos complejos

## Execution Process

### 1. **Análisis del Archivo Específico**
```yaml
IDENTIFICAR ARCHIVO:
  - Leer archivo original completo
  - Extraer metadatos del mapeo-archivos.json
  - Identificar dependencias específicas
  - Evaluar complejidad y terminología especializada

CONTEXTO DEL REPOSITORIO:
  - Cargar informe ejecutivo del repositorio
  - Identificar posición en flujo de aprendizaje
  - Analizar relación con otros archivos del repo
  - Determinar audiencia objetivo específica
```

### 2. **Research Específico del Archivo**
```yaml
ANÁLISIS DE CONTENIDO:
  - Tipo de documentación (tutorial, referencia, template, ejemplo)
  - Conceptos técnicos clave presentes
  - Ejemplos de código y su preservación
  - Enlaces internos y externos críticos
  - Estructura de headers y navegación

TERMINOLOGÍA ESPECIALIZADA:
  - Extraer términos técnicos específicos
  - Verificar contra glosario maestro
  - Identificar nuevos términos para el glosario
  - Determinar estrategia de traducción por término

DEPENDENCIAS Y REFERENCIAS:
  - Archivos que referencian este archivo
  - Archivos referenciados por este archivo
  - Orden de traducción recomendado
  - Validaciones de consistencia necesarias
```

### 3. **Generación del PRP Granular**

#### Template Específico por Tipo de Archivo

##### Para README.md (Documentación Principal)
```markdown
# PRP: Traducción de README.md - [Repositorio]

## Goal
Traducir el archivo README.md principal del repositorio [repo], manteniendo su función como punto de entrada educativo y preservando toda la funcionalidad de navegación y enlaces.

## Why
- **Primer contacto**: Es el archivo más visible del repositorio
- **Impacto inmediato**: Determina si usuarios hispanohablantes pueden aprovechar el repositorio
- **SEO y discoverabilidad**: Mejora visibilidad en búsquedas en español
- **Accesibilidad**: Elimina barrera de idioma para desarrolladores

## What
Traducción completa que preserve:
- ✅ Estructura de navegación y tabla de contenidos
- ✅ Enlaces a archivos internos (actualizando rutas si es necesario)
- ✅ Badges y shields informativos
- ✅ Ejemplos de código con comentarios contextuales
- ✅ Calls-to-action y next steps
- ✅ Metadata y frontmatter técnico

### Success Criteria Específicos
- [ ] Tabla de contenidos funcional en español
- [ ] Enlaces internos apuntan a archivos traducidos
- [ ] Ejemplos de código contextualizados para hispanohablantes
- [ ] Badges actualizados (ej: documentación → documentación-es)
- [ ] Call-to-action adaptado culturalmente
- [ ] Terminología técnica consistente con glosario
```

##### Para CLAUDE.md (Configuración Técnica)
```markdown
# PRP: Traducción de CLAUDE.md - [Repositorio]

## Goal
Traducir archivo de configuración CLAUDE.md preservando toda la funcionalidad técnica mientras se hace accesible a desarrolladores hispanohablantes.

## What
Traducción especializada que preserve:
- ✅ Comandos y sintaxis técnica exacta
- ✅ Nombres de herramientas y tecnologías
- ✅ Paths y rutas de archivos
- ✅ Configuraciones y parámetros técnicos
- ✅ Comentarios y explicaciones contextuales
- ✅ Referencias a archivos del proyecto

### Consideraciones Técnicas Críticas
- **NO traducir**: Nombres de comandos, tools, APIs
- **SÍ traducir**: Comentarios explicativos, descripciones de propósito
- **PRESERVAR**: Estructura de secciones, formato de configuración
- **ADAPTAR**: Ejemplos cuando sea culturalmente relevante
```

##### Para Templates (PRPs/templates/)
```markdown
# PRP: Traducción de Template - [Archivo Template]

## Goal
Traducir template manteniendo su funcionalidad como guía estructurada para desarrolladores hispanohablantes.

## What
Traducción que preserve estructura while making accessible:
- ✅ Placeholders y variables de template
- ✅ Estructura de secciones y formato
- ✅ Ejemplos de código embebidos
- ✅ Comentarios explicativos y guías
- ✅ Referencias a otros archivos del framework
```

### 4. **Context Engineering Específico**
```yaml
DOCUMENTACIÓN CRÍTICA:
  - file: "configuracion/mapeo-archivos.json"
    section: "frameworks.[repo].archivos_criticos.[archivo]"
    why: "Metadatos específicos: prioridad, complejidad, dependencias, tiempo estimado"
    
  - file: "configuracion/glosario-maestro.json"
    why: "Terminología específica a aplicar en este archivo"
    
  - file: "configuracion/reglas-traduccion.yaml"
    section: "patrones_traduccion"
    why: "Reglas específicas para código inline, enlaces, comandos"

ARCHIVO ORIGINAL:
  - file: "[repo-original]/[ruta-archivo]"
    why: "Contenido completo a traducir con estructura exacta"
    critical: "Preservar formato Markdown, código, metadatos"

CONTEXTO DEL REPOSITORIO:
  - file: "informes-ejecutivos/[repo].md"
    section: "Dependencias de Aprendizaje"
    why: "Entender posición del archivo en flujo educativo"

ARCHIVOS RELACIONADOS (si existen):
  - file: "[archivos-que-referencian-este]"
    why: "Mantener consistencia en referencias cruzadas"
```

### 5. **Implementation Blueprint Granular**
```yaml
ANÁLISIS PREVIO:
  - Escanear archivo completo buscando patrones específicos
  - Identificar bloques de código vs texto descriptivo
  - Mapear enlaces internos y externos
  - Extraer terminología técnica especializada

TRADUCCIÓN SECCIÓN POR SECCIÓN:
  - Header y metadata: Adaptar manteniendo funcionalidad
  - Tabla de contenidos: Traducir y verificar enlaces
  - Introducción: Traducir adaptando contexto cultural
  - Secciones técnicas: Preservar exactitud, traducir explicaciones
  - Ejemplos de código: Mantener código, traducir comentarios contextuales
  - Enlaces y referencias: Actualizar a versiones traducidas cuando existan

VALIDACIÓN ESPECÍFICA:
  - Verificar preservación de estructura Markdown
  - Comprobar funcionalidad de enlaces internos
  - Validar terminología contra glosario maestro
  - Revisar fluidez y naturalidad en español
```

### 6. **Validation Loops Específicos**
```bash
# Nivel 1: Validación Terminológica Específica
python3 herramientas/validador-terminologia.py \
  --archivo repositorios/[repo]-esp/[archivo-traducido] \
  --glosario configuracion/glosario-maestro.json \
  --tipo [tipo-archivo] \
  --verbose

# Nivel 2: Validación de Estructura Específica
diff -u [repo-original]/[archivo] repositorios/[repo]-esp/[archivo-traducido] \
  --ignore-matching-lines="^#" | grep -E "^[+-]" | wc -l
# Resultado esperado: Solo cambios de contenido, no estructura

# Nivel 3: Validación de Enlaces (si aplica)
if grep -q "](.*\.md" repositorios/[repo]-esp/[archivo-traducido]; then
  echo "Verificando enlaces internos..."
  markdown-link-check repositorios/[repo]-esp/[archivo-traducido] \
    --config .markdown-link-check.json
fi

# Nivel 4: Validación de Código Embebido
if grep -q "```" repositorios/[repo]-esp/[archivo-traducido]; then
  echo "Verificando preservación de bloques de código..."
  original_code_blocks=$(grep -c "```" [repo-original]/[archivo])
  translated_code_blocks=$(grep -c "```" repositorios/[repo]-esp/[archivo-traducido])
  
  if [ "$original_code_blocks" -eq "$translated_code_blocks" ]; then
    echo "✅ Bloques de código preservados"
  else
    echo "❌ Posible alteración de bloques de código"
    exit 1
  fi
fi
```

### 7. **Quality Checklist Específico**
```yaml
COMPLETITUD:
  - [ ] Todo el contenido traducido (0% contenido en inglés excepto términos técnicos)
  - [ ] Estructura Markdown preservada exactamente
  - [ ] Metadatos y frontmatter intactos
  - [ ] Enlaces actualizados apropiadamente

CALIDAD TÉCNICA:
  - [ ] Terminología consistente con glosario maestro
  - [ ] Código y comandos preservados sin alteración
  - [ ] Referencias técnicas exactas
  - [ ] Paths y rutas funcionales

CALIDAD LINGÜÍSTICA:
  - [ ] Español natural y fluido (no calco del inglés)
  - [ ] Apropiado para audiencia técnica hispanohablante
  - [ ] Consistencia en tratamiento (tú/usted según audiencia)
  - [ ] Adaptaciones culturales cuando sean relevantes

FUNCIONALIDAD:
  - [ ] Enlaces internos apuntan a archivos correctos
  - [ ] Navegación y tabla de contenidos funcional
  - [ ] Ejemplos y casos de uso relevantes para el contexto
  - [ ] Call-to-actions apropiados culturalmente
```

## Output Específico
Guardar como: `PRPs/traduccion-[archivo-sin-extension]-[repo].md`

Ejemplos:
- `PRPs/traduccion-readme-context-engineering-intro.md`
- `PRPs/traduccion-claude-superclaude-framework.md`
- `PRPs/traduccion-prp-base-template-prps-agentic-eng.md`

## Personas Auto-activation por Tipo
```yaml
README.md:
  - scribe: Documentación principal
  - mentor: Adaptación educativa
  
CLAUDE.md:
  - scribe: Documentación técnica
  - architect: Configuración de sistema
  
Templates:
  - scribe: Documentación estructurada
  - architect: Patrones y metodología
  
Ejemplos:
  - scribe: Documentación práctica
  - mentor: Casos de uso educativos
```

## Examples
```bash
# Traducir README principal
/traducir-archivo-create README.md --repositorio context-engineering-intro --tipo readme --prioridad alta

# Traducir configuración compleja
/traducir-archivo-create CLAUDE.md --repositorio superclaude-framework --tipo claude --think-hard

# Traducir template específico
/traducir-archivo-create PRPs/templates/prp_base.md --repositorio prps-agentic-eng --tipo template --persona-scribe
```

## Anti-Patterns to Avoid
- ❌ No traducir código o comandos técnicos
- ❌ No alterar estructura de headers Markdown
- ❌ No cambiar paths o rutas sin verificar destino
- ❌ No ignorar contexto del repositorio específico
- ❌ No saltarse validación de enlaces internos