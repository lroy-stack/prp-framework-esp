# PRP (Product Requirement prompts)

- Una colección de prompts que uso en mi trabajo diario

## Video Tutorial

👉 https://www.youtube.com/watch?v=KVOZ9s1S9Gk&lc=UgzfwxvFjo6pKEyPo1R4AaABAg

### ☕ Apoya Este Trabajo

**¿Encontraste valor en estos recursos?**

👉 **Cómprame un café:** https://coff.ee/wirasm

Invertí una cantidad considerable de tiempo creando estos recursos y prompts. Si encuentras valor en este proyecto, por favor considera comprarme un café para apoyar mi trabajo.

Eso me ayudará a mantener y mejorar los recursos disponibles de forma gratuita

---

### 🎯 Transforma Tu Equipo con Talleres de Ingeniería de IA

**¿Listo para avanzar más allá de demos de juguete hacia sistemas de IA listos para producción?**

👉 **Reserva un taller:** https://www.rasmuswiding.com/

✅ **Lo que obtendrás:**

- Pon a tu equipo en el camino para convertirse en usuarios avanzados de IA
- Aprende la metodología PRP exacta usada por los mejores equipos de ingeniería
- Entrenamiento práctico con Claude Code, PRPs y bases de código reales
- Desde talleres de ingeniería de IA para principiantes hasta avanzados para equipos e individuos

💡 **Perfecto para:** Equipos de ingeniería, equipos de producto y desarrolladores que quieren IA que realmente funcione en producción

¡Hablemos!
Contáctame directamente en rasmus@widinglabs.com

# Recursos de Ingeniería de IA para Claude Code

Una biblioteca comprensiva de recursos y context engineering para Ingeniería Agéntica, optimizada para Claude Code. Este repositorio proporciona la metodología Product Requirement Prompt (PRP), comandos preconfigurados y documentación extensa para habilitar desarrollo asistido por IA que entrega código listo para producción en el primer intento.

## ¿Qué es PRP?

Product Requirement Prompt (PRP)

## En resumen

Un PRP es PRD + inteligencia curada de la base de código + agente/runbook—el paquete mínimo viable que una IA necesita para plausiblemente entregar código listo para producción en el primer intento.

Product Requirement Prompt (PRP) es una metodología de prompts estructurada establecida por primera vez en el verano de 2024 con context engineering en el corazón. Un PRP proporciona a un agente de codificación de IA todo lo que necesita para entregar una fracción vertical de software funcionando—ni más, ni menos.

### Cómo PRP Difiere del PRD Tradicional

Un PRD tradicional clarifica qué debe hacer el producto y por qué los clientes lo necesitan, pero deliberadamente evita cómo será construido.

Un PRP mantiene las secciones de objetivo y justificación de un PRD pero añade tres capas críticas para IA:

### Contexto

Rutas de archivos precisas y contenido, versiones de bibliotecas y contexto de bibliotecas, ejemplos de fragmentos de código. Los LLMs generan código de mayor calidad cuando se les dan referencias directas en el prompt en lugar de descripciones amplias. Uso de un directorio ai_docs/ para canalizar documentación de bibliotecas y otras.

## Comenzando

### Opción 1: Copiar Recursos a Tu Proyecto Existente

1. **Copia los comandos de Claude** a tu proyecto:

   ```bash
   # Desde la raíz de tu proyecto
   cp -r /path/to/PRPs-agentic-eng/.claude/commands .claude/
   ```

2. **Copia los templates PRP y el runner**:

   ```bash
   cp -r /path/to/PRPs-agentic-eng/PRPs/templates PRPs/
   cp -r /path/to/PRPs-agentic-eng/PRPs/scripts PRPs/
   cp /path/to/PRPs-agentic-eng/PRPs/README.md PRPs/
   ```

3. **Copia la documentación de IA** (opcional pero recomendado):
   ```bash
   cp -r /path/to/PRPs-agentic-eng/PRPs/ai_docs PRPs/
   ```

### Opción 2: Clonar e Iniciar un Nuevo Proyecto

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/Wirasm/PRPs-agentic-eng.git
   cd PRPs-agentic-eng
   ```

2. **Crea la estructura de tu proyecto**:

   ```bash
   # Ejemplo para un proyecto Python
   mkdir -p src/tests
   touch src/__init__.py
   touch pyproject.toml
   touch CLAUDE.md
   ```

3. **Inicializa con UV** (para proyectos Python):
   ```bash
   uv venv
   uv sync
   ```

## Usando Comandos de Claude

El directorio `.claude/commands/` contiene 12 comandos preconfigurados que aparecen como comandos slash en Claude Code.

### Comandos Disponibles

1. **Creación y Ejecución de PRP**:
   - `/create-base-prp` - Generar PRPs comprensivos con investigación
   - `/execute-base-prp` - Ejecutar PRPs contra la base de código
   - `/planning-create` - Crear documentos de planificación con diagramas
   - `/spec-create-adv` - Creación avanzada de especificaciones
   - `/spec-execute` - Ejecutar especificaciones

2. **Revisión de Código y Refactorización**:
   - `/review-general` - Revisión general de código
   - `/review-staged-unstaged` - Revisar cambios de git
   - `/refactor-simple` - Tareas simples de refactorización

3. **Git y GitHub**:
   - `/create-pr` - Crear pull requests

4. **Utilidades**:
   - `/prime-core` - Preparar Claude con contexto del proyecto
   - `/onboarding` - Proceso de incorporación para nuevos miembros del equipo
   - `/debug` - Flujo de trabajo de debugging

### Cómo Usar los Comandos

1. **En Claude Code**, escribe `/` para ver los comandos disponibles
2. **Selecciona un comando** y proporciona argumentos cuando se solicite
3. **Ejemplo de uso**:
   ```
   /create-base-prp sistema de autenticación de usuario con OAuth2
   ```

## Usando PRPs

### Creando un PRP

1. **Usa el template** como punto de partida:

   ```bash
   cp PRPs/templates/prp_base.md PRPs/mi-funcionalidad.md
   ```

2. **Completa las secciones**:
   - Objetivo: Qué necesita ser construido
   - Por qué: Valor de negocio e impacto del usuario
   - Contexto: Documentación, ejemplos de código, problemas conocidos
   - Blueprint de Implementación: Tareas y pseudocódigo
   - Bucle de Validación: Pruebas ejecutables

3. **O usa Claude para generar uno**:
   ```
   /create-base-prp implementar autenticación de usuario con tokens JWT
   ```

### Ejecutando un PRP

1. **Usando el script runner**:

   ```bash
   # Modo interactivo (recomendado para desarrollo)
   uv run PRPs/scripts/prp_runner.py --prp mi-funcionalidad --interactive

   # Modo headless (para CI/CD)
   uv run PRPs/scripts/prp_runner.py --prp mi-funcionalidad --output-format json

   # JSON streaming (para monitoreo en tiempo real)
   uv run PRPs/scripts/prp_runner.py --prp mi-funcionalidad --output-format stream-json
   ```

2. **Usando comandos de Claude**:
   ```
   /execute-base-prp PRPs/mi-funcionalidad.md
   ```

### Mejores Prácticas de PRP

1. **El Contexto es Rey**: Incluye TODA la documentación necesaria, ejemplos y advertencias
2. **Bucles de Validación**: Proporciona pruebas/lints ejecutables que la IA puede ejecutar y corregir
3. **Denso en Información**: Usa palabras clave y patrones de la base de código
4. **Éxito Progresivo**: Comienza simple, valida, luego mejora

### Ejemplo de Estructura PRP

```markdown
## Objetivo

Implementar autenticación de usuario con tokens JWT

## Por qué

- Habilitar sesiones seguras de usuario
- Soportar autenticación de API
- Reemplazar autenticación básica con estándar de la industria

## Qué

Sistema de autenticación basado en JWT con login, logout y renovación de tokens

### Criterios de Éxito

- [ ] Los usuarios pueden hacer login con email/contraseña
- [ ] Los tokens JWT expiran después de 24 horas
- [ ] Los tokens de renovación funcionan correctamente
- [ ] Todos los endpoints están debidamente asegurados

## Todo el Contexto Necesario

### Documentación y Referencias

- url: https://jwt.io/introduction/
  por qué: Estructura JWT y mejores prácticas

- file: src/auth/basic_auth.py
  por qué: Patrón de autenticación actual a reemplazar

- doc: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
  sección: OAuth2 with Password and JWT

### Problemas Conocidos

# CRÍTICO: Usar algoritmo RS256 para producción

# CRÍTICO: Almacenar tokens de renovación en cookies httpOnly

# CRÍTICO: Implementar lista negra de tokens para logout

## Blueprint de Implementación

[... plan de implementación detallado ...]

## Bucle de Validación

### Nivel 1: Sintaxis y Estilo

ruff check src/ --fix
mypy src/

### Nivel 2: Pruebas Unitarias

uv run pytest tests/test_auth.py -v

### Nivel 3: Prueba de Integración

curl -X POST http://localhost:8000/auth/login \
 -H "Content-Type: application/json" \
 -d '{"email": "test@example.com", "password": "testpass"}'
```

## Recomendaciones de Estructura del Proyecto

```
tu-proyecto/
|-- .claude/
|   |-- commands/          # Comandos de Claude Code
|   `-- settings.json      # Permisos de herramientas
|-- PRPs/
|   |-- templates/         # Templates PRP
|   |-- scrips/           # Runner PRP
|   |-- ai_docs/          # Documentación de bibliotecas
|   |-- completed/        # PRPs finalizados
|   `-- *.md              # PRPs activos
|-- CLAUDE.md             # Guías específicas del proyecto
|-- src/                  # Tu código fuente
`-- tests/                # Tus pruebas
```

## Configurando CLAUDE.md

Crea un archivo `CLAUDE.md` en la raíz de tu proyecto con:

1. **Principios Core**: KISS, YAGNI, etc.
2. **Estructura de Código**: Límites de tamaño de archivo, longitud de función
3. **Arquitectura**: Cómo está organizado tu proyecto
4. **Testing**: Patrones de prueba y requisitos
5. **Convenciones de Estilo**: Guías específicas del lenguaje
6. **Comandos de Desarrollo**: Cómo ejecutar pruebas, lint, etc.

Ve el ejemplo CLAUDE.md en este repositorio para un template comprensivo.

## Uso Avanzado

### Ejecutando Múltiples Sesiones de Claude

Usa Git worktrees para desarrollo paralelo:

```bash
git worktree add -b feature-auth ../proyecto-auth
git worktree add -b feature-api ../proyecto-api

# Ejecuta Claude en cada worktree
cd ../proyecto-auth && claude
cd ../proyecto-api && claude
```

### Integración CI/CD

Usa el runner PRP en modo headless:

```yaml
# Ejemplo de GitHub Actions
- name: Execute PRP
  run: |
    uv run PRPs/scripts/prp_runner.py \
      --prp implement-feature \
      --output-format json > result.json
```

### Comandos Personalizados

Crea tus propios comandos en `.claude/commands/`:

```markdown
# .claude/commands/mi-comando.md

# Mi Comando Personalizado

Hacer algo específico para mi proyecto.

## Arguments: $ARGUMENTS

[Tu implementación del comando]
```

## Recursos Incluidos

### Documentación (PRPs/ai_docs/)

- `cc_base.md` - Documentación core de Claude Code
- `cc_actions_sdk.md` - Integración de GitHub Actions y SDK
- `cc_best_practices.md` - Guía de mejores prácticas
- `cc_settings.md` - Configuración y seguridad
- `cc_tutorials.md` - Tutoriales paso a paso

### Templates (PRPs/templates/)

- `prp_base.md` - Template PRP comprensivo con validación
- `prp_spec.md` - Template de especificación
- `prp_planning_base.md` - Template de planificación con diagramas

### Ejemplo PRP

- `example-from-workshop-mcp-crawl4ai-refactor-1.md` - Ejemplo de refactorización del mundo real

## Licencia

MIT License

## Soporte

Invertí una cantidad considerable de tiempo creando estos recursos y prompts. Si encuentras valor en este proyecto, por favor considera comprarme un café para apoyar mi trabajo.

👉 **Cómprame un café:** https://coff.ee/wirasm

---

Recuerda: El objetivo es el éxito de implementación en un solo intento a través de contexto comprensivo. ¡Feliz codificación con Claude Code!