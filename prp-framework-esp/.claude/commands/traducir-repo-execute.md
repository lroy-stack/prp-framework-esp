---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
description: "Ejecuta traducción sistemática de repositorios siguiendo PRPs con validación continua y metodología Context Engineering"
---

# /traducir-repo-execute - Ejecutor de Traducción de Repositorio

## Purpose
Ejecutar la traducción sistemática de repositorios completos siguiendo los PRPs generados, aplicando validación continua, control de calidad y metodología de Context Engineering para garantizar traducciones de nivel profesional.

## Usage
```
/traducir-repo-execute [archivo-prp] [--modo interactivo|batch] [--validar-continuo] [--persona-scribe]
```

## Arguments
- `archivo-prp` - Ruta al PRP de traducción de repositorio (ej: PRPs/traduccion-context-engineering-intro-completa.md)
- `--modo` - Modo de ejecución: interactivo (pausa para review) o batch (automático)
- `--validar-continuo` - Ejecutar validaciones después de cada archivo traducido
- `--persona-scribe` - Activar persona experta en documentación técnica
- `--think-hard` - Análisis profundo para secciones complejas
- `--uc` - Modo UltraCompressed para optimización

## Execution Process

### 1. **Carga y Análisis del PRP**
```yaml
CARGAR PRP:
  - Leer archivo PRP especificado
  - Extraer configuración del repositorio objetivo
  - Identificar archivos críticos y dependencias
  - Cargar contexto específico del repositorio

VALIDAR PREREQUISITOS:
  - Verificar existencia del repositorio original
  - Confirmar acceso a herramientas de validación
  - Validar configuración de glosario y reglas
  - Comprobar estructura de directorios de destino
```

### 2. **ULTRATHINK - Planificación Estratégica**
```yaml
ANÁLISIS DEL ALCANCE:
  - Revisar completamente el PRP y sus requisitos
  - Identificar archivos por orden de prioridad/dependencia
  - Planificar flujo de trabajo optimizado
  - Estimar checkpoints de validación

ESTRATEGIA DE IMPLEMENTACIÓN:
  - Crear plan fase por fase usando TodoWrite
  - Identificar puntos de validación críticos
  - Establecer criterios de calidad específicos
  - Planificar manejo de errores y rollback si es necesario
```

### 3. **Preparación del Entorno**
```bash
# Crear estructura de directorios
mkdir -p repositorios/[repo]-esp/{contenido,meta,temporal}

# Verificar herramientas
python3 herramientas/validador-terminologia.py --help
python3 herramientas/sincronizador-versiones.py --help

# Cargar configuración
cat configuracion/glosario-maestro.json | jq '.terminos_core | length'
cat configuracion/reglas-traduccion.yaml | grep -E "idioma_destino|dialecto"
```

### 4. **Ejecución Fase por Fase**

#### Fase 1: Archivos Críticos de Alta Prioridad
```yaml
PROCESO POR ARCHIVO:
  1. LEER archivo original completo
  2. ANALIZAR contexto y terminología especializada
  3. APLICAR reglas de traducción específicas
  4. TRADUCIR manteniendo estructura exacta
  5. VALIDAR terminología con glosario maestro
  6. PRESERVAR código, enlaces y metadatos
  7. REVISAR calidad técnica y cultural
  8. GUARDAR en estructura de destino

VALIDACIÓN INMEDIATA:
  - Ejecutar validador-terminologia.py en archivo
  - Verificar preservación de estructura Markdown
  - Comprobar enlaces y referencias
  - Validar metadata y frontmatter
```

#### Fase 2: Archivos de Prioridad Media
```yaml
CONTINUAR con archivos según orden de dependencias:
  - Aplicar lecciones aprendidas de archivos anteriores
  - Mantener consistencia terminológica establecida
  - Validar referencias cruzadas con archivos ya traducidos
  - Documentar decisiones de traducción específicas
```

#### Fase 3: Archivos de Completitud
```yaml
FINALIZAR traducción completa:
  - Traducir archivos restantes (README secundarios, etc.)
  - Verificar consistencia global del repositorio
  - Actualizar índices y tablas de contenido
  - Generar documentación de cambios realizados
```

### 5. **Validación Continua (Ejecutable)**

#### Nivel 1: Validación Terminológica
```bash
# Después de cada archivo crítico
python3 herramientas/validador-terminologia.py \
  --archivo repositorios/[repo]-esp/[archivo-traducido] \
  --glosario configuracion/glosario-maestro.json \
  --reporte temporal/validacion-[archivo].json

# Verificar resultado
if [ $? -eq 0 ]; then
  echo "✅ Terminología validada: [archivo]"
else
  echo "❌ Errores de terminología encontrados - revisar"
  exit 1
fi
```

#### Nivel 2: Validación de Estructura
```bash
# Verificar preservación de estructura Markdown
original_headers=$(grep -c "^#" [repo-original]/[archivo])
translated_headers=$(grep -c "^#" repositorios/[repo]-esp/[archivo])

if [ "$original_headers" -eq "$translated_headers" ]; then
  echo "✅ Estructura preservada: [archivo]"
else
  echo "⚠️ Posible cambio de estructura - revisar"
fi
```

#### Nivel 3: Validación de Enlaces
```bash
# Verificar enlaces internos funcionales
markdown-link-check repositorios/[repo]-esp/[archivo] \
  --config temporal/link-check-config.json

# Para enlaces relativos dentro del repositorio
find repositorios/[repo]-esp/ -name "*.md" -exec grep -l "\[.*\](\..*\.md)" {} \; | \
  xargs -I {} bash -c 'echo "Validando enlaces en: {}"; markdown-link-check "{}"'
```

#### Nivel 4: Validación de Calidad Cultural
```yaml
CRITERIOS DE REVIEW:
  - Terminología técnica apropiada para España/Latinoamérica
  - Ejemplos culturalmente relevantes cuando sea aplicable
  - Consistencia en uso de "tú" vs "usted" según audiencia
  - Preservación de conceptos técnicos en inglés cuando sea apropiado
  - Fluidez natural sin calco del inglés
```

### 6. **Gestión de Errores y Rollback**
```bash
# Backup antes de cambios críticos
cp -r repositorios/[repo]-esp/ temporal/backup-$(date +%Y%m%d-%H%M%S)/

# En caso de error crítico
if [ "$VALIDATION_FAILED" = "true" ]; then
  echo "❌ Validación fallida - ejecutando rollback"
  rm -rf repositorios/[repo]-esp/
  cp -r temporal/backup-latest/ repositorios/[repo]-esp/
  echo "🔄 Rollback completado - revisar errores en temporal/errores.log"
fi
```

### 7. **Finalización e Integración**

#### Actualización de Metadatos
```python
# Actualizar estado-general.json
import json
from datetime import datetime

with open('metadatos/estado-general.json', 'r+') as f:
    estado = json.load(f)
    estado['frameworks']['[repo]']['estado_traduccion'] = 'completado'
    estado['frameworks']['[repo]']['fecha_completado'] = datetime.now().isoformat()
    estado['estadisticas_globales']['repositorios_completados'] += 1
    f.seek(0)
    json.dump(estado, f, indent=2, ensure_ascii=False)
    f.truncate()
```

#### Generación de Métricas Finales
```bash
# Métricas de completitud
total_archivos=$(find [repo-original]/ -name "*.md" | wc -l)
archivos_traducidos=$(find repositorios/[repo]-esp/ -name "*.md" | wc -l)
porcentaje_completitud=$((archivos_traducidos * 100 / total_archivos))

echo "📊 Completitud: $porcentaje_completitud% ($archivos_traducidos/$total_archivos archivos)"

# Métricas de calidad terminológica
python3 herramientas/validador-terminologia.py \
  --directorio repositorios/[repo]-esp/ \
  --estadisticas \
  --glosario configuracion/glosario-maestro.json \
  > reportes/calidad-[repo]-$(date +%Y%m%d).md
```

### 8. **Reporte de Completación**
```markdown
# 📋 Reporte de Traducción Completada: [Repositorio]

## Resumen
- **Repositorio**: [nombre]
- **Fecha completado**: [fecha]
- **Tiempo total**: [horas]
- **Archivos traducidos**: [cantidad]
- **Calidad terminológica**: [porcentaje]%

## Archivos Principales Traducidos
- [ ] README.md → README-es.md
- [ ] CLAUDE.md → CLAUDE-es.md
- [ ] [otros archivos críticos...]

## Adaptaciones Realizadas
- [Lista de decisiones de traducción específicas]
- [Ejemplos adaptados al contexto hispanohablante]
- [Terminología especializada mantenida vs traducida]

## Validaciones Pasadas
- ✅ Terminología consistente (>95%)
- ✅ Estructura preservada (100%)
- ✅ Enlaces funcionales (100%)
- ✅ Review técnico completado

## Próximos Pasos
- [ ] Review por desarrollador hispanohablante nativo
- [ ] Promoción en comunidades tech
- [ ] Documentación de casos de uso específicos
```

## Personas Auto-activation
- **scribe**: PRINCIPAL - Experto en documentación técnica y localización
- **qa**: Para validación continua y criterios de calidad
- **architect**: Para decisiones de estructura cuando sea necesario
- **mentor**: Para adaptación educativa y cultural

## Error Recovery Patterns
```yaml
ERRORES COMUNES Y SOLUCIONES:
  terminologia_inconsistente:
    - Revisar glosario maestro
    - Verificar reglas de traducción
    - Aplicar corrección automática cuando sea posible
    
  estructura_markdown_rota:
    - Comparar con original
    - Revisar preservación de headers y formato
    - Reconstruir si es necesario
    
  enlaces_rotos:
    - Verificar paths relativos
    - Actualizar referencias internas
    - Mantener enlaces externos intactos
    
  validacion_fallida:
    - Analizar logs de error específicos
    - Aplicar correcciones incrementales
    - Re-ejecutar validaciones hasta éxito
```

## Quality Checklist Final
- [ ] PRP completamente ejecutado según especificaciones
- [ ] Todos los archivos críticos traducidos
- [ ] Validaciones automáticas exitosas (4 niveles)
- [ ] Consistencia terminológica >95%
- [ ] Estructura y formato preservados
- [ ] Enlaces y referencias funcionales
- [ ] Adaptaciones culturales apropiadas
- [ ] Metadatos del sistema actualizados
- [ ] Reporte de completación generado
- [ ] Ready para review humano final

## Examples
```bash
# Ejecutar traducción básica
/traducir-repo-execute PRPs/traduccion-context-engineering-intro-completa.md

# Ejecutar con validación continua
/traducir-repo-execute PRPs/traduccion-superclaude-framework-completa.md --validar-continuo

# Modo interactivo para review manual
/traducir-repo-execute PRPs/traduccion-prps-agentic-eng-completa.md --modo interactivo --persona-scribe
```