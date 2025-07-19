# Concepto de Product Requirement Prompt (PRP)

"Sobre-especificar qué construir mientras bajo-especificas el contexto, y cómo construirlo, es la razón por la que tantos intentos de codificación impulsados por IA se estancan en el 80%. Un Product Requirement Prompt (PRP) soluciona esto fusionando el alcance disciplinado de un Documento de Requisitos de Producto (PRD) clásico con la mentalidad 'el contexto es rey' de la ingeniería de prompts moderna."

## ¿Qué es un PRP?

Product Requirement Prompt (PRP)
Un PRP es un prompt estructurado que proporciona a un agente de codificación de IA todo lo que necesita para entregar una porción vertical de software funcional—ni más, ni menos.

### Cómo difiere de un PRD

Un PRD tradicional clarifica qué debe hacer el producto y por qué los clientes lo necesitan, pero deliberadamente evita cómo será construido.

Un PRP conserva las secciones de objetivo y justificación de un PRD pero agrega tres capas críticas para IA:

### Contexto

- Rutas de archivo precisas y contenido, versiones de librerías y contexto de librerías, ejemplos de fragmentos de código. Los LLMs generan código de mayor calidad cuando se les dan referencias directas en el prompt en lugar de descripciones amplias. Uso de un directorio ai_docs/ para canalizar documentación de librerías y otra documentación.

### Detalles de Implementación y Estrategia

- En contraste con un PRD tradicional, un PRP establece explícitamente cómo será construido el producto. Esto incluye el uso de endpoints de API, ejecutores de pruebas, o patrones de agente (ReAct, Plan-and-Execute) a utilizar. Uso de anotaciones de tipo, dependencias, patrones arquitectónicos y otras herramientas para asegurar que el código se construya correctamente.

### Puertas de Validación

- Verificaciones determinísticas como pytest, ruff, o pases de tipos estáticos. Los controles de calidad "Shift-left" capturan defectos temprano y son más baratos que el retrabajo tardío.
  Ejemplo: Cada nueva función debe ser probada individualmente, Puerta de validación = todas las pruebas pasan.

### Por Qué Existe la Capa PRP

- La carpeta PRP se usa para preparar y canalizar PRPs al codificador agéntico.

## Por qué el contexto es innegociable

Las salidas de modelos de lenguaje grande están limitadas por su ventana de contexto; el contexto irrelevante o faltante literalmente exprime tokens útiles

El mantra de la industria "Basura Entra → Basura Sale" se aplica doblemente a la ingeniería de prompts y especialmente en ingeniería agéntica: entrada descuidada produce código frágil

## En resumen

Un PRP es PRD + inteligencia de base de código curada + agente/runbook—el paquete mínimo viable que una IA necesita para plausiblemente entregar código listo para producción en el primer intento.

El PRP puede ser pequeño y enfocarse en una sola tarea o grande y cubrir múltiples tareas.
El verdadero poder del PRP está en la capacidad de encadenar tareas juntas en un PRP para construir, auto-validar y entregar características complejas.