# CLAUDE.md - Guía del Sistema de Traducción PRP Framework

Este archivo proporciona orientación a Claude Code (claude.ai/code) al trabajar con el sistema de traducción del PRP Framework al español.

## 🎯 Visión General del Proyecto

Este es el **Sistema de Traducción e Infraestructura del PRP Framework al Español** - un sistema integral para traducir y localizar el ecosistema completo del PRP Framework al español. El proyecto utiliza herramientas de automatización Python, metodología de Context Engineering y el framework SuperClaude para garantizar calidad, consistencia y mantenibilidad en las traducciones.

### Objetivo Principal
Hacer accesible a la comunidad hispanohablante las metodologías avanzadas de ingeniería de prompts, desarrollo asistido por IA y arquitecturas enterprise del ecosistema PRP, manteniendo la máxima fidelidad técnica y adaptación cultural apropiada.

## 🏗️ Arquitectura del Sistema

### Componentes Principales

```
prp-framework-esp/
├── 📁 herramientas/          # Scripts Python de automatización
│   ├── sincronizador-versiones.py    # Sincronización y tracking
│   └── validador-terminologia.py      # Validación de consistencia
├── 📁 repositorios/          # Contenido traducido por framework
│   ├── context-engineering-intro-esp/
│   ├── prps-agentic-eng-esp/
│   ├── superclaude-framework-esp/
│   └── servidor-mcp-esp/
├── 📁 configuracion/         # Sistema de configuración
│   ├── glosario-maestro.json         # Terminología oficial
│   ├── reglas-traduccion.yaml        # Estándares de traducción
│   └── mapeo-archivos.json           # Mapeo origen-destino
├── 📁 PRPs/                  # Product Requirement Prompts
│   ├── traduccion-context-engineering-intro-completa.md
│   ├── traduccion-prps-agentic-eng-completa.md
│   ├── traduccion-superclaude-framework-completa.md
│   └── traduccion-servidor-mcp-completa.md
├── 📁 metadatos/            # Estado y métricas del proyecto
│   ├── estado-general.json           # Estado global actualizado
│   └── metricas-baseline.json        # Métricas de calidad
├── 📁 flujos-trabajo/       # Documentación de procesos
├── 📁 informes-ejecutivos/  # Reportes de progreso
└── 📁 .claude/commands/     # Comandos slash especializados
```

### Herramientas de Traducción

**Scripts Principales**:
- `sincronizador-versiones.py` - Sincroniza con repositorios originales, rastrea cambios y actualiza estado
- `validador-terminologia.py` - Valida consistencia terminológica usando glosario maestro especializado

**Comandos Slash Especializados**:
- `/traducir-repo-execute` - Ejecuta traducción completa de repositorio
- `/traducir-archivo-execute` - Traduce archivos individuales con validación
- `/validar-terminologia` - Valida consistencia contra glosario
- `/status-traduccion` - Muestra estado actual del proyecto
- `/generar-reporte` - Genera reportes ejecutivos
- `/revisar-traduccion` - Revisión de calidad

## 🛠️ Comandos de Desarrollo

### Flujo de Trabajo de Traducción
```bash
# Sincronizar con repositorios originales
python3 herramientas/sincronizador-versiones.py --update

# Verificar estado del sistema
python3 herramientas/sincronizador-versiones.py --status

# Validar terminología en archivos traducidos
python3 herramientas/validador-terminologia.py --archivo archivo-es.md

# Validar todos los repositorios
python3 herramientas/validador-terminologia.py --verificar-todo

# Mostrar estadísticas del glosario
python3 herramientas/validador-terminologia.py --estadisticas
```

### Control de Calidad
```bash
# Generar reporte de validación
python3 herramientas/validador-terminologia.py --directorio repositorios/context-engineering-intro-esp/ --reporte reporte.md

# Comparar archivos original y traducido
python3 herramientas/sincronizador-versiones.py --comparar README.md README-es.md
```

### Comandos de Traducción con SuperClaude
```bash
# Traducción con persona especializada
/traducir-archivo-execute PRPs/traduccion-[framework].md --persona-scribe --think-hard

# Validación con persona de QA
/validar-terminologia --directorio repositorios/[framework]-esp/ --persona-qa

# Revisión de arquitectura
/revisar-traduccion --archivo [archivo] --persona-architect --seq
```

## ⚙️ Sistema de Configuración

### Glosario Maestro
- **Ubicación**: `configuracion/glosario-maestro.json`
- **Propósito**: Define qué términos traducir vs preservar en idioma original
- **Uso**: Validación automática de consistencia terminológica
- **Términos**: 45+ términos técnicos especializados

### Reglas de Traducción
- **Ubicación**: `configuracion/reglas-traduccion.yaml`
- **Contenido**: Estándares integrales de traducción
- **Patrones**: Preservación de código, enlaces y términos técnicos
- **Adaptaciones**: Estándares culturales y de formato

### Mapeo de Archivos
- **Ubicación**: `configuracion/mapeo-archivos.json`
- **Función**: Mapea archivos fuente a destinos de traducción
- **Tracking**: Relaciones entre contenido original y traducido

## 📊 Estándares de Calidad

### Requisitos de Validación
- **Consistencia terminológica**: ≥95% precisión contra glosario maestro
- **Preservación de estructura**: 100% mantenimiento del formato Markdown
- **Funcionalidad del código**: 100% preservación de ejemplos y comandos
- **Integridad de enlaces**: Todos los enlaces internos y externos funcionales

### Principios de Traducción
1. **Preservar términos técnicos** según glosario maestro
2. **Mantener estructura Markdown** y formato exacto
3. **Mantener bloques de código inalterados** excepto comentarios cuando claramente marcado
4. **Adaptar ejemplos culturalmente** cuando sea relevante (empresas, ubicaciones)
5. **Usar terminología consistente** en todas las traducciones
6. **Aplicar Context Engineering** para máxima precisión contextual

## 🚀 Frameworks en Traducción

### 1. Context Engineering Intro ✅ (46% completado)
- **Descripción**: Template fundacional para ingeniería de contexto
- **Archivos**: 13 totales, 6 traducidos
- **Prioridad**: Alta - Base metodológica
- **Estado**: En progreso activo

### 2. PRPs Agentic Engineering ✅ (31% completado)
- **Descripción**: Colección profesional de prompts
- **Archivos**: 70 totales, 22 traducidos
- **Prioridad**: Alta - Valor práctico inmediato
- **Estado**: En progreso

### 3. SuperClaude Framework 🟡 (0% pendiente)
- **Descripción**: Sistema avanzado de comandos y personas IA
- **Archivos**: 38 totales, 0 traducidos
- **Prioridad**: Media - Framework avanzado
- **Estado**: Pendiente

### 4. Servidor MCP ✅ (100% COMPLETADO)
- **Descripción**: Servidor Model Context Protocol con OAuth
- **Archivos**: 9 archivos críticos traducidos
- **Prioridad**: Alta - Infraestructura técnica
- **Estado**: ¡Completado exitosamente!

## 🎭 Integración con SuperClaude

### Personas Recomendadas para Traducción
- **`--persona-scribe`**: Para documentación técnica compleja
- **`--persona-architect`**: Para decisiones de arquitectura
- **`--persona-backend`**: Para código y comentarios técnicos
- **`--persona-qa`**: Para validación y control de calidad
- **`--persona-analyzer`**: Para análisis profundo y reportes

### Servidores MCP Útiles
- **`--c7`**: Acceso a documentación oficial de librerías
- **`--seq`**: Análisis complejo multi-paso
- **`--magic`**: Componentes UI y diseño
- **`--pup`**: Testing y validación automatizada

## 📈 Gestión de Estado

### Tracking del Proyecto
- **`metadatos/estado-general.json`**: Estado global y progreso actualizado en tiempo real
- **`metadatos/metricas-baseline.json`**: Métricas de calidad y líneas base
- **Actualización automática**: Por herramientas de sincronización y validación

### Estado Actual (Actualizado)
- **Archivos identificados totales**: 142
- **Archivos traducidos**: 38 (servidor MCP: 9, context-eng: 6, prps: 22, superclaude: 0)
- **Progreso de traducción**: ~27% global
- **Herramientas desarrolladas**: Infraestructura completa operativa

## 💡 Guías de Desarrollo

### Trabajo con Herramientas de Traducción
- Siempre ejecutar `--status` antes de comenzar para entender estado actual
- Usar herramientas de validación durante el proceso, no solo al final
- Actualizar glosario maestro al encontrar nuevos términos técnicos
- Ejecutar validación completa antes de commitear contenido traducido
- Usar personas apropiadas de SuperClaude para cada tipo de contenido

### Contribuciones de Código
- Seguir patrones Python existentes en `herramientas/`
- Mantener manejo integral de errores y logging
- Usar type hints y dataclasses para estructuras complejas
- Incluir parsing de argumentos CLI para todos los scripts
- Documentar en español todos los comentarios y docstrings

### Convenciones de Nomenclatura
- Original: `filename.md`
- Traducido: `filename-es.md`
- Reportes: Usar nombres descriptivos con timestamps
- Configuración: Usar kebab-case con propósitos claros
- PRPs: `traduccion-[framework]-completa.md`

## 🔧 Manejo de Errores

### Problemas Comunes
- **Inconsistencias terminológicas**: Usar herramientas de validación para identificar y resolver
- **Enlaces rotos**: Verificar referencias internas y URLs externas
- **Cambios de estructura**: Comparar con original usando herramientas de sincronización
- **Problemas de codificación**: Asegurar codificación UTF-8 para todo contenido en español

### Solución de Problemas
- Revisar logs para información detallada de errores
- Usar flag `--estadisticas` para entender cobertura del glosario
- Validar incrementalmente durante proceso de traducción
- Usar herramientas de comparación para identificar diferencias estructurales
- Aprovechar personas de SuperClaude para análisis profundo

## 🎯 Metodología de Trabajo

### Context Engineering Aplicado
1. **Análisis completo** del repositorio antes de traducir
2. **Identificación de patrones** técnicos y culturales
3. **Mapeo de dependencias** entre archivos
4. **Validación continua** durante el proceso
5. **Adaptación cultural** sin pérdida de precisión técnica

### Flujo de Trabajo Recomendado
1. **Preparación**: Sincronizar y analizar estado
2. **Planificación**: Revisar PRP específico del framework
3. **Ejecución**: Traducir con persona apropiada
4. **Validación**: Verificar con herramientas automáticas
5. **Revisión**: Control de calidad con persona QA
6. **Documentación**: Actualizar métricas y reportes

## 🚀 Valor del Proyecto

### Impacto Esperado
- **Accesibilidad**: Metodologías enterprise disponibles en español
- **Adopción**: Acelerar uso de IA en desarrollo hispanohablante
- **Calidad**: Estándares profesionales de traducción técnica
- **Escalabilidad**: Sistema reutilizable para futuros frameworks

### ROI Proyectado
- **Tiempo ahorrado**: 40% reducción vs traducción manual
- **Calidad mejorada**: 95%+ consistencia terminológica
- **Alcance ampliado**: ~500M hispanohablantes potenciales
- **Valor educativo**: Transferencia de conocimiento avanzado

---

**📝 Nota**: Este sistema aplica las mejores prácticas de Context Engineering, metodología PRP y el framework SuperClaude para garantizar traducciones de máxima calidad técnica y valor educativo para la comunidad hispanohablante.