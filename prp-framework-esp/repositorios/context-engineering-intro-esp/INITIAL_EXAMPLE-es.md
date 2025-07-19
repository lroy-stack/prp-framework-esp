## FEATURE:

- Agente Pydantic AI que tiene otro agente Pydantic AI como herramienta.
- Agente de Investigación para el agente principal y después un Agente de borrador de email para el sub-agente.
- CLI para interactuar con el agente.
- Gmail para el agente de borrador de email, API de Brave para el agente de investigación.

## EXAMPLES:

En la carpeta `examples/`, hay un README para que leas y entiendas de qué se trata el ejemplo y también cómo estructurar tu propio README cuando crees documentación para la funcionalidad arriba mencionada.

- `examples/cli.py` - usa esto como plantilla para crear el CLI
- `examples/agent/` - lee todos los archivos aquí para entender las mejores prácticas para crear agentes Pydantic AI que soporten diferentes proveedores y LLMs, manejar dependencias de agente, y añadir herramientas al agente.

No copies ninguno de estos ejemplos directamente, es para un proyecto completamente diferente. Pero úsalo como inspiración y para mejores prácticas.

## DOCUMENTATION:

Documentación de Pydantic AI: https://ai.pydantic.dev/

## OTHER CONSIDERATIONS:

- Incluir un .env.example, README con instrucciones para setup incluyendo cómo configurar Gmail y Brave.
- Incluir la estructura del proyecto en el README.
- El entorno virtual ya ha sido configurado con las dependencias necesarias.
- Usa python_dotenv y load_env() para variables de entorno