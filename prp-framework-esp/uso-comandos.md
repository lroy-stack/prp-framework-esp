# 🎯 Guía de Comandos - Sistema de Traducción PRP Framework

## 🚀 Instalación de SuperClaude (Prerequisito)

### Opción 1: Desde Código Fuente con Git Clone (MÁS FÁCIL) ⭐
```bash
# Clonar repositorio
git clone https://github.com/NomenAK/SuperClaude.git
cd SuperClaude

# Instalar con uv (recomendado)
uv sync

# O con pip tradicional
pip install -e .

# Ejecutar instalador (cualquiera de estos comandos funciona)
python3 SuperClaude install              # Más directo
python3 -m SuperClaude install           # Alternativa modular
SuperClaude install                      # Si está en PATH
```

### Opción 2: Desde PyPI (Instalación Global)
```bash
# Con uv (moderno y rápido)
uv add SuperClaude

# O con pip tradicional
pip install SuperClaude

# Ejecutar instalador
python3 -m SuperClaude install
```

### Opción 3: Instalación por Proyecto
```bash
# Crear entorno virtual
uv venv
source .venv/bin/activate

# Instalar SuperClaude
uv pip install SuperClaude

# Ejecutar instalador
python3 -m SuperClaude install
```

### Opciones del Instalador
```bash
# Instalación rápida (recomendada)
python3 SuperClaude install

# Selección interactiva de componentes
python3 SuperClaude install --interactive

# Instalación mínima (solo framework core)
python3 SuperClaude install --minimal

# Perfil desarrollador (todo incluido)
python3 SuperClaude install --profile developer

# Ver todas las opciones
python3 SuperClaude install --help
```

## 🎭 Personas de SuperClaude Disponibles

### Personas de Desarrollo
- **`--persona-frontend`**: UI/UX, accesibilidad, componentes React/Vue
- **`--persona-backend`**: APIs, bases de datos, arquitectura servidor
- **`--persona-architect`**: Diseño sistemas, escalabilidad, decisiones arquitectónicas

### Personas de Calidad
- **`--persona-analyzer`**: Análisis causa raíz, debugging, investigación
- **`--persona-security`**: Auditorías seguridad, vulnerabilidades, OWASP
- **`--persona-qa`**: Testing, casos extremos, cobertura de pruebas
- **`--persona-performance`**: Optimización, profiling, métricas

### Personas de Mejora
- **`--persona-refactorer`**: Calidad código, deuda técnica, clean code
- **`--persona-mentor`**: Documentación, tutoriales, transferencia conocimiento
- **`--persona-scribe`**: Documentación técnica especializada (ideal para traducciones)

## 📋 Comandos Slash Disponibles

### Comandos de Ejecución de Traducción

#### `/traducir-repo-execute`
**Propósito**: Ejecutar traducción completa de un repositorio siguiendo su PRP.

```bash
# Ejecutar traducción completa
/traducir-repo-execute [nombre-repositorio] --validar-continuo --actualizar-metricas

# Con opciones avanzadas
/traducir-repo-execute context-engineering-intro --prioridad alta --think-hard --persona-scribe
```

#### `/traducir-archivo-execute`
**Propósito**: Traducir archivos individuales con validación granular.

```bash
# Traducir archivo específico
/traducir-archivo-execute PRPs/traduccion-readme-context-engineering.md --validar-inmediato

# Con backup y validación
/traducir-archivo-execute PRPs/traduccion-servidor-mcp-completa.md --backup --persona-scribe
```

### Comandos de Validación y Control

#### `/validar-terminologia`
**Propósito**: Validar consistencia terminológica contra glosario maestro.

```bash
# Validar directorio completo
/validar-terminologia --directorio repositorios/servidor-mcp-esp/ --reporte

# Validar archivo específico
/validar-terminologia --archivo README-es.md --mostrar-detalles
```

#### `/status-traduccion`
**Propósito**: Ver estado actual del proyecto de traducción.

```bash
# Estado general
/status-traduccion

# Estado específico por framework
/status-traduccion --framework servidor-mcp --detallado
```

### Comandos de Generación y Reportes

#### `/traducir-repo-create`
**Propósito**: Crear PRPs especializados para traducción (ya ejecutado para los 3 frameworks).

```bash
# Para nuevos repositorios futuros
/traducir-repo-create [nuevo-repo] --prioridad alta --persona-scribe
```

#### `/generar-reporte`
**Propósito**: Generar reportes ejecutivos de traducción.

```bash
# Reporte general
/generar-reporte --tipo completo

# Reporte específico
/generar-reporte --framework servidor-mcp --tipo ejecutivo
```

#### `/revisar-traduccion`
**Propósito**: Ejecutar revisión de calidad en traducciones completadas.

```bash
# Revisión completa
/revisar-traduccion --directorio repositorios/servidor-mcp-esp/

# Revisión con sugerencias
/revisar-traduccion --archivo README-es.md --sugerir-mejoras
```

## 🛠️ Herramientas Python

### Sincronizador de Versiones
```bash
# Ver estado actual
python3 herramientas/sincronizador-versiones.py --status

# Actualizar sincronización
python3 herramientas/sincronizador-versiones.py --update

# Framework específico
python3 herramientas/sincronizador-versiones.py --framework servidor-mcp
```

### Validador de Terminología
```bash
# Validar todos los repositorios
python3 herramientas/validador-terminologia.py --verificar-todo

# Estadísticas del glosario
python3 herramientas/validador-terminologia.py --estadisticas

# Generar reporte detallado
python3 herramientas/validador-terminologia.py --directorio repositorios/servidor-mcp-esp/ --reporte validacion.md
```

## 🚀 Workflows Recomendados

### Para Ejecutar Traducciones de PRPs Existentes

```bash
# 1. Verificar estado actual
/status-traduccion

# 2. Ejecutar traducción del PRP deseado con persona especializada
/traducir-archivo-execute PRPs/traduccion-servidor-mcp-completa.md --prioridad alta --think-hard --persona-scribe

# 3. Validar resultados con persona de QA
/validar-terminologia --directorio repositorios/servidor-mcp-esp/ --persona-qa

# 4. Generar reporte con análisis profundo
/generar-reporte --framework servidor-mcp --persona-analyzer
```

### Uso Óptimo de Personas por Tarea

```bash
# Para documentación técnica compleja
/traducir-archivo-execute [archivo] --persona-scribe --think-hard

# Para análisis de arquitectura
/traducir-archivo-execute [archivo] --persona-architect --seq

# Para código con comentarios
/traducir-archivo-execute [archivo] --persona-backend --c7

# Para componentes UI
/traducir-archivo-execute [archivo] --persona-frontend --magic

# Para revisión de seguridad
/revisar-traduccion --archivo [archivo] --persona-security --scan
```

### Para Control de Calidad Continuo

```bash
# Durante traducción
/validar-terminologia --archivo [archivo-actual] --mostrar-detalles

# Al completar sección
/revisar-traduccion --directorio [directorio-actual]

# Estado general
/status-traduccion --detallado
```

## 📊 Estado Actual del Proyecto

### Frameworks con PRPs Listos para Ejecutar
1. ✅ **Context Engineering Intro** - 46% completado
2. ✅ **PRPs Agentic Engineering** - 31% completado  
3. ✅ **SuperClaude Framework** - 0% pendiente
4. ✅ **Servidor MCP** - 100% completado ✨

### PRPs Disponibles para Ejecución
- `PRPs/traduccion-context-engineering-intro-completa.md`
- `PRPs/traduccion-prps-agentic-eng-completa.md`
- `PRPs/traduccion-superclaude-framework-completa.md`
- `PRPs/traduccion-servidor-mcp-completa.md` ✅

## 💡 Tips de Uso

### Ejecución Eficiente con Personas
- **Documentación**: `--persona-scribe` + `--think-hard`
- **Código**: `--persona-backend` o `--persona-frontend` según contexto
- **Arquitectura**: `--persona-architect` + `--seq` para análisis profundo
- **Calidad**: `--persona-qa` + `--validar-inmediato` para validación continua
- **Seguridad**: `--persona-security` para revisión de vulnerabilidades

### Validación Continua
- Validar cada archivo tras traducción con persona apropiada
- Ejecutar validación completa al finalizar directorio
- Generar reportes para revisión posterior con `--persona-analyzer`

### Optimización con SuperClaude
- Usar `--uc` (UltraCompressed) para archivos grandes
- Combinar personas con flags de optimización (`--ultrathink`, `--iterate`)
- Mantener metadatos actualizados con `--actualizar-metricas`
- Aprovechar MCPs especializados:
  - `--c7` para documentación oficial
  - `--seq` para análisis complejo
  - `--magic` para componentes UI
  - `--pup` para testing automatizado

## 🔌 Servidores MCP de SuperClaude

### Context7 (Documentación de Librerías)
- **Uso**: `--c7` para acceder a documentación oficial
- **Ideal para**: Traducir referencias técnicas, APIs, patrones de frameworks
- **Token Cost**: Bajo-Medio

### Sequential (Análisis Complejo)
- **Uso**: `--seq` para razonamiento multi-paso
- **Ideal para**: Arquitectura compleja, análisis profundo, decisiones técnicas
- **Token Cost**: Medio-Alto

### Magic (Componentes UI)
- **Uso**: `--magic` para generar componentes modernos
- **Ideal para**: Traducir documentación de UI/UX, sistemas de diseño
- **Token Cost**: Medio

### Puppeteer/Playwright (Testing)
- **Uso**: `--pup` para automatización y testing
- **Ideal para**: Validar traducciones, testing E2E
- **Token Cost**: Bajo

## 📊 Combinaciones Recomendadas

### Para Traducción de Documentación Técnica
```bash
/traducir-archivo-execute [archivo] --persona-scribe --think-hard --c7
```

### Para Traducción de Arquitectura
```bash
/traducir-archivo-execute [archivo] --persona-architect --seq --ultrathink
```

### Para Traducción de Código con Comentarios
```bash
/traducir-archivo-execute [archivo] --persona-backend --validar-inmediato
```

### Para Revisión Final de Calidad
```bash
/revisar-traduccion --directorio [dir] --persona-qa --persona-analyzer --scan
```

---

## ⚠️ Notas Importantes sobre SuperClaude

### Requisitos Previos
- **Python 3.7+** requerido (verificar con `python3 --version`)
- **Git** para opción de clonación
- **Permisos** para escribir en `~/.claude/`

### Después de Instalar
Una vez instalado SuperClaude, puedes usar cualquiera de estos formatos:
- `SuperClaude [comando]` - Si está en PATH
- `python3 SuperClaude [comando]` - Directo
- `python3 -m SuperClaude [comando]` - Modular

### Comandos SuperClaude vs Comandos de Traducción
- **Comandos SuperClaude**: Empiezan con `/sc:` (ej: `/sc:implement`, `/sc:analyze`)
- **Comandos de Traducción**: Sin prefijo (ej: `/traducir-archivo-execute`, `/validar-terminologia`)
- Ambos tipos funcionan juntos para máxima efectividad

---

**🎯 Inicio Rápido**: 
1. **Instala SuperClaude** (si no lo has hecho):
   ```bash
   git clone https://github.com/NomenAK/SuperClaude.git && cd SuperClaude && uv sync && python3 SuperClaude install
   ```
2. **Ejecuta traducciones** con la persona apropiada:
   ```bash
   /traducir-archivo-execute PRPs/[archivo-prp] --persona-scribe --think-hard
   ```
3. **Aprovecha** las combinaciones de personas + MCPs para traducciones de máxima calidad