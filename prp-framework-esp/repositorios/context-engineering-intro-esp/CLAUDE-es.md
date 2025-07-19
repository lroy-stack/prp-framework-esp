### 🔄 Conciencia del Proyecto y Contexto
- **Siempre lee `PLANNING.md`** al inicio de una nueva conversación para entender la arquitectura, objetivos, estilo y limitaciones del proyecto.
- **Verifica `TASK.md`** antes de comenzar una nueva tarea. Si la tarea no está listada, añádela con una breve descripción y la fecha de hoy.
- **Usa convenciones de nomenclatura consistentes, estructura de archivos y patrones de arquitectura** como se describe en `PLANNING.md`.
- **Usa venv_linux** (el entorno virtual) al ejecutar comandos de Python, incluyendo para pruebas unitarias.

### 🧱 Estructura de Código y Modularidad
- **Nunca crees un archivo de más de 500 líneas de código.** Si un archivo se acerca a este límite, refactoriza dividiéndolo en módulos o archivos helper.
- **Organiza el código en módulos claramente separados**, agrupados por funcionalidad o responsabilidad.
  Para agentes esto se ve como:
    - `agent.py` - Definición principal del agente y lógica de ejecución
    - `tools.py` - Funciones de herramientas usadas por el agente
    - `prompts.py` - Prompts del sistema
- **Usa imports claros y consistentes** (prefiere imports relativos dentro de paquetes).
- **Usa imports claros y consistentes** (prefiere imports relativos dentro de paquetes).
- **Usa python_dotenv y load_env()** para variables de entorno.

### 🧪 Testing y Confiabilidad
- **Siempre crea pruebas unitarias de Pytest para nuevas funcionalidades** (funciones, clases, rutas, etc).
- **Después de actualizar cualquier lógica**, verifica si las pruebas unitarias existentes necesitan actualizarse. Si es así, hazlo.
- **Las pruebas deben vivir en una carpeta `/tests`** que refleje la estructura principal de la app.
  - Incluye al menos:
    - 1 prueba para uso esperado
    - 1 caso límite
    - 1 caso de fallo

### ✅ Completitud de Tareas
- **Marca las tareas completadas en `TASK.md`** inmediatamente después de terminarlas.
- Añade nuevas sub-tareas o TODOs descubiertas durante el desarrollo a `TASK.md` bajo una sección "Descubierto Durante el Trabajo".

### 📎 Estilo y Convenciones
- **Usa Python** como lenguaje principal.
- **Sigue PEP8**, usa type hints, y formatea con `black`.
- **Usa `pydantic` para validación de datos**.
- Usa `FastAPI` para APIs y `SQLAlchemy` o `SQLModel` para ORM si es aplicable.
- Escribe **docstrings para cada función** usando el estilo Google:
  ```python
  def example():
      """
      Resumen breve.

      Args:
          param1 (type): Descripción.

      Returns:
          type: Descripción.
      """
  ```

### 📚 Documentación y Explicabilidad
- **Actualiza `README.md`** cuando se añadan nuevas funcionalidades, cambien dependencias, o se modifiquen pasos de configuración.
- **Comenta código no obvio** y asegura que todo sea comprensible para un desarrollador de nivel medio.
- Al escribir lógica compleja, **añade un comentario inline `# Razón:`** explicando el por qué, no solo el qué.

### 🧠 Reglas de Comportamiento IA
- **Nunca asumas contexto faltante. Haz preguntas si no estás seguro.**
- **Nunca alucines librerías o funciones** – solo usa paquetes de Python conocidos y verificados.
- **Siempre confirma que las rutas de archivos y nombres de módulos** existen antes de referenciarlos en código o pruebas.
- **Nunca borres o sobrescribas código existente** a menos que se te instruya explícitamente o si es parte de una tarea de `TASK.md`.