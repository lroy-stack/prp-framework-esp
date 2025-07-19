# Crear PRP BASE

## Funcionalidad: $ARGUMENTS

Generar un PRP completo para implementación de funcionalidades con investigación profunda y exhaustiva. Asegurar que se pase contexto rico a la IA a través del PRP para permitir éxito de implementación en una sola pasada mediante auto-validación y refinamiento iterativo.

El agente de IA solo obtiene el contexto que estás agregando al PRP y sus propios datos de entrenamiento. Asume que el agente de IA tiene acceso al codebase y el mismo corte de conocimiento que tú, por lo que es importante que tus hallazgos de investigación estén incluidos o referenciados en el PRP. El Agente tiene capacidades de Websearch, así que pasa URLs a documentación y ejemplos.

## Proceso de Investigación

> Durante el proceso de investigación, crea tareas claras y genera tantos agentes y subagentes como sea necesario usando las herramientas batch. Mientras más profunda sea la investigación que hagamos aquí, mejor será el PRP. Optimizamos para probabilidad de éxito y no para velocidad.

1. **Análisis de Codebase en profundidad**
   - Crear todos claros y generar subagentes para buscar en el codebase funcionalidades/patrones similares. Piensa profundamente y planifica tu enfoque
   - Identificar todos los archivos necesarios para referenciar en el PRP
   - Anotar todas las convenciones existentes a seguir
   - Verificar patrones de pruebas existentes para enfoque de validación
   - Usar las herramientas batch para generar subagentes que busquen en el codebase funcionalidades/patrones similares

2. **Investigación Externa a escala**
   - Crear todos claros y generar con instrucciones subagentes para hacer investigación profunda de funcionalidades/patrones similares en línea e incluir urls a documentación y ejemplos
   - Documentación de librerías (incluir URLs específicas)
   - Para piezas críticas de documentación, agregar un archivo .md a PRPs/ai_docs y referenciarlo en el PRP con razonamiento claro e instrucciones
   - Ejemplos de implementación (GitHub/StackOverflow/blogs)
   - Mejores prácticas y errores comunes encontrados durante la investigación
   - Usar las herramientas batch para generar subagentes que busquen funcionalidades/patrones similares en línea e incluir urls a documentación y ejemplos

3. **Clarificación de Usuario**
   - Pedir clarificación si la necesitas

## Generación de PRP

Usando PRPs/templates/prp_base.md como plantilla:

### Contexto Crítico mínimo a Incluir y pasar al agente de IA como parte del PRP

- **Documentación**: URLs con secciones específicas
- **Ejemplos de Código**: Fragmentos reales del codebase
- **Gotchas**: Peculiaridades de librerías, problemas de versión
- **Patrones**: Enfoques existentes a seguir
- **Mejores Prácticas**: Errores comunes encontrados durante la investigación

### Blueprint de Implementación

- Comenzar con pseudocódigo mostrando el enfoque
- Referenciar archivos reales para patrones
- Incluir estrategia de manejo de errores
- Listar tareas a completar para cumplir el PRP en el orden que deben completarse, usar el patrón en el PRP con palabras clave densas en información

### Puertas de Validación (Deben ser Ejecutables por el agente de IA)

```bash
# Sintaxis/Estilo
ruff check --fix && mypy .

# Pruebas Unitarias
uv run pytest tests/ -v

```

Mientras más puertas de validación, mejor, pero asegúrate de que sean ejecutables por el agente de IA.
Incluye pruebas, servidores mcp, y cualquier otra puerta de validación relevante. Sé creativo con las puertas de validación.

**_ CRÍTICO DESPUÉS DE QUE TERMINES DE INVESTIGAR Y EXPLORAR EL CODEBASE ANTES DE EMPEZAR A ESCRIBIR EL PRP _**

**_ ULTRATHINK SOBRE EL PRP Y PLANIFICA TU ENFOQUE EN TODOS DETALLADOS LUEGO EMPIEZA A ESCRIBIR EL PRP _**

## Salida

Guardar como: `PRPs/{nombre-funcionalidad}.md`

## Checklist de Calidad

- [ ] Todo el contexto necesario incluido
- [ ] Las puertas de validación son ejecutables por IA
- [ ] Referencias a patrones existentes
- [ ] Ruta de implementación clara
- [ ] Manejo de errores documentado

Califica el PRP en una escala del 1-10 (nivel de confianza para tener éxito en implementación de una sola pasada usando claude codes)

Recuerda: El objetivo es éxito de implementación en una sola pasada a través de contexto comprensivo.