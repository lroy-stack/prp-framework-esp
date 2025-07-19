claude
** Crear una lista de tareas comprensiva en PRPs/checklist.md para construir nuestro proyecto de hackathon basado en $ARGIMENTS

Ingerir la información luego profundizar en nuestro codebase existente, Cuando esté listo ->

ULTRATHINK sobre la tarea del producto y crear el plan basado en claude.md y crear tareas detalladas siguiendo este principio:

### lista de tareas a completar para cumplir el PRP en el orden que deben completarse usando palabras clave densas en información

 - Ejemplos de palabras clave densas en información:
 ADD, CREATE, MODIFY, MIRROR, FIND, EXECUTE, KEEP, PRESERVE etc

 Marcar tareas hechas con: STATUS [DONE], si no están hechas dejar vacío

```yaml
Tarea 1:
STATUS [ ]
MODIFY src/existing_module.py:
  - FIND pattern: "class OldImplementation"
  - INJECT after line containing "def __init__"
  - PRESERVE existing method signatures

STATUS [ ]
CREATE src/new_feature.py:
  - MIRROR pattern from: src/similar_feature.py
  - MODIFY class name and core logic
  - KEEP error handling pattern identical

...(...)

Tarea N:
...

```

Cada tarea debería tener cobertura de pruebas unitarias, asegurar que las pruebas pasen en cada tarea