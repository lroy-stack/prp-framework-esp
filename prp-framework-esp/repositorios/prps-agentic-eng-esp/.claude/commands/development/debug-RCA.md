# Debugear Problema

Debugear y diagnosticar sistemáticamente el problema reportado.

## Descripción del Problema

$ARGUMENTS

## Proceso de Debugging

1. **Reproducir el Problema**
   - Obtener pasos exactos para reproducir
   - Verificar que puedes ver el mismo problema
   - Anotar cualquier mensaje de error o logs
   - Documentar el comportamiento esperado vs real

2. **Recopilar Información**

   ```bash
   # Verificar cambios recientes
   git log --oneline -10

   # Buscar patrones de error en logs
   # Buscar mensajes de error relacionados
   ```

3. **Aislar el Problema**
   - **Búsqueda Binaria**: Comentar secciones de código para reducir el alcance
   - **Git Bisect**: Encontrar cuándo fue introducido el bug
   - **Logging**: Agregar declaraciones de log estratégicas
   - **Debugger**: Establecer breakpoints si es aplicable

4. **Estrategias Comunes de Debugging**

   ### Para Errores de Runtime
   - Leer el stack trace completo
   - Identificar la línea exacta que causa el error
   - Verificar valores de variables en ese punto
   - Verificar supuestos sobre tipos de datos

   ### Para Errores de Lógica
   - Agregar declaraciones print/log para rastrear ejecución
   - Verificar que cada paso produce resultados esperados
   - Verificar condiciones de frontera
   - Probar con ejemplo mínimo reproducible

   ### Para Problemas de Rendimiento
   - Agregar mediciones de tiempo
   - Verificar consultas N+1
   - Buscar algoritmos ineficientes
   - Hacer profiling si es necesario

   ### Para Problemas de Integración
   - Verificar que el servicio externo es accesible
   - Verificar autenticación/credenciales
   - Validar formatos de request/response
   - Probar con curl/Postman primero

5. **Análisis de Causa Raíz**
   - ¿Por qué pasó esto?
   - ¿Por qué no fue detectado antes?
   - ¿Hay problemas similares en otros lugares?
   - ¿Cómo podemos prevenir esta clase de bugs?

6. **Implementar Corrección**
   - Corregir la causa raíz, no solo los síntomas
   - Agregar programación defensiva si es necesario
   - Considerar casos extremos
   - Mantener la corrección mínima y enfocada, seguir KISS

7. **Verificar Resolución**
   - Confirmar que el problema original está corregido
   - Verificar que no hay regresión
   - Probar funcionalidad relacionada
   - Agregar prueba para prevenir recurrencia

8. **Documentar Hallazgos**

   ```markdown
   ## Resumen de Debug

   ### Problema

   [Qué estaba roto]

   ### Causa Raíz

   [Por qué estaba roto]

   ### Corrección

   [Qué fue cambiado]

   ### Prevención

   [Cómo evitar problemas similares]
   ```

## Checklist de Debug

- [ ] Problema reproducido localmente
- [ ] Causa raíz identificada
- [ ] Corrección implementada
- [ ] Pruebas agregadas/actualizadas
- [ ] No se introdujeron regresiones
- [ ] Documentación actualizada si es necesario

Recordar: El objetivo no es solo corregir el bug, sino entender por qué pasó y prevenir problemas similares en el futuro.