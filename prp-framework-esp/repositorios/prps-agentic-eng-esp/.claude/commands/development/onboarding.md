Por favor realiza un análisis comprensivo de onboarding para un nuevo desarrollador que se une a este proyecto. Ejecuta los siguientes pasos:

## 1. Vista General del Proyecto
Primero, analiza la estructura del repositorio y proporciona:
- Nombre del proyecto, propósito y funcionalidad principal
- Stack tecnológico (lenguajes, frameworks, bases de datos, herramientas)
- Patrón de arquitectura (MVC, microservicios, etc.)
- Dependencias clave y sus propósitos

## 2. Estructura del Repositorio
Mapea la organización del codebase:
- Lista todos los directorios de nivel superior con sus propósitos
- Identifica dónde vive cada tipo de código (models, controllers, utils, tests)
- Destaca patrones organizacionales únicos o no estándar
- Nota cualquier estructura monorepo o submódulos

## 3. Primeros Pasos
Crea instrucciones de configuración paso a paso:
- Prerrequisitos (software requerido, versiones)
- Comandos de configuración de entorno
- Cómo instalar dependencias
- Archivos de configuración que necesitan ser creados/modificados
- Cómo ejecutar el proyecto localmente
- Cómo ejecutar pruebas
- Cómo construir para producción

## 4. Componentes Clave
Identifica y explica los archivos/módulos más importantes:
- Puntos de entrada (main.js, index.py, app.tsx, etc.)
- Ubicaciones de lógica de negocio core
- Modelos/esquemas de base de datos
- Endpoints API o rutas
- Gestión de configuración
- Implementación de autenticación/autorización

## 5. Flujo de Desarrollo
Documenta el proceso de desarrollo:
- Convenciones de nomenclatura de ramas Git
- Cómo crear una nueva funcionalidad
- Requerimientos de testing
- Reglas de estilo de código/linting
- Proceso de PR y guías de revisión
- Vista general del pipeline CI/CD

## 6. Decisiones de Arquitectura
Identifica patrones y decisiones importantes:
- Patrones de diseño utilizados y por qué
- Enfoque de gestión de estado
- Estrategia de manejo de errores
- Configuración de logging y monitoreo
- Medidas de seguridad
- Optimizaciones de rendimiento

## 7. Tareas Comunes
Proporciona ejemplos para tareas frecuentes de desarrollo:
- Cómo agregar un nuevo endpoint API
- Cómo crear un nuevo modelo de base de datos
- Cómo agregar una nueva prueba
- Cómo debugear problemas comunes
- Cómo actualizar dependencias

## 8. Gotchas Potenciales
Lista cosas que podrían confundir a nuevos desarrolladores:
- Configuraciones no obvias
- Variables de entorno requeridas
- Dependencias de servicios externos
- Problemas conocidos o workarounds
- Cuellos de botella de rendimiento
- Áreas de deuda técnica

## 9. Documentación y Recursos
- Localizar documentación existente (README, wikis, docs/)
- Documentación API
- Esquemas de base de datos
- Guías de despliegue
- Convenciones de equipo o guías de estilo

## 10. Próximos Pasos
Crear un checklist de onboarding para el nuevo desarrollador:
1. Configurar entorno de desarrollo
2. Ejecutar el proyecto exitosamente
3. Hacer un pequeño cambio de prueba
4. Ejecutar la suite de pruebas
5. Entender el flujo de usuario principal
6. Identificar área para empezar a contribuir

## Formato de Salida
Por favor crear:
1. Un archivo comprensivo ONBOARDING.md en la raíz del repositorio con toda la información anterior
2. Un QUICKSTART.md con solo los pasos esenciales de configuración
3. Sugerir actualizaciones al README.md si le falta información crítica (no actualizar el readme directamente)

Enfócate en claridad y accionabilidad. Asume que el desarrollador es experimentado pero completamente nuevo a este codebase.