# Crear PRP de TAREA (Avanzado)

Generar una lista de tareas comprensiva para cambios enfocados con validación.

## Tarea: $ARGUMENTS

## Proceso de Análisis

1. **Definición de Alcance**
   - Identificar todos los archivos afectados
   - Mapear dependencias
   - Verificar efectos secundarios
   - Anotar cobertura de pruebas

2. **Investigación de Patrones**
   - Encontrar cambios similares en historial
   - Identificar convenciones a seguir
   - Verificar funciones auxiliares
   - Revisar patrones de pruebas

3. **Clarificación del Usuario**
   - Confirmar alcance del cambio
   - Verificar criterios de aceptación
   - Verificar consideraciones de despliegue
   - Identificar bloqueadores

## Generación de PRP

**LEER**
Usando formato TASK_PRP/PRPs/prp_task.md:

### Sección de Contexto

```yaml
context:
  docs:
    - url: [documentación de API]
      focus: [métodos específicos]

  patterns:
    - file: existing/example.py
      copy: [patrón a seguir]

  gotchas:
    - issue: "La librería requiere X"
      fix: "Siempre hacer Y primero"
```

### Estructura de Tareas

```
ACTION path/to/file:
  - OPERATION: [cambio específico]
  - VALIDATE: [comando de prueba]
  - IF_FAIL: [estrategia de debug]
  - ROLLBACK: [enfoque de deshacer]
```

### Secuenciación de Tareas

1. **Tareas de Configuración**: Prerrequisitos
2. **Cambios Core**: Modificaciones principales
3. **Integración**: Conectar componentes
4. **Validación**: Pruebas comprensivas
5. **Limpieza**: Remover código temporal

### Estrategia de Validación

- Prueba unitaria después de cada cambio
- Prueba de integración después de grupos
- Verificación de rendimiento si es relevante
- Escaneo de seguridad para áreas sensibles

## Puntos de Interacción del Usuario

1. **Revisión de Tareas**
   - Confirmar desglose de tareas
   - Validar secuenciación
   - Verificar completitud

2. **Evaluación de Riesgos**
   - Revisar impactos potenciales
   - Confirmar enfoque de rollback
   - Establecer criterios de éxito

## Elementos Críticos

- Incluir patrones de debug
- Agregar verificaciones de rendimiento
- Anotar preocupaciones de seguridad
- Documentar supuestos

## Salida

Guardar como: `TASK_PRP/PRPs/{nombre-tarea}.md`

## Checklist de Calidad

- [ ] Todos los cambios identificados
- [ ] Dependencias mapeadas
- [ ] Cada tarea tiene validación
- [ ] Pasos de rollback incluidos
- [ ] Estrategias de debug proporcionadas
- [ ] Impacto de rendimiento anotado
- [ ] Seguridad verificada
- [ ] No faltan casos extremos

Recuerda: Cambios pequeños y enfocados con validación inmediata.