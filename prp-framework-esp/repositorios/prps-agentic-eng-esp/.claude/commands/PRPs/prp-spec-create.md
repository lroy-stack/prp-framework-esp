# Crear PRP de ESPECIFICACIÓN (Avanzado)

Generar un PRP comprensivo impulsado por especificaciones con objetivos de transformación claros.

## Especificación: $ARGUMENTS

## Proceso de Análisis

1. **Evaluación del Estado Actual**
   - Mapear implementación existente
   - Identificar puntos de dolor
   - Documentar deuda técnica
   - Anotar puntos de integración

2. **Investigación del Estado Deseado**
   - Mejores prácticas para el estado objetivo
   - Ejemplos de implementación
   - Estrategias de migración
   - Evaluación de riesgos
   - Mapeo de dependencias

3. **Clarificación del Usuario**
   - Confirmar objetivos de transformación
   - Prioridad de objetivos
   - Compromisos aceptables

## Generación de PRP

Usando /PRPs/templates/prp_spec.md:

### Documentación de Estados

```yaml
current_state:
  files: [lista de archivos afectados]
  behavior: [cómo funciona ahora]
  issues: [problemas específicos]

desired_state:
  files: [estructura esperada]
  behavior: [funcionalidad objetivo]
  benefits: [mejoras obtenidas]
```

### Objetivos Jerárquicos

1. **Alto Nivel**: Objetivo general de transformación
2. **Nivel Medio**: Hitos principales
3. **Bajo Nivel**: Tareas específicas con validación

### Especificación de Tareas con palabras clave densas en información

#### Palabras clave densas en información:

- MIRROR: Reflejar el estado del código existente para ser reflejado a otro caso de uso
- COPY: Copiar el estado del código existente para ser copiado a otro caso de uso
- ADD: Agregar nuevo código al codebase
- MODIFY: Modificar código existente
- DELETE: Eliminar código existente
- RENAME: Renombrar código existente
- MOVE: Mover código existente
- REPLACE: Reemplazar código existente
- CREATE: Crear nuevo código

#### Ejemplo:

```yaml
task_name:
  action: MODIFY/CREATE
  file: path/to/file
  changes: |
    - Modificaciones específicas
    - Detalles de implementación
    - Con marcadores claros
  validation:
    - command: "comando de prueba"
    - expect: "criterios de éxito"
```

### Estrategia de Implementación

- Identificar dependencias
- Ordenar tareas por prioridad y orden de implementación y lógica de dependencias
- Incluir planes de rollback
- Mejora progresiva

## Puntos de Interacción del Usuario

1. **Validación de Objetivos**
   - Revisar desglose jerárquico
   - Confirmar prioridades
   - Identificar piezas faltantes

2. **Revisión de Riesgos**
   - Documentar riesgos identificados
   - Encontrar mitigaciones
   - Establecer criterios de go/no-go

## Requerimientos de Contexto

- Detalles de implementación actual
- Ejemplos de arquitectura objetivo
- Mejores prácticas de migración
- Estrategias de testing

## Salida

Guardar como: `SPEC_PRP/PRPs/{nombre-spec}.md`

## Checklist de Calidad

- [ ] Estado actual completamente documentado
- [ ] Estado deseado claramente definido
- [ ] Todos los objetivos medibles
- [ ] Tareas ordenadas por dependencia
- [ ] Cada tarea tiene validación que la IA puede ejecutar
- [ ] Riesgos identificados con mitigaciones
- [ ] Estrategia de rollback incluida
- [ ] Puntos de integración anotados

Recuerda: Enfócate en el viaje de transformación, no solo en el destino.