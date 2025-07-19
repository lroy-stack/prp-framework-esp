# Crear Pull Request

Crear un pull request bien estructurado con descripción y contexto apropiados.

## Título PR (si se proporciona)
$ARGUMENTS

## Proceso

1. **Preparar Rama**
   ```bash
   # Verificar rama actual
   git branch --show-current
   
   # Asegurar que no estamos en main
   # Si estamos en main, crear una rama de funcionalidad
   ```

2. **Revisar Cambios**
   ```bash
   # Ver qué se incluirá
   git status
   git diff main...HEAD
   ```

3. **Crear Commits**
   - Preparar archivos relevantes
   - Crear commits lógicos y atómicos si no se han hecho ya
   - Escribir mensajes de commit claros siguiendo conventional commits, no incluir ninguna referencia a claude, escrito por claude etc:
     - `feat:` para nuevas funcionalidades
     - `fix:` para correcciones de bugs
     - `docs:` para documentación
     - `test:` para pruebas
     - `refactor:` para refactoring

4. **Enviar al Remoto**
   ```bash
   git push -u origin HEAD
   ```

5. **Crear PR**
   ```bash
   gh pr create --title "$ARGUMENTS" --body "$(cat <<'EOF'
   ## Resumen
   [Descripción breve de qué hace este PR]
   
   ## Cambios
   - [Listar cambios clave]
   - [Ser específico]
   
   ## Tipo de Cambio
   - [ ] Corrección de bug
   - [ ] Nueva funcionalidad
   - [ ] Cambio que rompe compatibilidad
   - [ ] Actualización de documentación
   
   ## Testing
   - [ ] Las pruebas pasan localmente
   - [ ] Agregadas nuevas pruebas
   - [ ] Testing manual completado
   
   ## Checklist
   - [ ] El código sigue el estilo del proyecto
   - [ ] Auto-revisado
   - [ ] Documentación actualizada
   - [ ] Sin console.logs o código de debug
   
   ## Screenshots (si aplica)
   [Agregar screenshots para cambios de UI]
   
   ## Contexto Adicional
   [Cualquier información extra que los revisores deberían saber]
   EOF
   )"
   ```

6. **Post-Creación**
   - Agregar etiquetas si es necesario: `gh pr edit --add-label "feature,needs-review"`
   - Solicitar revisores si se conocen
   - Enlazar a issues relacionados

Recordar:
- Mantener PRs enfocados y pequeños
- Proporcionar contexto para revisores
- Probar exhaustivamente antes de crear PR