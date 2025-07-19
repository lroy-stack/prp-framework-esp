# Requerimientos Iniciales - Servidor MCP PRP

## CARACTERÍSTICA:

Queremos crear un servidor MCP usando la plantilla de este repositorio

El objetivo del servidor MCP es crear una versión simple del taskmaster mcp que en lugar de parsear PRDs parseamos PRPs.

Características adicionales:

- Extracción de información PRP impulsada por LLM usando Anthropic
- Operaciones CRUD en tareas, documentación, etiquetas, etc. hacia y desde la BD

Necesitamos herramientas para parsear PRPs. Esta herramienta debe tomar un PRP completo y usar Anthropic para extraer las tareas en tareas y guardarlas en la base de datos, incluyendo documentación circundante del PRP como los objetivos, los por qué, usuarios objetivo, etc.

Necesitamos:

- Poder realizar operaciones CRUD en tareas, documentación, etiquetas, etc.
- Herramienta de obtención de tareas para conseguir las tareas de la base de datos
- Poder listar todas las tareas
- Poder agregar información a una tarea
- Poder obtener la documentación adicional de la base de datos
- Poder modificar la documentación adicional
- Las tablas de BD necesitan actualizarse para coincidir con nuestros nuevos modelos de datos

## EJEMPLOS Y DOCUMENTACIÓN:

Todos los ejemplos ya están referenciados en prp_mcp_base.md - hacer cualquier investigación adicional según sea necesario.

## OTRAS CONSIDERACIONES:

- No usar regex complejo o patrones de parseo complejos, usamos un LLM para parsear PRPs.
- El modelo y clave API para Anthropic ambos necesitan ser variables de entorno - estas están configuradas en .dev.vars.example
- Es muy importante que creemos una tarea por archivo para mantener las preocupaciones separadas

## Arquitectura Propuesta

### Herramientas MCP Principales

1. **parseprp** - Parsear PRP usando Anthropic y extraer tareas
2. **createTask** - Crear nueva tarea en la base de datos
3. **getTasks** - Obtener tareas de la base de datos
4. **updateTask** - Actualizar tarea existente
5. **deleteTask** - Eliminar tarea
6. **getDocumentation** - Obtener documentación adicional
7. **updateDocumentation** - Modificar documentación

### Esquema de Base de Datos

```sql
-- Tabla principal de tareas
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) DEFAULT 'pending',
  priority VARCHAR(20) DEFAULT 'medium',
  created_by VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Documentación asociada a PRPs
CREATE TABLE prp_documentation (
  id SERIAL PRIMARY KEY,
  prp_name VARCHAR(255) NOT NULL,
  goals TEXT,
  why TEXT,
  target_users TEXT,
  context TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Etiquetas para organización
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  color VARCHAR(7) DEFAULT '#000000'
);

-- Relación muchos a muchos entre tareas y etiquetas
CREATE TABLE task_tags (
  task_id INTEGER REFERENCES tasks(id) ON DELETE CASCADE,
  tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
  PRIMARY KEY (task_id, tag_id)
);
```

### Variables de Entorno Requeridas

```bash
# En .dev.vars
ANTHROPIC_API_KEY=tu_clave_api_anthropic
CLAUDE_MODEL=claude-3-sonnet-20240229
```