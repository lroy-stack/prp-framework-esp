---
name: commit
description: Analizar cambios y crear un commit git inteligente
arguments: "Instrucciones adicionales para el commit"
---

instrucciones adicionales = $ARGUMENTS

tipo = "feat", "fix", "docs", "style", "refactor", "perf", "test", "chore"

# Commit Git Inteligente PRPs/ai_docs

Por favor ayúdame a crear un commit git:

1. Primero, verificar el estado actual de git y analizar qué cambió:

```bash
git status
git diff --staged
```

2. Si no hay archivos preparados, mostrarme los cambios y ayudarme a decidir qué preparar:

```bash
git diff
git status -s
```

3. Basado en los cambios, sugerir:

- El tipo de commit apropiado (feat/fix/docs/style/refactor/perf/test/chore)
- Un mensaje de commit conciso y descriptivo siguiendo conventional commits
- Si los cambios son complejos, sugerir dividir en múltiples commits

4. El formato del commit debería ser:

$tipo: descripción para commits simples
Para cambios complejos, incluir un cuerpo explicando qué y por qué

5. Después de mostrarme el mensaje de commit sugerido, preguntar si quiero:

- Usarlo tal como está
- Modificarlo
- Agregar más detalles al cuerpo
- Preparar archivos diferentes

6. Una vez aprobado, crear el commit y mostrarme el resultado.

7. Finalmente, preguntar si quiero hacer push o crear un PR.