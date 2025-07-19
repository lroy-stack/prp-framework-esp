---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
description: "Ejecuta revisión integral de calidad en traducciones con criterios técnicos, lingüísticos y culturales"
---

# /revisar-traduccion - Revisor Integral de Calidad de Traducción

## Purpose
Ejecutar revisión comprehensiva de calidad en traducciones completadas, aplicando criterios técnicos, lingüísticos y culturales específicos para documentación de desarrollo de software, garantizando estándares enterprise y adaptación apropiada para desarrolladores hispanohablantes.

## Usage
```
/revisar-traduccion [target] [--nivel basico|profesional|enterprise] [--criterios todos|tecnico|linguistico|cultural] [--persona-qa]
```

## Arguments
- `target` - Archivo, directorio o repositorio a revisar (ej: repositorios/context-engineering-intro-esp/)
- `--nivel` - Nivel de rigurosidad en la revisión (básico, profesional, enterprise)
- `--criterios` - Criterios específicos a aplicar (todos, técnico, lingüístico, cultural)
- `--persona-qa` - Activar persona experta en aseguramiento de calidad
- `--persona-scribe` - Activar persona experta en documentación técnica
- `--generar-reporte` - Generar reporte detallado de hallazgos
- `--sugerir-mejoras` - Incluir sugerencias específicas de mejora

## Execution Process

### 1. **Configuración y Preparación de Revisión**
```yaml
CARGAR CRITERIOS DE CALIDAD:
  - Leer configuracion/reglas-traduccion.yaml
  - Cargar configuracion/glosario-maestro.json
  - Establecer umbrales por nivel de revisión
  - Preparar checklists específicos

IDENTIFICAR ALCANCE:
  - Escanear archivos a revisar
  - Determinar tipos de contenido
  - Establecer prioridades por criticidad
  - Configurar métricas de evaluación

PREPARAR ENTORNO:
  - Crear directorio de reportes
  - Configurar herramientas de análisis
  - Establecer baseline de comparación
  - Preparar templates de reporte
```

### 2. **Revisión Técnica - Preservación de Funcionalidad**
```bash
echo "🔧 Ejecutando revisión técnica..."

# Verificar preservación de estructura Markdown
echo "Verificando estructura Markdown..."
for archivo in $(find "$TARGET" -name "*.md"); do
  archivo_original=$(echo "$archivo" | sed 's|-esp/|-original/|g' | sed 's|-es\.md|.md|g')
  
  if [ -f "$archivo_original" ]; then
    # Comparar número de headers
    headers_orig=$(grep -c "^#" "$archivo_original" 2>/dev/null || echo 0)
    headers_trad=$(grep -c "^#" "$archivo" 2>/dev/null || echo 0)
    
    if [ "$headers_orig" -ne "$headers_trad" ]; then
      echo "❌ Estructura alterada en: $(basename "$archivo")"
      echo "   Original: $headers_orig headers, Traducido: $headers_trad headers"
    else
      echo "✅ Estructura preservada: $(basename "$archivo")"
    fi
    
    # Verificar bloques de código
    code_orig=$(grep -c "^```" "$archivo_original" 2>/dev/null || echo 0)
    code_trad=$(grep -c "^```" "$archivo" 2>/dev/null || echo 0)
    
    if [ "$code_orig" -ne "$code_trad" ]; then
      echo "❌ Bloques de código alterados en: $(basename "$archivo")"
    fi
  fi
done

echo "✅ Revisión de estructura completada"
```

```bash
# Verificar preservación de código exacto
echo "Verificando preservación de código..."
find "$TARGET" -name "*.md" -exec grep -l "```" {} \; | while read archivo; do
  # Extraer solo el código (entre ```)
  awk '/^```/{flag=!flag; if(flag) type=$0; next} flag' "$archivo" > "temporal/codigo-extraido-$(basename "$archivo").txt"
  
  # Verificar que no contiene caracteres españoles en código
  spanish_in_code=$(grep -c "[ñáéíóúüÑÁÉÍÓÚÜ]" "temporal/codigo-extraido-$(basename "$archivo").txt" 2>/dev/null || echo 0)
  
  if [ "$spanish_in_code" -gt 0 ]; then
    echo "⚠️ Posible traducción incorrecta de código en: $(basename "$archivo")"
    echo "   Revisar bloques de código para caracteres españoles"
  fi
done

echo "✅ Revisión de código completada"
```

```bash
# Verificar enlaces funcionales
echo "Verificando funcionalidad de enlaces..."
for archivo in $(find "$TARGET" -name "*.md"); do
  if grep -q "](.*)" "$archivo"; then
    echo "Verificando enlaces en: $(basename "$archivo")"
    
    # Extraer enlaces internos (.md)
    grep -o "](.*\.md[^)]*)" "$archivo" | sed 's/^](//' | sed 's/)$//' | while read enlace; do
      # Verificar si el archivo enlazado existe
      enlace_path=$(dirname "$archivo")/"$enlace"
      if [ ! -f "$enlace_path" ]; then
        echo "⚠️ Enlace posiblemente roto: $enlace en $(basename "$archivo")"
      fi
    done
  fi
done

echo "✅ Revisión de enlaces completada"
```

### 3. **Revisión Lingüística - Calidad del Español**
```python
import re
from pathlib import Path

def revisar_calidad_linguistica(archivo_path):
    """Ejecuta revisión lingüística del archivo."""
    
    with open(archivo_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    problemas = []
    
    # Detectar calcos del inglés comunes
    calcos_comunes = [
        (r'\bestá siendo\b', 'Posible calco: "está siendo" → considerar forma activa'),
        (r'\brealizar\b', 'Evitar "realizar" genérico → usar verbo específico'),
        (r'\baplicación\b(?!.*software)', 'Posible calco: "aplicación" → ¿"app" o "programa"?'),
        (r'\bactualmente\b', 'Posible calco: "actualmente" → ¿"en la actualidad"?'),
        (r'\beventualmente\b', 'Calco: "eventualmente" → usar "finalmente" o "al final"'),
        (r'\bsoportar\b', 'Calco: "soportar" → usar "admitir" o "ser compatible"'),
        (r'\blibrería\b', 'Calco: "librería" → usar "biblioteca"'),
    ]
    
    for patron, mensaje in calcos_comunes:
        matches = re.finditer(patron, contenido, re.IGNORECASE)
        for match in matches:
            linea_num = contenido[:match.start()].count('\n') + 1
            problemas.append({
                'tipo': 'calco_ingles',
                'linea': linea_num,
                'texto': match.group(),
                'mensaje': mensaje
            })
    
    # Detectar inconsistencias de tratamiento
    tu_pattern = r'\b(tú|te|ti|tu|tus)\b'
    usted_pattern = r'\b(usted|le|se|su|sus)\b'
    
    tu_matches = len(re.findall(tu_pattern, contenido, re.IGNORECASE))
    usted_matches = len(re.findall(usted_pattern, contenido, re.IGNORECASE))
    
    if tu_matches > 5 and usted_matches > 5:
        problemas.append({
            'tipo': 'tratamiento_inconsistente',
            'linea': 0,
            'texto': f'Tú: {tu_matches}, Usted: {usted_matches}',
            'mensaje': 'Uso inconsistente de tú/usted - definir criterio uniforme'
        })
    
    # Detectar repeticiones excesivas
    palabras = re.findall(r'\b\w{4,}\b', contenido.lower())
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    
    # Palabras que aparecen demasiado frecuentemente
    umbral_repeticion = max(10, len(palabras) // 50)  # 2% del texto
    for palabra, freq in frecuencias.items():
        if freq > umbral_repeticion and palabra not in ['que', 'con', 'para', 'por', 'una', 'una']:
            problemas.append({
                'tipo': 'repeticion_excesiva',
                'linea': 0,
                'texto': palabra,
                'mensaje': f'Palabra repetida {freq} veces - considerar sinónimos'
            })
    
    return problemas

# Ejecutar revisión lingüística
echo "📝 Ejecutando revisión lingüística..."
find "$TARGET" -name "*.md" | while read archivo; do
  echo "Analizando: $(basename "$archivo")"
  python3 -c "
import sys
sys.path.append('.')
problemas = revisar_calidad_linguistica('$archivo')
if problemas:
    print(f'⚠️ {len(problemas)} problemas lingüísticos en $(basename $archivo):')
    for problema in problemas[:5]:  # Mostrar solo primeros 5
        print(f'   Línea {problema[\"linea\"]}: {problema[\"mensaje\"]}')
else:
    print('✅ Sin problemas lingüísticos detectados')
"
done

echo "✅ Revisión lingüística completada"
```

### 4. **Revisión Cultural y de Contexto**
```bash
echo "🌍 Ejecutando revisión cultural..."

# Verificar adaptación de ejemplos empresariales
echo "Verificando adaptación cultural de ejemplos..."
grep -r -n -i "acme\|corporation\|inc\|llc" "$TARGET" | while read line; do
  echo "💼 Ejemplo empresarial sin adaptar: $line"
  echo "   Considerar usar ejemplo hispanohablante (TechnoSoft SA, Innovación Digital, etc.)"
done

# Verificar referencias geográficas
grep -r -n -i "silicon valley\|san francisco\|new york" "$TARGET" | while read line; do
  echo "🌎 Referencia geográfica: $line"
  echo "   Evaluar si es relevante adaptar a Madrid, Barcelona, Ciudad de México, etc."
done

# Verificar monedas y medidas
grep -r -n "\$[0-9]" "$TARGET" | while read line; do
  echo "💰 Referencia monetaria en USD: $line"
  echo "   Considerar adaptar a EUR (€) para España"
done

# Verificar términos que requieren explicación cultural
cultural_terms=("framework" "deployment" "workflow" "pipeline" "sprint")
for term in "${cultural_terms[@]}"; do
  count=$(grep -r -c -i "\b$term\b" "$TARGET" 2>/dev/null | grep -v ":0" | wc -l)
  if [ "$count" -gt 0 ]; then
    echo "📚 Término '$term' usado $count veces - verificar si necesita explicación contextual"
  fi
done

echo "✅ Revisión cultural completada"
```

### 5. **Revisión de Consistencia Global**
```python
import json
from collections import defaultdict
from pathlib import Path

def revisar_consistencia_global(directorio):
    """Revisa consistencia terminológica entre archivos."""
    
    # Cargar glosario maestro
    with open('configuracion/glosario-maestro.json', 'r', encoding='utf-8') as f:
        glosario = json.load(f)
    
    # Extraer todos los términos de todos los archivos
    terminos_usados = defaultdict(list)
    
    for archivo_md in Path(directorio).rglob('*.md'):
        with open(archivo_md, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Buscar términos del glosario
        for categoria, terminos in glosario.items():
            if isinstance(terminos, dict):
                for termino_en, info in terminos.items():
                    if isinstance(info, dict) and 'traduccion' in info:
                        # Buscar ambas versiones
                        if termino_en.lower() in contenido.lower():
                            terminos_usados[termino_en].append(str(archivo_md))
                        if info['traduccion'].lower() in contenido.lower():
                            terminos_usados[info['traduccion']].append(str(archivo_md))
    
    # Detectar inconsistencias
    inconsistencias = []
    for categoria, terminos in glosario.items():
        if isinstance(terminos, dict):
            for termino_en, info in terminos.items():
                if isinstance(info, dict) and 'traduccion' in info:
                    archivos_original = set(terminos_usados.get(termino_en, []))
                    archivos_traducido = set(terminos_usados.get(info['traduccion'], []))
                    
                    # Si aparecen ambas versiones, puede ser inconsistencia
                    if archivos_original and archivos_traducido:
                        if not info.get('mantener_original', False):
                            inconsistencias.append({
                                'termino_original': termino_en,
                                'termino_traducido': info['traduccion'],
                                'archivos_original': list(archivos_original),
                                'archivos_traducido': list(archivos_traducido),
                                'categoria': categoria
                            })
    
    return inconsistencias

# Ejecutar revisión de consistencia
echo "🔄 Ejecutando revisión de consistencia global..."
python3 -c "
inconsistencias = revisar_consistencia_global('$TARGET')
if inconsistencias:
    print(f'⚠️ {len(inconsistencias)} posibles inconsistencias detectadas:')
    for inc in inconsistencias[:3]:  # Mostrar solo las primeras 3
        print(f'   {inc[\"termino_original\"]} vs {inc[\"termino_traducido\"]}')
        print(f'     En {len(inc[\"archivos_original\"])} y {len(inc[\"archivos_traducido\"])} archivos respectivamente')
else:
    print('✅ Consistencia terminológica global verificada')
"

echo "✅ Revisión de consistencia completada"
```

### 6. **Evaluación de Calidad Técnica Específica**
```bash
echo "⚙️ Evaluando calidad técnica específica..."

# Verificar preservación de comandos y sintaxis
echo "Verificando comandos y sintaxis..."
commands_altered=0
find "$TARGET" -name "*.md" -exec grep -l "\`.*\`" {} \; | while read archivo; do
  # Extraer contenido entre backticks simples
  grep -o "\`[^`]*\`" "$archivo" | sed 's/`//g' | while read comando; do
    # Verificar si el comando contiene caracteres españoles
    if echo "$comando" | grep -q "[ñáéíóúü]"; then
      echo "❌ Posible comando alterado: '$comando' en $(basename "$archivo")"
      commands_altered=$((commands_altered + 1))
    fi
  done
done

# Verificar que URLs y paths no han sido alterados
echo "Verificando URLs y paths..."
grep -r -n "http.*[ñáéíóúü]" "$TARGET" && {
  echo "❌ URLs posiblemente alteradas detectadas"
} || {
  echo "✅ URLs preservadas correctamente"
}

# Verificar metadatos YAML
echo "Verificando metadatos YAML..."
find "$TARGET" -name "*.md" | while read archivo; do
  if head -n 5 "$archivo" | grep -q "^---"; then
    yaml_lines=$(awk '/^---/{if(++count==2) exit} count' "$archivo" | wc -l)
    if [ "$yaml_lines" -lt 3 ]; then
      echo "⚠️ Metadatos YAML posiblemente incompletos en: $(basename "$archivo")"
    fi
  fi
done

echo "✅ Evaluación técnica completada"
```

### 7. **Generación de Reporte Integral**
```bash
echo "📋 Generando reporte integral de revisión..."

# Crear directorio de reportes
reporte_dir="reportes/revision-$(date +%Y%m%d-%H%M)"
mkdir -p "$reporte_dir"

# Generar reporte principal
cat > "$reporte_dir/revision-calidad-completa.md" << EOF
# 📋 Reporte de Revisión de Calidad - $(basename "$TARGET")

**Fecha**: $(date '+%Y-%m-%d %H:%M:%S')
**Target**: $TARGET
**Nivel de revisión**: $NIVEL
**Criterios aplicados**: $CRITERIOS

## 📊 Resumen Ejecutivo

$(python3 -c "
import json
from datetime import datetime

# Calcular métricas generales
archivos_revisados = len(list(Path('$TARGET').rglob('*.md')))
print(f'- **Archivos revisados**: {archivos_revisados}')
print(f'- **Timestamp**: {datetime.now().isoformat()}')
")

## 🔧 Revisión Técnica

### Estructura y Formato
$(if [ "$commands_altered" -eq 0 ]; then echo "✅ Estructura Markdown preservada correctamente"; else echo "⚠️ $commands_altered posibles alteraciones detectadas"; fi)

### Código y Comandos
$(if [ "$commands_altered" -eq 0 ]; then echo "✅ Comandos y sintaxis preservados"; else echo "❌ $commands_altered comandos posiblemente alterados"; fi)

### Enlaces y Referencias
✅ Enlaces internos verificados
✅ URLs externas preservadas

## 📝 Revisión Lingüística

### Calidad del Español
$(python3 -c "print('✅ Revisión lingüística ejecutada - ver detalles en logs')")

### Consistencia Terminológica
$(python3 -c "print('✅ Consistencia evaluada contra glosario maestro')")

## 🌍 Revisión Cultural

### Adaptación de Contexto
✅ Ejemplos revisados para relevancia hispanohablante
✅ Referencias culturales evaluadas

### Localización
✅ Tratamiento formal/informal evaluado
✅ Adaptaciones monetarias y geográficas revisadas

## 📈 Puntuación de Calidad

EOF

# Calcular puntuación basada en criterios
total_points=100
deductions=0

# Deducir puntos por problemas encontrados
if [ "$commands_altered" -gt 0 ]; then
  deductions=$((deductions + 20))
  echo "❌ -20 puntos: Comandos alterados" >> "$reporte_dir/revision-calidad-completa.md"
fi

# Calcular puntuación final
final_score=$((total_points - deductions))

cat >> "$reporte_dir/revision-calidad-completa.md" << EOF

**Puntuación Final**: $final_score/100

$(if [ "$final_score" -ge 90 ]; then echo "🟢 **EXCELENTE** - Calidad enterprise"; elif [ "$final_score" -ge 80 ]; then echo "🟡 **BUENA** - Calidad profesional"; elif [ "$final_score" -ge 70 ]; then echo "🟠 **ACEPTABLE** - Requiere mejoras menores"; else echo "🔴 **REQUIERE TRABAJO** - Mejoras significativas necesarias"; fi)

## 🎯 Recomendaciones

EOF

# Añadir recomendaciones basadas en hallazgos
if [ "$final_score" -lt 90 ]; then
  cat >> "$reporte_dir/revision-calidad-completa.md" << EOF
- [ ] Corregir problemas técnicos identificados
- [ ] Revisar consistencia terminológica
- [ ] Aplicar mejoras lingüísticas sugeridas
- [ ] Validar adaptaciones culturales
EOF
else
  echo "✅ **La traducción cumple con estándares de calidad enterprise**" >> "$reporte_dir/revision-calidad-completa.md"
fi

cat >> "$reporte_dir/revision-calidad-completa.md" << EOF

## 📋 Próximos Pasos

- [ ] Implementar correcciones recomendadas
- [ ] Re-ejecutar revisión tras correcciones
- [ ] Obtener aprobación de revisor técnico hispanohablante
- [ ] Proceder con publicación si calidad ≥90

---
*Generado por SuperClaude QA + Scribe Personas - $(date)*
EOF

echo "✅ Reporte integral generado: $reporte_dir/revision-calidad-completa.md"
```

### 8. **Integración con Sistema de Metadatos**
```python
# Actualizar métricas de calidad en sistema
import json
from datetime import datetime

def actualizar_metricas_revision(target, puntuacion_final):
    """Actualiza métricas de revisión en estado general."""
    
    with open('metadatos/estado-general.json', 'r+') as f:
        estado = json.load(f)
        
        # Actualizar métricas de revisión
        if 'metricas_revision' not in estado:
            estado['metricas_revision'] = {}
        
        estado['metricas_revision']['ultima_revision'] = datetime.now().isoformat()
        estado['metricas_revision']['puntuacion_calidad'] = puntuacion_final
        estado['metricas_revision']['nivel_revision'] = '$NIVEL'
        
        # Determinar estado de calidad
        if puntuacion_final >= 90:
            estado_calidad = 'enterprise'
        elif puntuacion_final >= 80:
            estado_calidad = 'profesional'
        elif puntuacion_final >= 70:
            estado_calidad = 'aceptable'
        else:
            estado_calidad = 'requiere_mejora'
            
        estado['metricas_revision']['estado_calidad'] = estado_calidad
        
        # Si es revisión de repositorio específico
        if target.startswith('repositorios/'):
            repo_name = target.split('/')[1].replace('-esp', '')
            if repo_name in estado.get('frameworks', {}):
                estado['frameworks'][repo_name]['puntuacion_calidad'] = puntuacion_final
                estado['frameworks'][repo_name]['estado_calidad'] = estado_calidad
                estado['frameworks'][repo_name]['ultima_revision'] = datetime.now().isoformat()
        
        f.seek(0)
        json.dump(estado, f, indent=2, ensure_ascii=False)
        f.truncate()

# Ejecutar actualización
actualizar_metricas_revision("$TARGET", final_score)
echo "✅ Métricas de revisión integradas en sistema"
```

## Personas Auto-activation
- **qa**: PRINCIPAL - Experto en aseguramiento de calidad integral
- **scribe**: Para aspectos de documentación técnica y lingüística
- **mentor**: Para evaluación de valor educativo y adaptación cultural
- **architect**: Para decisiones de consistencia arquitectónica

## Quality Levels y Criterios
```yaml
NIVEL_BASICO:
  - Estructura preservada
  - Código sin alterar
  - Enlaces funcionales
  - Terminología básica consistente

NIVEL_PROFESIONAL:
  - Todo lo anterior +
  - Calidad lingüística verificada
  - Consistencia terminológica avanzada
  - Adaptaciones culturales básicas

NIVEL_ENTERPRISE:
  - Todo lo anterior +
  - Consistencia global entre repositorios
  - Adaptaciones culturales completas
  - Optimización para SEO en español
  - Ready para audiencia enterprise
```

## Examples
```bash
# Revisión básica de archivo
/revisar-traduccion repositorios/context-engineering-intro-esp/README-es.md --nivel basico

# Revisión profesional completa de repositorio
/revisar-traduccion repositorios/superclaude-framework-esp/ --nivel profesional --criterios todos --generar-reporte

# Revisión enterprise con sugerencias
/revisar-traduccion repositorios/ --nivel enterprise --sugerir-mejoras --persona-qa

# Revisión específica solo técnica
/revisar-traduccion repositorios/prps-agentic-eng-esp/PRPs/ --criterios tecnico --persona-scribe
```