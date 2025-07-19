# Concepto de Product Requirement Prompt (PRP)

"Sobre-especificar qué construir mientras sub-especificas el contexto, y cómo construirlo, es por qué tantos intentos de codificación impulsados por IA se estancan en el 80%. Un Product Requirement Prompt (PRP) arregla eso fusionando el alcance disciplinado de un Documento de Requisitos de Producto (PRD) clásico con la mentalidad de 'el contexto es rey' de la ingeniería de prompts moderna."

## ¿Qué es un PRP?

Product Requirement Prompt (PRP)
Un PRP es un prompt estructurado que proporciona a un agente de codificación IA todo lo que necesita para entregar una rebanada vertical de software funcional—ni más, ni menos.

### Cómo difiere de un PRD

Un PRD tradicional clarifica qué debe hacer el producto y por qué los clientes lo necesitan, pero deliberadamente evita cómo será construido.

Un PRP mantiene las secciones de objetivo y justificación de un PRD pero agrega tres capas críticas para IA:

### Contexto

- Rutas de archivos precisas y contenido, versiones de librerías y contexto de librerías, ejemplos de fragmentos de código. Los LLMs generan código de mayor calidad cuando se les dan referencias directas en el prompt en lugar de descripciones amplias. Uso de un directorio ai_docs/ para canalizar docs de librerías y otros.

### Detalles de Implementación y Estrategia

- En contraste con un PRD tradicional, un PRP explícitamente establece cómo será construido el producto. Esto incluye el uso de endpoints API, ejecutores de pruebas, o patrones de agente (ReAct, Plan-and-Execute) a usar. Uso de typehints, dependencias, patrones arquitectónicos y otras herramientas para asegurar que el código sea construido correctamente.

### Puertas de Validación

- Verificaciones determinísticas como pytest, ruff, o pasos de tipos estáticos "Shift-left" los controles de calidad capturan defectos temprano y son más baratos que re-trabajo tardío.
  Ejemplo: Cada nueva función debe ser probada individualmente, Puerta de validación = todas las pruebas pasan.

### Capa PRP Por Qué Existe

- La carpeta PRP se usa para preparar y canalizar PRPs al codificador agéntico.

## Por qué el contexto es no-negociable

Las salidas de modelos de lenguaje grande están limitadas por su ventana de contexto; el contexto irrelevante o faltante literalmente exprime tokens útiles

El mantra de la industria "Basura Entra → Basura Sale" aplica doblemente a la ingeniería de prompts y especialmente en ingeniería agéntica: entrada descuidada produce código frágil

## En resumen

Un PRP es PRD + inteligencia curada de codebase + agente/runbook—el paquete mínimo viable que una IA necesita para entregar código listo para producción en el primer intento.

El PRP puede ser pequeño y enfocarse en una sola tarea o grande y cubrir múltiples tareas.
El verdadero poder del PRP está en la habilidad de encadenar tareas juntas en un PRP para construir, auto-validar y entregar funcionalidades complejas.