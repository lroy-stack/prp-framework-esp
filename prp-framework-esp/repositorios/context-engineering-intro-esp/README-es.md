# Plantilla de Context Engineering

Una plantilla completa para comenzar con Context Engineering - la disciplina de diseñar contexto para asistentes de codificación IA para que tengan la información necesaria para completar el trabajo de extremo a extremo.

> **Context Engineering es 10x mejor que Ingeniería de Prompts y 100x mejor que Vibe Coding.**

## 🚀 Inicio Rápido

```bash
# 1. Clonar esta plantilla
git clone https://github.com/coleam00/Context-Engineering-Intro.git
cd Context-Engineering-Intro

# 2. Configurar las reglas de tu proyecto (opcional - plantilla proporcionada)
# Editar CLAUDE.md para añadir tus directrices específicas del proyecto

# 3. Añadir ejemplos (altamente recomendado)
# Colocar ejemplos de código relevantes en la carpeta examples/

# 4. Crear tu solicitud de funcionalidad inicial
# Editar INITIAL.md con los requisitos de tu funcionalidad

# 5. Generar un PRP (Product Requirements Prompt) comprensivo
# En Claude Code, ejecutar:
/generate-prp INITIAL.md

# 6. Ejecutar el PRP para implementar tu funcionalidad
# En Claude Code, ejecutar:
/execute-prp PRPs/tu-nombre-funcionalidad.md
```

## 📚 Tabla de Contenidos

- [¿Qué es Context Engineering?](#qué-es-context-engineering)
- [Estructura de la Plantilla](#estructura-de-la-plantilla)
- [Guía Paso a Paso](#guía-paso-a-paso)
- [Escribir Archivos INITIAL.md Efectivos](#escribir-archivos-initialmd-efectivos)
- [El Flujo de Trabajo PRP](#el-flujo-de-trabajo-prp)
- [Usar Ejemplos Efectivamente](#usar-ejemplos-efectivamente)
- [Mejores Prácticas](#mejores-prácticas)

## ¿Qué es Context Engineering?

Context Engineering representa un cambio de paradigma respecto a la Ingeniería de Prompts tradicional:

### Ingeniería de Prompts vs Context Engineering

**Ingeniería de Prompts:**
- Se enfoca en redacción inteligente y frases específicas
- Limitado a cómo formulas una tarea
- Como darle a alguien una nota adhesiva

**Context Engineering:**
- Un sistema completo para proporcionar contexto comprensivo
- Incluye documentación, ejemplos, reglas, patrones y validación
- Como escribir un guión completo con todos los detalles

### Por qué Importa Context Engineering

1. **Reduce Fallos de IA**: La mayoría de fallos de agentes no son fallos del modelo - son fallos de contexto
2. **Asegura Consistencia**: La IA sigue los patrones y convenciones de tu proyecto
3. **Habilita Funcionalidades Complejas**: La IA puede manejar implementaciones multi-paso con contexto apropiado
4. **Auto-corrige**: Los bucles de validación permiten que la IA corrija sus propios errores

## Estructura de la Plantilla

```
context-engineering-intro/
├── .claude/
│   ├── commands/
│   │   ├── generate-prp.md    # Genera PRPs comprensivos
│   │   └── execute-prp.md     # Ejecuta PRPs para implementar funcionalidades
│   └── settings.local.json    # Permisos de Claude Code
├── PRPs/
│   ├── templates/
│   │   └── prp_base.md       # Plantilla base para PRPs
│   └── EXAMPLE_multi_agent_prp.md  # Ejemplo de un PRP completo
├── examples/                  # Tus ejemplos de código (¡crítico!)
├── CLAUDE.md                 # Reglas globales para asistente IA
├── INITIAL.md               # Plantilla para solicitudes de funcionalidad
├── INITIAL_EXAMPLE.md       # Ejemplo de solicitud de funcionalidad
└── README.md                # Este archivo
```

Esta plantilla no se enfoca en RAG y herramientas con Context Engineering porque tengo MUCHO más preparado para eso pronto. ;)

## Guía Paso a Paso

### 1. Configurar Reglas Globales (CLAUDE.md)

El archivo `CLAUDE.md` contiene reglas para todo el proyecto que el asistente IA seguirá en cada conversación. La plantilla incluye:

- **Conciencia del proyecto**: Leer documentos de planificación, verificar tareas
- **Estructura de código**: Límites de tamaño de archivo, organización de módulos
- **Requisitos de testing**: Patrones de pruebas unitarias, expectativas de cobertura
- **Convenciones de estilo**: Preferencias de lenguaje, reglas de formato
- **Estándares de documentación**: Formatos de docstring, prácticas de comentarios

**Puedes usar la plantilla proporcionada tal como está o personalizarla para tu proyecto.**

### 2. Crear Tu Solicitud de Funcionalidad Inicial

Edita `INITIAL.md` para describir lo que quieres construir:

```markdown
## FEATURE:
[Describe lo que quieres construir - sé específico sobre funcionalidad y requisitos]

## EXAMPLES:
[Lista cualquier archivo de ejemplo en la carpeta examples/ y explica cómo deben usarse]

## DOCUMENTATION:
[Incluye enlaces a documentación relevante, APIs, o recursos de servidor MCP]

## OTHER CONSIDERATIONS:
[Menciona cualquier gotcha, requisitos específicos, o cosas que los asistentes IA comúnmente pasan por alto]
```

**Ve `INITIAL_EXAMPLE.md` para un ejemplo completo.**

### 3. Generar el PRP

Los PRPs (Product Requirements Prompts) son blueprints de implementación comprensivos que incluyen:

- Contexto completo y documentación
- Pasos de implementación con validación
- Patrones de manejo de errores
- Requisitos de testing

Son similares a los PRDs (Product Requirements Documents) pero están diseñados más específicamente para instruir a un asistente de codificación IA.

Ejecuta en Claude Code:
```bash
/generate-prp INITIAL.md
```

**Nota:** Los Comandos Slash son comandos personalizados definidos en `.claude/commands/`. Puedes ver su implementación:
- `.claude/commands/generate-prp.md` - Ve cómo investiga y crea PRPs
- `.claude/commands/execute-prp.md` - Ve cómo implementa funcionalidades desde PRPs

La variable `$ARGUMENTS` en estos comandos recibe lo que pases después del nombre del comando (ej., `INITIAL.md` o `PRPs/tu-funcionalidad.md`).

Este comando:
1. Lee tu solicitud de funcionalidad
2. Investiga el codebase para patrones
3. Busca documentación relevante
4. Crea un PRP comprensivo en `PRPs/tu-nombre-funcionalidad.md`

### 4. Ejecutar el PRP

Una vez generado, ejecuta el PRP para implementar tu funcionalidad:

```bash
/execute-prp PRPs/tu-nombre-funcionalidad.md
```

El asistente de codificación IA:
1. Lee todo el contexto del PRP
2. Crea un plan de implementación detallado
3. Ejecuta cada paso con validación
4. Ejecuta tests y corrige cualquier problema
5. Asegura que todos los criterios de éxito se cumplan

## Escribir Archivos INITIAL.md Efectivos

### Secciones Clave Explicadas

**FEATURE**: Sé específico y comprensivo
- ❌ "Construir un web scraper"
- ✅ "Construir un web scraper asíncrono usando BeautifulSoup que extrae datos de productos de sitios de e-commerce, maneja rate limiting, y almacena resultados en PostgreSQL"

**EXAMPLES**: Aprovecha la carpeta examples/
- Coloca patrones de código relevantes en `examples/`
- Referencia archivos específicos y patrones a seguir
- Explica qué aspectos deben imitarse

**DOCUMENTATION**: Incluye todos los recursos relevantes
- URLs de documentación de API
- Guías de librerías
- Documentación de servidor MCP
- Esquemas de base de datos

**OTHER CONSIDERATIONS**: Captura detalles importantes
- Requisitos de autenticación
- Límites de rate o cuotas
- Problemas comunes
- Requisitos de rendimiento

## El Flujo de Trabajo PRP

### Cómo Funciona /generate-prp

El comando sigue este proceso:

1. **Fase de Investigación**
   - Analiza tu codebase para patrones
   - Busca implementaciones similares
   - Identifica convenciones a seguir

2. **Recopilación de Documentación**
   - Obtiene documentación de API relevante
   - Incluye documentación de librerías
   - Añade gotchas y peculiaridades

3. **Creación de Blueprint**
   - Crea plan de implementación paso a paso
   - Incluye puertas de validación
   - Añade requisitos de testing

4. **Verificación de Calidad**
   - Puntúa nivel de confianza (1-10)
   - Asegura que todo el contexto está incluido

### Cómo Funciona /execute-prp

1. **Cargar Contexto**: Lee todo el PRP
2. **Planificar**: Crea lista de tareas detallada usando TodoWrite
3. **Ejecutar**: Implementa cada componente
4. **Validar**: Ejecuta tests y linting
5. **Iterar**: Corrige cualquier problema encontrado
6. **Completar**: Asegura que todos los requisitos se cumplan

Ve `PRPs/EXAMPLE_multi_agent_prp.md` para un ejemplo completo de lo que se genera.

## Usar Ejemplos Efectivamente

La carpeta `examples/` es **crítica** para el éxito. Los asistentes de codificación IA funcionan mucho mejor cuando pueden ver patrones a seguir.

### Qué Incluir en Ejemplos

1. **Patrones de Estructura de Código**
   - Cómo organizas módulos
   - Convenciones de importación
   - Patrones de clase/función

2. **Patrones de Testing**
   - Estructura de archivos de test
   - Enfoques de mocking
   - Estilos de assertions

3. **Patrones de Integración**
   - Implementaciones de cliente API
   - Conexiones de base de datos
   - Flujos de autenticación

4. **Patrones de CLI**
   - Parsing de argumentos
   - Formato de output
   - Manejo de errores

### Estructura de Ejemplo

```
examples/
├── README.md           # Explica qué demuestra cada ejemplo
├── cli.py             # Patrón de implementación CLI
├── agent/             # Patrones de arquitectura de agente
│   ├── agent.py      # Patrón de creación de agente
│   ├── tools.py      # Patrón de implementación de herramientas
│   └── providers.py  # Patrón multi-proveedor
└── tests/            # Patrones de testing
    ├── test_agent.py # Patrones de prueba unitaria
    └── conftest.py   # Configuración de Pytest
```

## Mejores Prácticas

### 1. Sé Explícito en INITIAL.md
- No asumas que la IA conoce tus preferencias
- Incluye requisitos específicos y limitaciones
- Referencia ejemplos liberalmente

### 2. Proporciona Ejemplos Comprensivos
- Más ejemplos = mejores implementaciones
- Muestra tanto qué hacer COMO qué no hacer
- Incluye patrones de manejo de errores

### 3. Usa Puertas de Validación
- Los PRPs incluyen comandos de test que deben pasar
- La IA iterará hasta que todas las validaciones tengan éxito
- Esto asegura código funcionando al primer intento

### 4. Aprovecha la Documentación
- Incluye documentación oficial de API
- Añade recursos de servidor MCP
- Referencia secciones específicas de documentación

### 5. Personaliza CLAUDE.md
- Añade tus convenciones
- Incluye reglas específicas del proyecto
- Define estándares de codificación

## Recursos

- [Documentación de Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [Mejores Prácticas de Context Engineering](https://www.philschmid.de/context-engineering)