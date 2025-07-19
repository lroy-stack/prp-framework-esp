---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
description: "Dashboard ejecutivo de estado de traducción con métricas en tiempo real y progreso por repositorio"
---

# /status-traduccion - Dashboard de Estado de Traducción

## Purpose
Proporcionar dashboard ejecutivo del estado actual del proyecto de traducción con métricas en tiempo real, progreso detallado por repositorio, análisis de calidad, estimaciones de tiempo y recomendaciones actionable para toma de decisiones.

## Usage
```
/status-traduccion [--repositorio repo] [--formato dashboard|resumen|completo] [--metricas] [--roadmap]
```

## Arguments
- `--repositorio` - Estado específico de repositorio (context-engineering-intro, prps-agentic-eng, superclaude-framework)
- `--formato` - Tipo de reporte (dashboard visual, resumen ejecutivo, análisis completo)
- `--metricas` - Incluir métricas detalladas de rendimiento y calidad
- `--roadmap` - Mostrar roadmap y próximos pasos recomendados
- `--exportar` - Exportar a formato (json, csv, markdown)
- `--historico` - Incluir tendencias históricas

## Execution Process

### 1. **Recolección de Datos del Sistema**
```bash
echo "📊 Recolectando datos del sistema..."

# Cargar estado general
if [ -f "metadatos/estado-general.json" ]; then
  echo "✅ Estado general encontrado"
else
  echo "❌ Estado general no encontrado - ejecutar sincronización inicial"
  exit 1
fi

# Verificar estructura de repositorios
repos_disponibles=0
repos_inicializados=0
repos_completados=0

for repo in context-engineering-intro prps-agentic-eng superclaude-framework; do
  if [ -d "../$repo" ]; then
    repos_disponibles=$((repos_disponibles + 1))
  fi
  
  if [ -d "repositorios/${repo}-esp" ]; then
    repos_inicializados=$((repos_inicializados + 1))
    
    # Verificar si tiene archivos traducidos
    archivos_traducidos=$(find "repositorios/${repo}-esp" -name "*.md" 2>/dev/null | wc -l)
    if [ "$archivos_traducidos" -gt 0 ]; then
      repos_completados=$((repos_completados + 1))
    fi
  fi
done

echo "📈 Repositorios: $repos_disponibles disponibles, $repos_inicializados inicializados, $repos_completados con contenido"
```

### 2. **Análisis de Progreso Global**
```python
import json
from datetime import datetime, timedelta
from pathlib import Path

def calcular_metricas_globales():
    """Calcula métricas globales del proyecto de traducción."""
    
    # Cargar estado general
    with open('metadatos/estado-general.json', 'r') as f:
        estado = json.load(f)
    
    # Cargar mapeo de archivos para obtener totales esperados
    with open('configuracion/mapeo-archivos.json', 'r') as f:
        mapeo = json.load(f)
    
    metricas = {
        'fecha_consulta': datetime.now().isoformat(),
        'progreso_global': {},
        'progreso_por_repositorio': {},
        'metricas_calidad': {},
        'metricas_tiempo': {},
        'recomendaciones': []
    }
    
    # Calcular progreso global
    total_archivos_esperados = 0
    total_archivos_traducidos = 0
    total_archivos_criticos_esperados = 0
    total_archivos_criticos_traducidos = 0
    
    for repo, config in mapeo.get('frameworks', {}).items():
        archivos_criticos_esperados = len(config.get('archivos_criticos', {}))
        total_archivos_criticos_esperados += archivos_criticos_esperados
        
        # Contar archivos traducidos
        repo_esp_dir = Path(f'repositorios/{repo}-esp')
        if repo_esp_dir.exists():
            archivos_traducidos = len(list(repo_esp_dir.rglob('*.md')))
            total_archivos_traducidos += archivos_traducidos
            
            # Contar archivos críticos traducidos
            archivos_criticos_traducidos = 0
            for archivo_critico in config.get('archivos_criticos', {}):
                archivo_traducido = repo_esp_dir / archivo_critico.replace('.md', '-es.md')
                if archivo_traducido.exists():
                    archivos_criticos_traducidos += 1
            
            total_archivos_criticos_traducidos += archivos_criticos_traducidos
            
            # Métricas por repositorio
            progreso_repo = {
                'archivos_criticos_esperados': archivos_criticos_esperados,
                'archivos_criticos_traducidos': archivos_criticos_traducidos,
                'progreso_criticos_porcentaje': round((archivos_criticos_traducidos / archivos_criticos_esperados * 100), 2) if archivos_criticos_esperados > 0 else 0,
                'archivos_total_traducidos': archivos_traducidos,
                'tiempo_estimado_restante': config.get('tiempo_estimado_horas', 0),
                'prioridad': 1 if repo == 'context-engineering-intro' else 2 if repo == 'prps-agentic-eng' else 3
            }
            
            # Determinar estado
            if progreso_repo['progreso_criticos_porcentaje'] >= 100:
                progreso_repo['estado'] = 'completado'
            elif progreso_repo['progreso_criticos_porcentaje'] >= 50:
                progreso_repo['estado'] = 'en_progreso'
            elif progreso_repo['progreso_criticos_porcentaje'] > 0:
                progreso_repo['estado'] = 'iniciado'
            else:
                progreso_repo['estado'] = 'pendiente'
            
            metricas['progreso_por_repositorio'][repo] = progreso_repo
    
    # Métricas globales
    progreso_criticos_global = round((total_archivos_criticos_traducidos / total_archivos_criticos_esperados * 100), 2) if total_archivos_criticos_esperados > 0 else 0
    
    metricas['progreso_global'] = {
        'archivos_criticos_completados': total_archivos_criticos_traducidos,
        'archivos_criticos_totales': total_archivos_criticos_esperados,
        'progreso_porcentaje': progreso_criticos_global,
        'archivos_totales_traducidos': total_archivos_traducidos,
        'repositorios_completados': len([r for r in metricas['progreso_por_repositorio'].values() if r['estado'] == 'completado']),
        'repositorios_totales': len(mapeo.get('frameworks', {}))
    }
    
    # Métricas de calidad (si existen)
    if 'metricas_calidad' in estado:
        metricas['metricas_calidad'] = estado['metricas_calidad']
    
    if 'metricas_revision' in estado:
        metricas['metricas_calidad'].update(estado['metricas_revision'])
    
    # Generar recomendaciones
    if progreso_criticos_global < 30:
        metricas['recomendaciones'].append("🚀 Prioridad: Iniciar con Context Engineering Intro (mayor ROI)")
    elif progreso_criticos_global < 70:
        metricas['recomendaciones'].append("📈 Continuar con el repositorio actual antes de iniciar nuevo")
    else:
        metricas['recomendaciones'].append("🎯 Excelente progreso - preparar para revisión final")
    
    return metricas

# Ejecutar cálculo
print("Calculando métricas globales...")
metricas = calcular_metricas_globales()
print(f"✅ Métricas calculadas - Progreso global: {metricas['progreso_global']['progreso_porcentaje']}%")
```

### 3. **Dashboard Visual Ejecutivo**
```bash
echo "🎯 Generando Dashboard Ejecutivo..."

cat > "reportes/dashboard-$(date +%Y%m%d-%H%M).md" << EOF
# 📊 Dashboard Ejecutivo - Estado de Traducción PRP Framework

**Fecha**: $(date '+%Y-%m-%d %H:%M:%S')
**Proyecto**: Traducción PRP Framework al Español
**Versión Dashboard**: v2.0

## 🎯 Estado Global del Proyecto

$(python3 -c "
import json
with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

progreso = metricas['progreso_global']['progreso_porcentaje']
completados = metricas['progreso_global']['archivos_criticos_completados']
totales = metricas['progreso_global']['archivos_criticos_totales']

# Barra de progreso visual
bar_width = 30
filled = int((progreso / 100) * bar_width)
empty = bar_width - filled
bar = '█' * filled + '░' * empty

print(f'**Progreso General**: {progreso}%')
print(f'\`{bar}\` {completados}/{totales} archivos críticos')
print()

# Estado por color
if progreso >= 80:
    status = '🟢 EN OBJETIVO'
elif progreso >= 50:
    status = '🟡 EN PROGRESO'
elif progreso >= 20:
    status = '🟠 INICIADO'
else:
    status = '🔴 PENDIENTE'

print(f'**Estado**: {status}')
")

## 📈 Progreso por Repositorio

$(python3 -c "
import json
with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

repos_orden = ['context-engineering-intro', 'prps-agentic-eng', 'superclaude-framework']
for repo in repos_orden:
    if repo in metricas['progreso_por_repositorio']:
        data = metricas['progreso_por_repositorio'][repo]
        progreso = data['progreso_criticos_porcentaje']
        estado = data['estado']
        
        # Icono por estado
        iconos = {
            'completado': '✅',
            'en_progreso': '🔄',
            'iniciado': '🟡',
            'pendiente': '⚪'
        }
        icono = iconos.get(estado, '❓')
        
        # Nombre más amigable
        nombres = {
            'context-engineering-intro': 'Context Engineering Intro',
            'prps-agentic-eng': 'PRPs Agentic Engineering', 
            'superclaude-framework': 'SuperClaude Framework'
        }
        nombre = nombres.get(repo, repo)
        
        print(f'### {icono} {nombre}')
        print(f'- **Progreso**: {progreso}% archivos críticos')
        print(f'- **Estado**: {estado.replace(\"_\", \" \").title()}')
        print(f'- **Archivos**: {data[\"archivos_criticos_traducidos\"]}/{data[\"archivos_criticos_esperados\"]} críticos')
        print()
")

## 📊 Métricas de Calidad

$(python3 -c "
import json
with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

calidad = metricas.get('metricas_calidad', {})
if calidad:
    print('### 🎯 Indicadores de Calidad')
    
    if 'consistencia_terminologica' in calidad:
        consistencia = calidad['consistencia_terminologica']
        if consistencia >= 95:
            print(f'- **Terminología**: ✅ {consistencia}% (Excelente)')
        elif consistencia >= 90:
            print(f'- **Terminología**: 🟡 {consistencia}% (Buena)')
        else:
            print(f'- **Terminología**: 🔴 {consistencia}% (Requiere atención)')
    
    if 'puntuacion_calidad' in calidad:
        puntuacion = calidad['puntuacion_calidad']
        if puntuacion >= 90:
            print(f'- **Calidad General**: ✅ {puntuacion}/100 (Enterprise)')
        elif puntuacion >= 80:
            print(f'- **Calidad General**: 🟡 {puntuacion}/100 (Profesional)')
        else:
            print(f'- **Calidad General**: 🔴 {puntuacion}/100 (Requiere mejora)')
    
    if 'ultima_validacion' in calidad:
        print(f'- **Última Validación**: {calidad[\"ultima_validacion\"][:10]}')
else:
    print('### ⚠️ Métricas de Calidad')
    print('- No hay datos de calidad disponibles')
    print('- Ejecutar validación terminológica para obtener métricas')
")

## ⏱️ Estimaciones de Tiempo

$(python3 -c "
import json
with open('configuracion/mapeo-archivos.json', 'r') as f:
    mapeo = json.load(f)

with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

print('### 📅 Planificación Temporal')

tiempo_total_estimado = mapeo.get('metricas_estimacion', {}).get('tiempo_total_horas', 88)
tiempo_consumido = 0

# Calcular tiempo consumido basado en progreso
for repo, data in metricas['progreso_por_repositorio'].items():
    repo_config = mapeo['frameworks'].get(repo, {})
    tiempo_repo = sum(info.get('tiempo_estimado_horas', 0) for info in repo_config.get('archivos_criticos', {}).values())
    progreso_repo = data['progreso_criticos_porcentaje'] / 100
    tiempo_consumido += tiempo_repo * progreso_repo

tiempo_restante = tiempo_total_estimado - tiempo_consumido

print(f'- **Tiempo Total Estimado**: {tiempo_total_estimado} horas')
print(f'- **Tiempo Consumido**: {tiempo_consumido:.1f} horas')
print(f'- **Tiempo Restante**: {tiempo_restante:.1f} horas')

# Estimación de finalización
if tiempo_restante > 0:
    semanas_restantes = tiempo_restante / 10  # Asumiendo 10h/semana
    print(f'- **Estimación Finalización**: {semanas_restantes:.1f} semanas ({tiempo_restante/40:.1f} meses)')
else:
    print(f'- **Estado**: ✅ Proyecto completado')
")

## 🎯 Recomendaciones Prioritarias

$(python3 -c "
import json
with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

print('### 🚀 Acciones Inmediatas')
for rec in metricas.get('recomendaciones', []):
    print(f'- {rec}')

# Recomendaciones específicas por estado
progreso = metricas['progreso_global']['progreso_porcentaje']

if progreso < 10:
    print('- 📋 Ejecutar: `/traducir-repo-create context-engineering-intro --prioridad alta`')
elif progreso < 50:
    print('- 🔄 Continuar traducción del repositorio actual')
    print('- 🔍 Ejecutar validación terminológica regular')
elif progreso < 80:
    print('- 📊 Ejecutar revisión de calidad en repositorios completados')
    print('- 🎯 Preparar siguiente repositorio en pipeline')
else:
    print('- ✅ Ejecutar revisión final enterprise')
    print('- 📢 Preparar para publicación y promoción')
")

## 📋 Próximos Pasos (Próximas 2 semanas)

$(python3 -c "
import json
from datetime import datetime, timedelta

with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

print('### 🗓️ Roadmap Inmediato')

# Determinar próximos pasos basado en estado actual
progreso_repos = metricas['progreso_por_repositorio']

# Encontrar próximo repositorio a trabajar
repos_pendientes = [repo for repo, data in progreso_repos.items() if data['estado'] in ['pendiente', 'iniciado']]
repos_en_progreso = [repo for repo, data in progreso_repos.items() if data['estado'] == 'en_progreso']

if repos_en_progreso:
    print(f'- **Semana 1-2**: Completar {repos_en_progreso[0]}')
    print(f'- **Ejecutar**: Traducción de archivos críticos restantes')
    print(f'- **Validar**: Terminología y calidad continua')

if repos_pendientes:
    print(f'- **Semana 3-4**: Iniciar {repos_pendientes[0]}')
    print(f'- **Preparar**: PRP de traducción completa')

print(f'- **Continuous**: Validación terminológica y revisión calidad')
print(f'- **Continuous**: Actualización de métricas y reportes')
")

---

## 📞 Comandos Útiles

\`\`\`bash
# Actualizar este dashboard
/status-traduccion --formato dashboard

# Validar calidad actual
/validar-terminologia repositorios/ --tipo repositorio

# Revisar calidad específica
/revisar-traduccion repositorios/[repo]-esp/ --nivel profesional

# Generar PRP para siguiente repo
/traducir-repo-create [siguiente-repo] --prioridad alta
\`\`\`

*Dashboard generado automáticamente - $(date '+%Y-%m-%d %H:%M')*
EOF

echo "✅ Dashboard generado: reportes/dashboard-$(date +%Y%m%d-%H%M).md"
```

### 4. **Análisis de Tendencias (si hay histórico)**
```python
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

def analizar_tendencias():
    """Analiza tendencias históricas si hay datos disponibles."""
    
    reportes_dir = Path('reportes')
    dashboards = sorted(reportes_dir.glob('dashboard-*.md'))
    
    if len(dashboards) < 2:
        return "No hay suficientes datos históricos para análisis de tendencias"
    
    tendencias = {
        'velocidad_traduccion': 'No disponible',
        'mejora_calidad': 'No disponible',
        'prediccion_finalizacion': 'No disponible'
    }
    
    # Si hay métricas históricas, analizarlas
    metricas_files = sorted(Path('temporal').glob('metricas-globales-*.json'))
    
    if len(metricas_files) >= 2:
        # Comparar últimas dos métricas
        with open(metricas_files[-1], 'r') as f:
            metricas_actual = json.load(f)
        with open(metricas_files[-2], 'r') as f:
            metricas_anterior = json.load(f)
        
        progreso_actual = metricas_actual['progreso_global']['progreso_porcentaje']
        progreso_anterior = metricas_anterior['progreso_global']['progreso_porcentaje']
        
        delta_progreso = progreso_actual - progreso_anterior
        
        if delta_progreso > 0:
            tendencias['velocidad_traduccion'] = f"📈 +{delta_progreso:.1f}% desde última medición"
        else:
            tendencias['velocidad_traduccion'] = f"📊 Estable ({delta_progreso:.1f}%)"
    
    return tendencias

# Ejecutar análisis de tendencias si se solicita
if [ "$HISTORICO" = "true" ]; then
  echo "📈 Analizando tendencias históricas..."
  python3 -c "
tendencias = analizar_tendencias()
print('### 📈 Análisis de Tendencias')
for key, value in tendencias.items():
    print(f'- **{key.replace(\"_\", \" \").title()}**: {value}')
"
fi
```

### 5. **Exportación de Datos**
```bash
if [ "$EXPORTAR" ]; then
  echo "📤 Exportando datos en formato $EXPORTAR..."
  
  case "$EXPORTAR" in
    "json")
      cp temporal/metricas-globales.json "reportes/status-export-$(date +%Y%m%d).json"
      echo "✅ Datos exportados: reportes/status-export-$(date +%Y%m%d).json"
      ;;
    "csv")
      python3 -c "
import json
import csv
from datetime import datetime

with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

# Crear CSV con datos por repositorio
with open(f'reportes/status-export-{datetime.now().strftime(\"%Y%m%d\")}.csv', 'w', newline='') as csvfile:
    fieldnames = ['repositorio', 'progreso_porcentaje', 'archivos_traducidos', 'archivos_totales', 'estado', 'prioridad']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for repo, data in metricas['progreso_por_repositorio'].items():
        writer.writerow({
            'repositorio': repo,
            'progreso_porcentaje': data['progreso_criticos_porcentaje'],
            'archivos_traducidos': data['archivos_criticos_traducidos'],
            'archivos_totales': data['archivos_criticos_esperados'],
            'estado': data['estado'],
            'prioridad': data['prioridad']
        })

print('✅ Datos exportados en CSV')
"
      ;;
    "markdown")
      cp "reportes/dashboard-$(date +%Y%m%d)*.md" "reportes/status-export-$(date +%Y%m%d).md" 2>/dev/null || echo "Dashboard ya está en formato markdown"
      ;;
  esac
fi
```

### 6. **Guardado de Métricas para Histórico**
```bash
# Guardar métricas actuales para análisis histórico futuro
echo "$metricas" > "temporal/metricas-globales-$(date +%Y%m%d-%H%M).json"
echo "$metricas" > "temporal/metricas-globales.json"  # Versión actual

echo "💾 Métricas guardadas para histórico"
```

### 7. **Recomendaciones Específicas de Comando**
```bash
echo "🎯 Generando recomendaciones específicas..."

python3 -c "
import json
with open('temporal/metricas-globales.json', 'r') as f:
    metricas = json.load(f)

print('## 🚀 Comandos Recomendados para Ejecutar Ahora:')
print()

# Recomendaciones basadas en estado actual
progreso_global = metricas['progreso_global']['progreso_porcentaje']
repos = metricas['progreso_por_repositorio']

# Encontrar próxima acción recomendada
if progreso_global < 10:
    print('### 🏁 Iniciar Traducción')
    print('\`\`\`bash')
    print('/traducir-repo-create context-engineering-intro --prioridad alta --persona-scribe')
    print('\`\`\`')
elif progreso_global < 50:
    # Encontrar repo en progreso
    for repo, data in repos.items():
        if data['estado'] == 'en_progreso':
            print(f'### 🔄 Continuar {repo}')
            print('\`\`\`bash')
            print(f'/validar-terminologia repositorios/{repo}-esp/ --auto-corregir')
            print(f'/revisar-traduccion repositorios/{repo}-esp/ --nivel profesional')
            print('\`\`\`')
            break
elif progreso_global < 80:
    print('### 📊 Revisión de Calidad')
    print('\`\`\`bash')
    print('/revisar-traduccion repositorios/ --nivel enterprise --generar-reporte')
    print('/validar-terminologia repositorios/ --tipo repositorio --exportar json')
    print('\`\`\`')
else:
    print('### ✅ Finalización')
    print('\`\`\`bash')
    print('/generar-reporte --tipo final --incluir-metricas')
    print('/revisar-traduccion repositorios/ --nivel enterprise --sugerir-mejoras')
    print('\`\`\`')

print()
print('### 🔄 Comandos de Mantenimiento Regular')
print('\`\`\`bash')
print('# Actualizar estado (ejecutar semanalmente)')
print('/status-traduccion --formato dashboard --metricas')
print()
print('# Validar calidad (ejecutar después de cada sesión de traducción)')
print('/validar-terminologia repositorios/ --auto-corregir')
print()
print('# Sincronizar con originales (ejecutar mensualmente)')
print('python3 herramientas/sincronizador-versiones.py --update')
print('\`\`\`')
"
```

## Output Formats
```yaml
DASHBOARD: "Vista ejecutiva con métricas visuales y recomendaciones"
RESUMEN: "Resumen conciso del estado actual"
COMPLETO: "Análisis detallado con todas las métricas disponibles"
METRICAS: "Foco en números y KPIs cuantificables"
ROADMAP: "Planificación temporal y próximos pasos"
```

## Personas Auto-activation
- **architect**: Para decisiones estratégicas y roadmap
- **qa**: Para métricas de calidad y estándares
- **scribe**: Para generación de reportes ejecutivos
- **mentor**: Para evaluación de progreso educativo

## Examples
```bash
# Dashboard ejecutivo completo
/status-traduccion --formato dashboard --metricas --roadmap

# Estado específico de repositorio
/status-traduccion --repositorio context-engineering-intro --formato completo

# Exportar métricas para análisis externo
/status-traduccion --exportar json --historico

# Resumen rápido del progreso
/status-traduccion --formato resumen
```