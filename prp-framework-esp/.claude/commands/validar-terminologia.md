---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
description: "Valida consistencia terminológica en traducciones usando glosario maestro con reportes detallados y corrección automática"
---

# /validar-terminologia - Validador de Consistencia Terminológica

## Purpose
Ejecutar validación exhaustiva de consistencia terminológica en archivos traducidos utilizando el glosario maestro, detectar inconsistencias automáticamente, generar reportes detallados y proporcionar sugerencias de corrección para mantener calidad profesional en las traducciones.

## Usage
```
/validar-terminologia [target] [--tipo archivo|directorio|repositorio] [--auto-corregir] [--reporte detallado] [--persona-qa]
```

## Arguments
- `target` - Archivo, directorio o repositorio a validar (ej: repositorios/context-engineering-intro-esp/)
- `--tipo` - Alcance de validación (archivo individual, directorio completo, repositorio completo)
- `--auto-corregir` - Aplicar correcciones automáticas cuando sea seguro hacerlo
- `--reporte` - Nivel de detalle del reporte (básico, detallado, completo)
- `--persona-qa` - Activar persona experta en aseguramiento de calidad
- `--glosario` - Usar glosario específico (por defecto: glosario-maestro.json)
- `--exportar` - Exportar resultados a formato específico (json, csv, markdown)

## Execution Process

### 1. **Análisis de Configuración y Carga**
```yaml
CARGAR GLOSARIO MAESTRO:
  - Leer configuracion/glosario-maestro.json
  - Validar estructura y completitud
  - Cargar reglas de traducción específicas
  - Preparar patrones de búsqueda optimizados

CARGAR REGLAS DE TRADUCCIÓN:
  - Leer configuracion/reglas-traduccion.yaml
  - Extraer patrones específicos de validación
  - Configurar excepciones y casos especiales
  - Preparar criterios de calidad

IDENTIFICAR TARGET:
  - Determinar tipo de target (archivo/directorio/repositorio)
  - Escanear archivos .md relevantes
  - Establecer orden de procesamiento
  - Configurar reportes y métricas
```

### 2. **Ejecución de Herramienta Base**
```bash
echo "🔍 Ejecutando validador de terminología..."

# Preparar directorio de reportes
mkdir -p temporal/validacion-$(date +%Y%m%d)

# Ejecutar herramienta base con configuración apropiada
case "$TIPO" in
  "archivo")
    python3 herramientas/validador-terminologia.py \
      --archivo "$TARGET" \
      --glosario configuracion/glosario-maestro.json \
      --reporte "temporal/validacion-$(date +%Y%m%d)/$(basename "$TARGET" .md)-terminologia.json" \
      --verbose
    ;;
  "directorio")
    python3 herramientas/validador-terminologia.py \
      --directorio "$TARGET" \
      --glosario configuracion/glosario-maestro.json \
      --reporte "temporal/validacion-$(date +%Y%m%d)/directorio-terminologia.json" \
      --verificar-consistencia \
      --estadisticas
    ;;
  "repositorio")
    python3 herramientas/validador-terminologia.py \
      --directorio "$TARGET" \
      --glosario configuracion/glosario-maestro.json \
      --reporte "temporal/validacion-$(date +%Y%m%d)/repositorio-completo.json" \
      --verificar-consistencia \
      --estadisticas \
      --generar-sugerencias
    ;;
esac

# Capturar código de salida
VALIDATION_EXIT_CODE=$?
```

### 3. **Análisis Avanzado de Resultados**
```python
import json
from pathlib import Path
from datetime import datetime

def analizar_resultados_validacion(reporte_path):
    """Análisis avanzado de resultados de validación."""
    
    with open(reporte_path, 'r', encoding='utf-8') as f:
        resultados = json.load(f)
    
    # Métricas de calidad
    metricas = {
        'archivos_analizados': len(resultados.get('archivos', [])),
        'terminos_validados': resultados.get('estadisticas', {}).get('terminos_encontrados', 0),
        'errores_encontrados': resultados.get('estadisticas', {}).get('errores_encontrados', 0),
        'consistencia_porcentaje': 0,
        'categorias_problematicas': [],
        'archivos_con_errores': []
    }
    
    # Calcular porcentaje de consistencia
    if metricas['terminos_validados'] > 0:
        metricas['consistencia_porcentaje'] = round(
            ((metricas['terminos_validados'] - metricas['errores_encontrados']) / 
             metricas['terminos_validados']) * 100, 2
        )
    
    # Identificar categorías problemáticas
    errores_por_categoria = {}
    for archivo_info in resultados.get('archivos', []):
        for error in archivo_info.get('errores', []):
            categoria = error.get('categoria', 'desconocida')
            errores_por_categoria[categoria] = errores_por_categoria.get(categoria, 0) + 1
    
    # Ordenar por frecuencia
    metricas['categorias_problematicas'] = sorted(
        errores_por_categoria.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    # Archivos con errores
    metricas['archivos_con_errores'] = [
        archivo['nombre'] for archivo in resultados.get('archivos', [])
        if archivo.get('errores', [])
    ]
    
    return metricas

# Ejecutar análisis
reporte_file = f"temporal/validacion-{datetime.now().strftime('%Y%m%d')}/[target-file].json"
if Path(reporte_file).exists():
    metricas = analizar_resultados_validacion(reporte_file)
    print(f"📊 Análisis de Resultados:")
    print(f"   Consistencia: {metricas['consistencia_porcentaje']}%")
    print(f"   Errores: {metricas['errores_encontrados']}")
    print(f"   Archivos problemáticos: {len(metricas['archivos_con_errores'])}")
```

### 4. **Detección de Patrones Específicos**
```bash
echo "🔍 Analizando patrones específicos..."

# Detectar uso incorrecto de términos técnicos
echo "Verificando términos técnicos críticos..."
grep -r -n "mejor práctica\|mejores prácticas" "$TARGET" && {
  echo "⚠️ Detectado: 'mejor práctica' - Considerar usar 'práctica recomendada' o mantener 'best practice'"
}

grep -r -n "prompt engineering" "$TARGET" && {
  echo "✅ Correcto: 'prompt engineering' preservado"
}

# Detectar inconsistencias en tratamiento formal/informal
echo "Verificando consistencia de tratamiento..."
tu_count=$(grep -r -c "\bte\b\|\btu\b\|\btus\b" "$TARGET" 2>/dev/null || echo 0)
usted_count=$(grep -r -c "\busted\b\|\ble\b\|\bsu\b" "$TARGET" 2>/dev/null || echo 0)

if [ "$tu_count" -gt 0 ] && [ "$usted_count" -gt 0 ]; then
  echo "⚠️ Posible inconsistencia: Uso mezclado de tú/usted detectado"
  echo "   Apariciones 'tú': $tu_count, 'usted': $usted_count"
fi

# Verificar preservación de código
echo "Verificando preservación de código..."
code_alterations=$(grep -r -n "```.*[ñáéíóúü]" "$TARGET" 2>/dev/null | wc -l)
if [ "$code_alterations" -gt 0 ]; then
  echo "❌ Posible alteración de código detectada en $code_alterations líneas"
  grep -r -n "```.*[ñáéíóúü]" "$TARGET"
else
  echo "✅ Código preservado correctamente"
fi
```

### 5. **Corrección Automática Segura**
```python
import re
import json
from pathlib import Path

def aplicar_correcciones_automaticas(archivo, glosario_path):
    """Aplica correcciones automáticas seguras basadas en glosario."""
    
    with open(glosario_path, 'r', encoding='utf-8') as f:
        glosario = json.load(f)
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    contenido_original = contenido
    correcciones_aplicadas = []
    
    # Solo aplicar correcciones de términos core seguros
    for categoria, terminos in glosario.items():
        if categoria in ['terminos_core', 'terminos_ui']:
            for termino_en, info in terminos.items():
                if isinstance(info, dict) and 'traduccion' in info:
                    # Solo corregir si NO debe mantenerse original
                    if not info.get('mantener_original', False):
                        patron_seguro = rf'\b{re.escape(termino_en)}\b'
                        if re.search(patron_seguro, contenido):
                            contenido_nuevo = re.sub(
                                patron_seguro, 
                                info['traduccion'], 
                                contenido
                            )
                            if contenido_nuevo != contenido:
                                correcciones_aplicadas.append({
                                    'termino_original': termino_en,
                                    'termino_corregido': info['traduccion'],
                                    'categoria': categoria
                                })
                                contenido = contenido_nuevo
    
    # Solo escribir si hay cambios
    if contenido != contenido_original:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        return correcciones_aplicadas
    
    return []

# Aplicar correcciones si se solicita
if [ "$AUTO_CORREGIR" = "true" ]; then
  echo "🔧 Aplicando correcciones automáticas seguras..."
  
  python3 -c "
import sys
sys.path.append('herramientas')
correcciones = aplicar_correcciones_automaticas('$TARGET', 'configuracion/glosario-maestro.json')
if correcciones:
    print(f'✅ {len(correcciones)} correcciones aplicadas automáticamente')
    for corr in correcciones:
        print(f'   {corr[\"termino_original\"]} → {corr[\"termino_corregido\"]}')
else:
    print('ℹ️ No se encontraron correcciones automáticas seguras')
"
fi
```

### 6. **Generación de Reportes Detallados**
```bash
echo "📋 Generando reporte detallado..."

# Crear reporte en Markdown
cat > "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md" << EOF
# 📊 Reporte de Validación Terminológica

**Fecha**: $(date '+%Y-%m-%d %H:%M:%S')
**Target**: $TARGET
**Tipo**: $TIPO

## 📈 Métricas Generales

- **Archivos analizados**: $(find "$TARGET" -name "*.md" | wc -l)
- **Consistencia terminológica**: ${metricas[consistencia_porcentaje]}%
- **Términos validados**: ${metricas[terminos_validados]}
- **Errores encontrados**: ${metricas[errores_encontrados]}

## 🎯 Estado de Calidad

EOF

# Añadir estado basado en porcentaje
if [ "${metricas[consistencia_porcentaje]}" -ge 95 ]; then
  echo "✅ **EXCELENTE** - Calidad enterprise (≥95%)" >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md"
elif [ "${metricas[consistencia_porcentaje]}" -ge 90 ]; then
  echo "🟡 **BUENA** - Calidad profesional (90-94%)" >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md"
elif [ "${metricas[consistencia_porcentaje]}" -ge 80 ]; then
  echo "🟠 **ACEPTABLE** - Requiere mejora (80-89%)" >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md"
else
  echo "🔴 **REQUIERE ATENCIÓN** - Calidad insuficiente (<80%)" >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md"
fi

# Añadir recomendaciones específicas
cat >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md" << EOF

## 🔧 Recomendaciones

EOF

if [ "${metricas[errores_encontrados]}" -gt 0 ]; then
  cat >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md" << EOF
### Errores a Corregir

$(python3 herramientas/validador-terminologia.py --archivo "$TARGET" --generar-sugerencias 2>/dev/null | head -10)

### Archivos Problemáticos

EOF
  for archivo in "${metricas[archivos_con_errores][@]}"; do
    echo "- $archivo" >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md"
  done
fi

cat >> "temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md" << EOF

## 📋 Próximos Pasos

- [ ] Revisar y corregir errores identificados
- [ ] Aplicar correcciones automáticas seguras
- [ ] Validar cambios con re-ejecución
- [ ] Documentar decisiones de traducción específicas

---
*Generado por SuperClaude QA Persona - $(date)*
EOF

echo "✅ Reporte detallado generado: temporal/validacion-$(date +%Y%m%d)/reporte-terminologia.md"
```

### 7. **Validación Cruzada con Otros Repositorios**
```bash
echo "🔄 Ejecutando validación cruzada..."

# Si hay múltiples repositorios traducidos, verificar consistencia entre ellos
if [ -d "repositorios/" ]; then
  repos_traducidos=$(find repositorios/ -name "*-esp" -type d | wc -l)
  
  if [ "$repos_traducidos" -gt 1 ]; then
    echo "Verificando consistencia entre $repos_traducidos repositorios..."
    
    # Crear glosario consolidado de términos usados
    find repositorios/ -name "*.md" -exec cat {} \; | \
      grep -oE '\b[A-Z][a-zA-Z]{3,}\b' | \
      sort | uniq -c | sort -nr | head -20 > \
      temporal/validacion-$(date +%Y%m%d)/terminos-consolidados.txt
    
    echo "✅ Análisis de términos consolidados completado"
    echo "📄 Ver: temporal/validacion-$(date +%Y%m%d)/terminos-consolidados.txt"
  fi
fi
```

### 8. **Integración con Sistema de Metadatos**
```python
# Actualizar métricas en estado general
import json
from datetime import datetime

def actualizar_metricas_validacion(target, metricas):
    """Actualiza métricas de validación en estado general."""
    
    with open('metadatos/estado-general.json', 'r+') as f:
        estado = json.load(f)
        
        # Actualizar métricas de calidad
        if 'metricas_calidad' not in estado:
            estado['metricas_calidad'] = {}
        
        estado['metricas_calidad']['ultima_validacion'] = datetime.now().isoformat()
        estado['metricas_calidad']['consistencia_terminologica'] = metricas['consistencia_porcentaje']
        estado['metricas_calidad']['errores_pendientes'] = metricas['errores_encontrados']
        
        # Si es validación de repositorio específico
        if target.startswith('repositorios/'):
            repo_name = target.split('/')[1].replace('-esp', '')
            if repo_name in estado.get('frameworks', {}):
                estado['frameworks'][repo_name]['calidad_terminologica'] = metricas['consistencia_porcentaje']
                estado['frameworks'][repo_name]['ultima_validacion'] = datetime.now().isoformat()
        
        f.seek(0)
        json.dump(estado, f, indent=2, ensure_ascii=False)
        f.truncate()

# Ejecutar actualización
actualizar_metricas_validacion("$TARGET", metricas)
echo "✅ Métricas de validación integradas en sistema"
```

## Personas Auto-activation
- **qa**: PRINCIPAL - Experto en aseguramiento de calidad y validación
- **scribe**: Para aspectos de documentación técnica
- **architect**: Para decisiones de consistencia a nivel sistema

## Quality Gates y Umbrales
```yaml
UMBRALES_CALIDAD:
  excelente: "≥95% consistencia"
  profesional: "90-94% consistencia"
  aceptable: "80-89% consistencia"
  requiere_atencion: "<80% consistencia"

CRITERIOS_AUTOMATICOS:
  auto_aprobar: "≥95% y 0 errores críticos"
  revisar_manual: "90-94% o errores menores"
  rechazar: "<90% o errores críticos"

ACCIONES_POR_UMBRAL:
  excelente: "Aprobar automáticamente"
  profesional: "Aprobar con comentarios"
  aceptable: "Solicitar correcciones menores"
  requiere_atencion: "Bloquear hasta corrección"
```

## Examples
```bash
# Validación básica de archivo
/validar-terminologia repositorios/context-engineering-intro-esp/README-es.md --tipo archivo

# Validación completa de repositorio con corrección
/validar-terminologia repositorios/superclaude-framework-esp/ --tipo repositorio --auto-corregir --reporte completo

# Validación de directorio específico
/validar-terminologia repositorios/prps-agentic-eng-esp/PRPs/ --tipo directorio --persona-qa

# Exportar resultados para análisis externo
/validar-terminologia repositorios/ --tipo repositorio --exportar csv --reporte detallado
```

## Anti-Patterns to Avoid
- ❌ No ejecutar validación después de cada traducción
- ❌ No revisar reportes detallados de errores
- ❌ Aplicar correcciones automáticas sin verificar contexto
- ❌ Ignorar inconsistencias entre repositorios
- ❌ No actualizar glosario con nuevos términos encontrados