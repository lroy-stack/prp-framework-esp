name: "Plantilla Base PRP v2 - Rica en Contexto con Bucles de Validación"
description: |

## Propósito
Plantilla optimizada para agentes IA para implementar funcionalidades con contexto suficiente y capacidades de auto-validación para lograr código funcional a través de refinamiento iterativo.

## Principios Fundamentales
1. **Context is King**: Incluye TODA la documentación necesaria, ejemplos y advertencias
2. **Bucles de Validación**: Proporciona tests/lints ejecutables que la IA puede ejecutar y corregir
3. **Información Densa**: Usa keywords y patrones del codebase
4. **Éxito Progresivo**: Comienza simple, valida, luego mejora
5. **Reglas globales**: Asegúrate de seguir todas las reglas en CLAUDE.md

---

## Goal
[Qué necesita construirse - sé específico sobre el estado final y deseos]

## Why
- [Valor de negocio e impacto del usuario]
- [Integración con funcionalidades existentes]
- [Problemas que esto resuelve y para quién]

## What
[Comportamiento visible al usuario y requisitos técnicos]

### Criterios de Éxito
- [ ] [Resultados específicos medibles]

## Todo el Contexto Necesario

### Documentación y Referencias (lista todo el contexto necesario para implementar la funcionalidad)
```yaml
# DEBE LEER - Incluye estos en tu ventana de contexto
- url: [URL oficial de documentos API]
  why: [Secciones/métodos específicos que necesitarás]
  
- file: [ruta/al/ejemplo.py]
  why: [Patrón a seguir, gotchas a evitar]
  
- doc: [URL de documentación de librería] 
  section: [Sección específica sobre problemas comunes]
  critical: [Insight clave que previene errores comunes]

- docfile: [PRPs/ai_docs/archivo.md]
  why: [documentos que el usuario ha pegado en el proyecto]

```

### Árbol actual del Codebase (ejecuta `tree` en la raíz del proyecto) para obtener una visión general del codebase
```bash

```

### Árbol deseado del Codebase con archivos a añadir y responsabilidad del archivo
```bash

```

### Gotchas Conocidos de nuestro codebase y Peculiaridades de Librerías
```python
# CRÍTICO: [Nombre de librería] requiere [configuración específica]
# Ejemplo: FastAPI requiere funciones async para endpoints
# Ejemplo: Este ORM no soporta inserts batch de más de 1000 registros
# Ejemplo: Usamos pydantic v2 y  
```

## Blueprint de Implementación

### Modelos de datos y estructura

Crear los modelos de datos fundamentales, aseguramos type safety y consistencia.
```python
Ejemplos: 
 - modelos orm
 - modelos pydantic
 - esquemas pydantic
 - validadores pydantic

```

### lista de tareas a completar para cumplir el PRP en el orden que deben completarse

```yaml
Tarea 1:
MODIFICAR src/existing_module.py:
  - ENCONTRAR patrón: "class OldImplementation"
  - INYECTAR después de línea que contiene "def __init__"
  - PRESERVAR firmas de método existentes

CREAR src/new_feature.py:
  - REFLEJAR patrón de: src/similar_feature.py
  - MODIFICAR nombre de clase y lógica principal
  - MANTENER patrón de manejo de errores idéntico

...(...)

Tarea N:
...

```


### Pseudocódigo por tarea según sea necesario añadido a cada tarea
```python

# Tarea 1
# Pseudocódigo con detalles CRÍTICOS no escribas código completo
async def new_feature(param: str) -> Result:
    # PATRÓN: Siempre validar input primero (ver src/validators.py)
    validated = validate_input(param)  # lanza ValidationError
    
    # GOTCHA: Esta librería requiere connection pooling
    async with get_connection() as conn:  # ver src/db/pool.py
        # PATRÓN: Usar decorador retry existente
        @retry(attempts=3, backoff=exponential)
        async def _inner():
            # CRÍTICO: API devuelve 429 si >10 req/sec
            await rate_limiter.acquire()
            return await external_api.call(validated)
        
        result = await _inner()
    
    # PATRÓN: Formato de respuesta estandarizado
    return format_response(result)  # ver src/utils/responses.py
```

### Puntos de Integración
```yaml
DATABASE:
  - migration: "Añadir columna 'feature_enabled' a tabla users"
  - index: "CREATE INDEX idx_feature_lookup ON users(feature_id)"
  
CONFIG:
  - añadir a: config/settings.py
  - patrón: "FEATURE_TIMEOUT = int(os.getenv('FEATURE_TIMEOUT', '30'))"
  
ROUTES:
  - añadir a: src/api/routes.py  
  - patrón: "router.include_router(feature_router, prefix='/feature')"
```

## Bucle de Validación

### Nivel 1: Sintaxis y Estilo
```bash
# Ejecuta estos PRIMERO - corrige cualquier error antes de proceder
ruff check src/new_feature.py --fix  # Auto-corrige lo que es posible
mypy src/new_feature.py              # Verificación de tipos

# Esperado: Sin errores. Si hay errores, LEE el error y corrige.
```

### Nivel 2: Pruebas Unitarias cada nueva funcionalidad/archivo/función usa patrones de test existentes
```python
# CREAR test_new_feature.py con estos casos de test:
def test_happy_path():
    """Funcionalidad básica funciona"""
    result = new_feature("valid_input")
    assert result.status == "success"

def test_validation_error():
    """Input inválido lanza ValidationError"""
    with pytest.raises(ValidationError):
        new_feature("")

def test_external_api_timeout():
    """Maneja timeouts graciosamente"""
    with mock.patch('external_api.call', side_effect=TimeoutError):
        result = new_feature("valid")
        assert result.status == "error"
        assert "timeout" in result.message
```

```bash
# Ejecuta e itera hasta que pase:
uv run pytest test_new_feature.py -v
# Si falla: Lee error, entiende causa raíz, corrige código, re-ejecuta (nunca mockear para pasar)
```

### Nivel 3: Test de Integración
```bash
# Iniciar el servicio
uv run python -m src.main --dev

# Testear el endpoint
curl -X POST http://localhost:8000/feature \
  -H "Content-Type: application/json" \
  -d '{"param": "test_value"}'

# Esperado: {"status": "success", "data": {...}}
# Si error: Verificar logs en logs/app.log para stack trace
```

## Checklist de validación final
- [ ] Todos los tests pasan: `uv run pytest tests/ -v`
- [ ] Sin errores de linting: `uv run ruff check src/`
- [ ] Sin errores de tipo: `uv run mypy src/`
- [ ] Test manual exitoso: [curl/comando específico]
- [ ] Casos de error manejados graciosamente
- [ ] Los logs son informativos pero no verbosos
- [ ] Documentación actualizada si es necesario

---

## Anti-Patrones a Evitar
- ❌ No crear nuevos patrones cuando los existentes funcionan
- ❌ No saltarse validación porque "debería funcionar"  
- ❌ No ignorar tests que fallan - corrígelos
- ❌ No usar funciones sync en contexto async
- ❌ No hardcodear valores que deberían ser config
- ❌ No capturar todas las excepciones - sé específico