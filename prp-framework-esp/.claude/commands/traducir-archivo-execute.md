---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
description: "Ejecuta traducción granular de archivos específicos con validación detallada y control de calidad técnica"
---

# /traducir-archivo-execute - Ejecutor de Traducción de Archivo Individual

## Purpose
Ejecutar traducción granular de archivos específicos siguiendo PRPs dedicados, con control de calidad detallado, validación técnica especializada y manejo de casos especiales que requieren atención experta.

## Usage
```
/traducir-archivo-execute [archivo-prp] [--validar-inmediato] [--backup] [--persona-scribe]
```

## Arguments
- `archivo-prp` - Ruta al PRP de traducción de archivo específico (ej: PRPs/traduccion-readme-context-engineering-intro.md)
- `--validar-inmediato` - Ejecutar todas las validaciones inmediatamente después de la traducción
- `--backup` - Crear backup antes de realizar cambios
- `--persona-scribe` - Activar persona experta en documentación técnica
- `--think-hard` - Análisis profundo para secciones complejas
- `--dry-run` - Simular traducción sin escribir archivos (para testing)

## Execution Process

### 1. **Carga y Análisis del PRP**
```yaml
CARGAR PRP ESPECÍFICO:
  - Leer archivo PRP de traducción granular
  - Extraer metadatos del archivo objetivo
  - Identificar tipo de contenido y estrategias específicas
  - Cargar contexto del repositorio y dependencias

VERIFICAR PREREQUISITOS:
  - Confirmar existencia del archivo original
  - Verificar estructura de directorios de destino
  - Validar acceso a herramientas de validación
  - Comprobar configuración de glosario y reglas
```

### 2. **ULTRATHINK - Análisis Específico del Archivo**
```yaml
ANÁLISIS DE CONTENIDO:
  - Leer archivo original completo
  - Identificar secciones y tipos de contenido
  - Mapear código vs texto descriptivo
  - Analizar terminología técnica específica
  - Detectar patrones especiales (enlaces, references, código embebido)

ESTRATEGIA DE TRADUCCIÓN:
  - Determinar orden de sección por sección
  - Identificar dependencias internas
  - Planificar preservación de elementos técnicos
  - Establecer checkpoints de validación
```

### 3. **Backup y Preparación**
```bash
# Crear backup si se especifica
if [ "$BACKUP" = "true" ]; then
  backup_dir="temporal/backups/$(date +%Y%m%d-%H%M%S)"
  mkdir -p "$backup_dir"
  cp "[archivo-original]" "$backup_dir/"
  echo "✅ Backup creado en: $backup_dir"
fi

# Preparar directorio de destino
mkdir -p "$(dirname "repositorios/[repo]-esp/[archivo-destino]")"

# Verificar herramientas
python3 herramientas/validador-terminologia.py --help > /dev/null
echo "✅ Herramientas de validación disponibles"
```

### 4. **Ejecución de Traducción Sección por Sección**

#### Análisis Inicial del Archivo
```yaml
EXTRACCIÓN DE ESTRUCTURA:
  - Headers y jerarquía de secciones
  - Bloques de código y su lenguaje
  - Enlaces internos y externos
  - Metadatos y frontmatter
  - Tablas y listas estructuradas
  - Imágenes y referencias multimedia
```

#### Traducción por Tipos de Contenido

##### Headers y Metadatos
```yaml
PROCESS:
  - Traducir títulos preservando jerarquía (# ## ###)
  - Mantener IDs de sección si existen
  - Adaptar metadatos preservando funcionalidad
  - Actualizar tabla de contenidos si existe

VALIDATION:
  - Verificar que número de headers coincide
  - Comprobar que jerarquía se mantiene
  - Validar IDs únicos si se usan para navegación
```

##### Bloques de Código
```yaml
PROCESS:
  - PRESERVAR código exactamente como está
  - Traducir solo comentarios contextuales
  - Mantener ejemplos de comandos intactos
  - Adaptar nombres de variables solo si son educativos

CRITICAL:
  - NO alterar sintaxis de código
  - NO traducir nombres de funciones/métodos
  - NO cambiar paths o URLs en código
  - Mantener indentación exacta
```

##### Enlaces y Referencias
```yaml
PROCESS:
  - Enlaces externos: Mantener intactos
  - Enlaces internos: Actualizar a versiones traducidas si existen
  - Referencias de archivos: Verificar existencia del destino
  - Anchors: Actualizar si headers han cambiado

VALIDATION:
  - Verificar que todos los enlaces son accesibles
  - Comprobar consistencia de referencias internas
  - Validar anchors apuntan a secciones correctas
```

##### Texto Descriptivo
```yaml
PROCESS:
  - Aplicar reglas de glosario maestro
  - Mantener terminología técnica en inglés cuando corresponda
  - Adaptar ejemplos a contexto hispanohablante cuando sea relevante
  - Preservar exactitud técnica

QUALITY:
  - Español natural sin calcos del inglés
  - Consistencia en tratamiento (tú/usted)
  - Fluidez apropiada para audiencia técnica
  - Adaptación cultural cuando añada valor
```

### 5. **Validación Granular Inmediata**

#### Nivel 1: Validación de Estructura
```bash
# Verificar preservación de estructura Markdown
echo "🔍 Validando estructura..."

# Contar headers
original_h1=$(grep -c "^# " "[archivo-original]")
translated_h1=$(grep -c "^# " "repositorios/[repo]-esp/[archivo]")

original_h2=$(grep -c "^## " "[archivo-original]")
translated_h2=$(grep -c "^## " "repositorios/[repo]-esp/[archivo]")

if [ "$original_h1" -eq "$translated_h1" ] && [ "$original_h2" -eq "$translated_h2" ]; then
  echo "✅ Estructura de headers preservada"
else
  echo "❌ Estructura de headers alterada"
  echo "Original H1: $original_h1, Traducido H1: $translated_h1"
  echo "Original H2: $original_h2, Traducido H2: $translated_h2"
  exit 1
fi

# Verificar bloques de código
original_code=$(grep -c "^```" "[archivo-original]")
translated_code=$(grep -c "^```" "repositorios/[repo]-esp/[archivo]")

if [ "$original_code" -eq "$translated_code" ]; then
  echo "✅ Bloques de código preservados ($original_code bloques)"
else
  echo "❌ Número de bloques de código alterado"
  exit 1
fi
```

#### Nivel 2: Validación Terminológica
```bash
echo "🔍 Validando terminología..."

python3 herramientas/validador-terminologia.py \
  --archivo "repositorios/[repo]-esp/[archivo]" \
  --glosario configuracion/glosario-maestro.json \
  --reporte "temporal/validacion-$(basename [archivo] .md).json" \
  --verbose

if [ $? -eq 0 ]; then
  echo "✅ Terminología validada correctamente"
  # Mostrar estadísticas
  cat "temporal/validacion-$(basename [archivo] .md).json" | \
    jq '.estadisticas | "Términos validados: \(.terminos_encontrados), Errores: \(.errores_encontrados)"'
else
  echo "❌ Errores de terminología encontrados"
  echo "Revisar: temporal/validacion-$(basename [archivo] .md).json"
  exit 1
fi
```

#### Nivel 3: Validación de Enlaces
```bash
echo "🔍 Validando enlaces..."

# Solo si el archivo contiene enlaces
if grep -q "](.*)" "repositorios/[repo]-esp/[archivo]"; then
  # Crear configuración específica para enlaces internos
  cat > temporal/link-check-config.json << EOF
{
  "ignorePatterns": [
    {
      "pattern": "^https://github.com/"
    }
  ],
  "aliveStatusCodes": [200, 206, 999],
  "timeout": "10s"
}
EOF

  # Validar enlaces
  markdown-link-check "repositorios/[repo]-esp/[archivo]" \
    --config temporal/link-check-config.json \
    --quiet || {
    echo "⚠️ Algunos enlaces pueden estar rotos - revisar manualmente"
    echo "Esto es común durante traducción antes de que todos los archivos estén listos"
  }
  
  echo "✅ Validación de enlaces completada"
fi
```

#### Nivel 4: Validación de Calidad Técnica
```bash
echo "🔍 Validando calidad técnica..."

# Verificar que no hay texto mezclado (inglés-español)
mixed_content=$(grep -E "[a-zA-Z]{3,}.*[ñáéíóúü]|[ñáéíóúü].*[a-zA-Z]{3,}" \
  "repositorios/[repo]-esp/[archivo]" | \
  grep -v -E "(code|http|github|npm|git|API|JSON|YAML|URL)" | wc -l)

if [ "$mixed_content" -gt 5 ]; then
  echo "⚠️ Posible contenido mezclado inglés-español detectado ($mixed_content líneas)"
  echo "Revisar manualmente para confirmar si es apropiado"
else
  echo "✅ Contenido en español consistente"
fi

# Verificar preservación de metadatos YAML (si existen)
if head -n 5 "[archivo-original]" | grep -q "^---"; then
  if head -n 10 "repositorios/[repo]-esp/[archivo]" | grep -q "^---"; then
    echo "✅ Metadatos YAML preservados"
  else
    echo "❌ Metadatos YAML posiblemente perdidos"
    exit 1
  fi
fi
```

### 6. **Validación de Consistencia con Repositorio**
```bash
echo "🔍 Validando consistencia con repositorio..."

# Si existen otros archivos traducidos, verificar consistencia terminológica
if [ -d "repositorios/[repo]-esp/" ] && [ "$(find repositorios/[repo]-esp/ -name "*.md" | wc -l)" -gt 1 ]; then
  echo "Verificando consistencia terminológica con otros archivos..."
  
  python3 herramientas/validador-terminologia.py \
    --directorio "repositorios/[repo]-esp/" \
    --glosario configuracion/glosario-maestro.json \
    --verificar-consistencia \
    --reporte "temporal/consistencia-repo.json"
  
  if [ $? -eq 0 ]; then
    echo "✅ Consistencia terminológica con repositorio validada"
  else
    echo "⚠️ Posibles inconsistencias terminológicas detectadas"
    echo "Revisar: temporal/consistencia-repo.json"
  fi
fi
```

### 7. **Actualización de Metadatos**
```python
# Actualizar estado del archivo específico
import json
from datetime import datetime

# Cargar estado actual
with open('metadatos/estado-general.json', 'r') as f:
    estado = json.load(f)

# Actualizar información del archivo
repo = "[repo]"
archivo = "[archivo]"

if repo not in estado['frameworks']:
    estado['frameworks'][repo] = {}

if 'archivos_traducidos' not in estado['frameworks'][repo]:
    estado['frameworks'][repo]['archivos_traducidos'] = {}

estado['frameworks'][repo]['archivos_traducidos'][archivo] = {
    'fecha_traduccion': datetime.now().isoformat(),
    'validaciones_pasadas': ['estructura', 'terminologia', 'enlaces', 'calidad_tecnica'],
    'tiempo_traduccion_minutos': '[tiempo-real]',
    'revisor': 'claude-code-scribe'
}

# Actualizar estadísticas globales
total_traducidos = sum(
    len(fw.get('archivos_traducidos', {})) 
    for fw in estado['frameworks'].values()
)
estado['estadisticas_globales']['archivos_traducidos'] = total_traducidos

# Guardar estado actualizado
with open('metadatos/estado-general.json', 'w') as f:
    json.dump(estado, f, indent=2, ensure_ascii=False)

print(f"✅ Metadatos actualizados: {archivo} marcado como traducido")
```

### 8. **Reporte de Completación del Archivo**
```markdown
# 📄 Reporte de Traducción: [Archivo]

## Información General
- **Archivo original**: [repo-original]/[archivo]
- **Archivo traducido**: repositorios/[repo]-esp/[archivo]
- **Fecha**: [fecha-hora]
- **Tiempo empleado**: [minutos] minutos
- **Repositorio**: [repo]

## Validaciones Ejecutadas
- ✅ **Estructura**: Headers y formato preservados
- ✅ **Terminología**: Consistente con glosario maestro
- ✅ **Enlaces**: Funcionales y actualizados
- ✅ **Calidad técnica**: Código y metadatos preservados
- ✅ **Consistencia**: Coherente con otros archivos del repo

## Estadísticas de Traducción
- **Headers traducidos**: [cantidad]
- **Bloques de código preservados**: [cantidad]
- **Enlaces validados**: [cantidad]
- **Términos técnicos aplicados**: [cantidad]

## Adaptaciones Realizadas
- [Lista de decisiones de traducción específicas]
- [Términos técnicos mantenidos en inglés]
- [Adaptaciones culturales aplicadas]
- [Enlaces actualizados a versiones traducidas]

## Próximos Pasos
- [ ] Review por desarrollador hispanohablante nativo
- [ ] Validación con usuarios finales del repositorio
- [ ] Integración con otros archivos del repositorio
```

### 9. **Manejo de Errores Específicos**
```yaml
ERROR_PATTERNS:
  terminologia_inconsistente:
    detect: "Términos no encontrados en glosario"
    fix: "Agregar al glosario o usar traducción estándar"
    command: "python3 herramientas/validador-terminologia.py --sugerir"
    
  estructura_alterada:
    detect: "Número de headers no coincide"
    fix: "Revisar y restaurar estructura exacta"
    rollback: "Restaurar desde backup y repetir"
    
  enlaces_rotos:
    detect: "markdown-link-check falló"
    fix: "Actualizar enlaces a versiones traducidas o corregir paths"
    note: "Algunos enlaces pueden fallar temporalmente durante traducción"
    
  codigo_alterado:
    detect: "Número de bloques de código cambió"
    fix: "Revisar y restaurar código exacto"
    critical: "NUNCA alterar código funcional"
    
  metadatos_perdidos:
    detect: "YAML frontmatter no encontrado"
    fix: "Restaurar metadatos exactos del original"
    check: "Verificar que inicia y termina con ---"
```

## Quality Checklist Final
```yaml
COMPLETITUD:
  - [ ] Archivo completamente traducido
  - [ ] Estructura Markdown exactamente preservada
  - [ ] Metadatos y frontmatter intactos
  - [ ] Todas las validaciones automáticas pasadas

CALIDAD TÉCNICA:
  - [ ] Código preservado sin alteraciones
  - [ ] Enlaces actualizados apropiadamente
  - [ ] Terminología técnica consistente
  - [ ] Referencias y paths funcionales

CALIDAD LINGÜÍSTICA:
  - [ ] Español natural y técnicamente preciso
  - [ ] Consistencia con otros archivos del repo
  - [ ] Adaptaciones culturales apropiadas
  - [ ] Fluidez para audiencia hispanohablante

INTEGRACIÓN:
  - [ ] Metadatos del sistema actualizados
  - [ ] Reporte de traducción generado
  - [ ] Consistencia con glosario maestro validada
  - [ ] Ready para review y uso por comunidad
```

## Examples
```bash
# Traducción básica con validación
/traducir-archivo-execute PRPs/traduccion-readme-context-engineering-intro.md --validar-inmediato

# Traducción con backup de seguridad
/traducir-archivo-execute PRPs/traduccion-claude-superclaude-framework.md --backup --persona-scribe

# Simulación sin cambios (testing)
/traducir-archivo-execute PRPs/traduccion-prp-base-template.md --dry-run

# Traducción de archivo complejo
/traducir-archivo-execute PRPs/traduccion-commands-superclaude.md --think-hard --validar-inmediato
```