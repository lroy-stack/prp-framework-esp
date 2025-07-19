# Crear PRP de PLANIFICACIÓN (Avanzado)

Transformar ideas vagas en PRDs comprensivos con documentación visual rica.

## Idea: $ARGUMENTS

## Proceso de Descubrimiento

1. **Expansión de Concepto**
   - Desglosar la idea central
   - Definir criterios de éxito
   - Mapear a objetivos de negocio si se proporcionan

2. **Investigación de Mercado y Técnica**
   - Hacer búsqueda web profunda para lo siguiente:
     - Análisis de mercado
     - Análisis de competencia
     - Estudio de factibilidad técnica
     - Ejemplos de mejores prácticas
     - Posibilidades de integración

3. **Investigación de Usuarios y Clarificación**
     - Pedir al usuario lo siguiente si no se proporciona:
     - ¿Personas usuarias objetivo?
     - ¿Puntos de dolor clave?
     - ¿Métricas de éxito?
     - ¿Restricciones/requerimientos?

## Generación de PRD

Usando /PRPs/templates/prp_planning_base.md:

### Plan de Documentación Visual
```yaml
diagrams_needed:
  user_flows:
    - Happy path journey
    - Error scenarios
    - Edge cases
  
  architecture:
    - System components
    - Data flow
    - Integration points
  
  sequences:
    - API interactions
    - Event flows
    - State changes
  
  data_models:
    - Entity relationships
    - Schema design
    - State machines
```

### Integración de Investigación
- **Análisis de Mercado**: Incluir hallazgos en PRD
- **Opciones Técnicas**: Comparar enfoques
- **Evaluación de Riesgos**: Con estrategias de mitigación
- **Métricas de Éxito**: Específicas, medibles

### Desarrollo de Historias de Usuario
```markdown
## Epic: [Funcionalidad de alto nivel]

### Historia 1: [Necesidad del usuario]
**Como** [tipo de usuario]
**Quiero** [capacidad]
**Para que** [beneficio]

**Criterios de Aceptación:**
- [ ] Comportamiento específico
- [ ] Manejo de casos extremos
- [ ] Requerimiento de rendimiento

**Notas Técnicas:**
- Enfoque de implementación
- Implicaciones de API
- Requerimientos de datos
```

### Estrategia de Implementación
- Fases con dependencias (sin fechas)
- Ordenamiento por prioridad
- MVP vs funcionalidades mejoradas
- Prerrequisitos técnicos

## Puntos de Interacción del Usuario

1. **Validación de Idea**
   - Confirmar entendimiento
   - Clarificar ambigüedades
   - Establecer límites

2. **Revisión de Investigación**
   - Compartir hallazgos
   - Validar supuestos
   - Ajustar dirección

3. **Revisión de Borrador de PRD**
   - Aprobación de arquitectura
   - Reconocimiento de riesgos
   - Acuerdo de métricas de éxito

## Guías de Diagramas
- Usar Mermaid para todos los diagramas
- Incluir leyendas donde sea necesario
- Mostrar rutas de error
- Anotar flujos complejos

## Estructura de Salida
```markdown
1. Resumen Ejecutivo
2. Problema y Solución
3. Historias de Usuario (con diagramas)
4. Arquitectura Técnica (con diagramas)
5. Especificaciones de API
6. Modelos de Datos
7. Fases de Implementación
8. Riesgos y Mitigaciones
9. Métricas de Éxito
10. Apéndices
```

Guardar como: `PRPs/{nombre-funcionalidad}-prd.md`

## Checklist de Calidad
- [ ] Problema claramente articulado
- [ ] La solución aborda el problema
- [ ] Todos los flujos de usuario diagramados
- [ ] Wireframes incluidos si es necesario
- [ ] Arquitectura visualizada
- [ ] APIs completamente especificadas con ejemplos
- [ ] Modelos de datos incluidos
- [ ] Dependencias identificadas
- [ ] Riesgos identificados y mitigados
- [ ] Métricas de éxito medibles
- [ ] Fases de implementación lógicas
- [ ] Listo para PRP de implementación

Recuerda: Los grandes PRDs previenen confusión de implementación.