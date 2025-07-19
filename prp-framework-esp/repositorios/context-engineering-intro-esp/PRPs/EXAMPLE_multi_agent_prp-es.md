name: "Sistema Multi-Agente: Agente de Investigación con Sub-Agente de Borrador de Email"
description: |

## Propósito
Construir un sistema multi-agente de Pydantic AI donde un Agente de Investigación principal usa la API de Brave Search y tiene un Agente de Borrador de Email (usando Gmail API) como herramienta. Esto demuestra el patrón agente-como-herramienta con integraciones de API externas.

## Principios Fundamentales
1. **Context is King**: Incluye TODA la documentación necesaria, ejemplos y advertencias
2. **Bucles de Validación**: Proporciona tests/lints ejecutables que la IA puede ejecutar y corregir
3. **Información Densa**: Usa keywords y patrones del codebase
4. **Éxito Progresivo**: Comienza simple, valida, luego mejora

---

## Goal
Crear un sistema multi-agente listo para producción donde los usuarios pueden investigar temas vía CLI, y el Agente de Investigación puede delegar tareas de redacción de emails a un Agente de Borrador de Email. El sistema debe soportar múltiples proveedores LLM y manejar autenticación API de forma segura.

## Why
- **Valor de negocio**: Automatiza flujos de trabajo de investigación y redacción de emails
- **Integración**: Demuestra patrones avanzados multi-agente de Pydantic AI
- **Problemas resueltos**: Reduce trabajo manual para comunicaciones de email basadas en investigación

## What
Una aplicación basada en CLI donde:
- Usuarios ingresan consultas de investigación
- Agente de Investigación busca usando API de Brave
- Agente de Investigación puede invocar Agente de Borrador de Email para crear borradores de Gmail
- Resultados se transmiten de vuelta al usuario en tiempo real

### Criterios de Éxito
- [ ] Agente de Investigación busca exitosamente vía API de Brave
- [ ] Agente de Email crea borradores de Gmail con autenticación apropiada
- [ ] Agente de Investigación puede invocar Agente de Email como herramienta
- [ ] CLI proporciona respuestas en streaming con visibilidad de herramientas
- [ ] Todos los tests pasan y el código cumple estándares de calidad

## Todo el Contexto Necesario

### Documentación y Referencias
```yaml
# DEBE LEER - Incluye estos en tu ventana de contexto
- url: https://ai.pydantic.dev/agents/
  why: Patrones de creación de agentes principales
  
- url: https://ai.pydantic.dev/multi-agent-applications/
  why: Patrones de sistema multi-agente, especialmente agente-como-herramienta
  
- url: https://developers.google.com/gmail/api/guides/sending
  why: Autenticación de Gmail API y creación de borradores
  
- url: https://api-dashboard.search.brave.com/app/documentation
  why: Endpoints REST de Brave Search API
  
- file: examples/agent/agent.py
  why: Patrón para creación de agente, registro de herramientas, dependencias
  
- file: examples/agent/providers.py
  why: Patrón de configuración LLM multi-proveedor
  
- file: examples/cli.py
  why: Estructura CLI con respuestas en streaming y visibilidad de herramientas

- url: https://github.com/googleworkspace/python-samples/blob/main/gmail/snippet/send%20mail/create_draft.py
  why: Ejemplo oficial de creación de borrador de Gmail
```

### Árbol actual del Codebase
```bash
.
├── examples/
│   ├── agent/
│   │   ├── agent.py
│   │   ├── providers.py
│   │   └── ...
│   └── cli.py
├── PRPs/
│   └── templates/
│       └── prp_base.md
├── INITIAL.md
├── CLAUDE.md
└── requirements.txt
```

### Árbol deseado del Codebase con archivos a añadir
```bash
.
├── agents/
│   ├── __init__.py               # Init del paquete
│   ├── research_agent.py         # Agente principal con Brave Search
│   ├── email_agent.py           # Sub-agente con capacidades Gmail
│   ├── providers.py             # Configuración de proveedor LLM
│   └── models.py                # Modelos Pydantic para validación de datos
├── tools/
│   ├── __init__.py              # Init del paquete
│   ├── brave_search.py          # Integración Brave Search API
│   └── gmail_tool.py            # Integración Gmail API
├── config/
│   ├── __init__.py              # Init del paquete
│   └── settings.py              # Gestión de entorno y configuración
├── tests/
│   ├── __init__.py              # Init del paquete
│   ├── test_research_agent.py   # Tests del agente de investigación
│   ├── test_email_agent.py      # Tests del agente de email
│   ├── test_brave_search.py     # Tests de herramienta de búsqueda Brave
│   ├── test_gmail_tool.py       # Tests de herramienta Gmail
│   └── test_cli.py              # Tests de CLI
├── cli.py                       # Interfaz CLI
├── .env.example                 # Plantilla de variables de entorno
├── requirements.txt             # Dependencias actualizadas
├── README.md                    # Documentación comprensiva
└── credentials/.gitkeep         # Directorio para credenciales Gmail
```

### Gotchas Conocidos y Peculiaridades de Librerías
```python
# CRÍTICO: Pydantic AI requiere async en toda la aplicación - no funciones sync en contexto async
# CRÍTICO: Gmail API requiere flujo OAuth2 en primera ejecución - credentials.json necesario
# CRÍTICO: Brave API tiene límites de rate - 2000 req/mes en tier gratuito
# CRÍTICO: Patrón agente-como-herramienta requiere pasar ctx.usage para tracking de tokens
# CRÍTICO: Borradores de Gmail necesitan codificación base64 con formato MIME apropiado
# CRÍTICO: Siempre usar imports absolutos para código más limpio
# CRÍTICO: Almacenar credenciales sensibles en .env, nunca commitearlas
```

## Blueprint de Implementación

### Modelos de datos y estructura

```python
# models.py - Estructuras de datos principales
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ResearchQuery(BaseModel):
    query: str = Field(..., description="Tema de investigación a investigar")
    max_results: int = Field(10, ge=1, le=50)
    include_summary: bool = Field(True)

class BraveSearchResult(BaseModel):
    title: str
    url: str
    description: str
    score: float = Field(0.0, ge=0.0, le=1.0)

class EmailDraft(BaseModel):
    to: List[str] = Field(..., min_items=1)
    subject: str = Field(..., min_length=1)
    body: str = Field(..., min_length=1)
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None

class ResearchEmailRequest(BaseModel):
    research_query: str
    email_context: str = Field(..., description="Contexto para generación de email")
    recipient_email: str
```

### Lista de tareas a completar

```yaml
Tarea 1: Configurar Configuración y Entorno
CREAR config/settings.py:
  - PATRÓN: Usar pydantic-settings como ejemplos usan os.getenv
  - Cargar variables de entorno con defaults
  - Validar que las API keys requeridas estén presentes

CREAR .env.example:
  - Incluir todas las variables de entorno requeridas con descripciones
  - Seguir patrón de examples/README.md

Tarea 2: Implementar Herramienta Brave Search
CREAR tools/brave_search.py:
  - PATRÓN: Funciones async como examples/agent/tools.py
  - Cliente REST simple usando httpx (ya en requirements)
  - Manejar límites de rate y errores graciosamente
  - Retornar modelos BraveSearchResult estructurados

Tarea 3: Implementar Herramienta Gmail
CREAR tools/gmail_tool.py:
  - PATRÓN: Seguir flujo OAuth2 de Gmail quickstart
  - Almacenar token.json en directorio credentials/
  - Crear borrador con codificación MIME apropiada
  - Manejar refresh de autenticación automáticamente

Tarea 4: Crear Agente de Borrador de Email
CREAR agents/email_agent.py:
  - PATRÓN: Seguir estructura de examples/agent/agent.py
  - Usar Agent con patrón deps_type
  - Registrar gmail_tool como @agent.tool
  - Retornar modelo EmailDraft

Tarea 5: Crear Agente de Investigación
CREAR agents/research_agent.py:
  - PATRÓN: Patrón multi-agente de documentos Pydantic AI
  - Registrar brave_search como herramienta
  - Registrar email_agent.run() como herramienta
  - Usar RunContext para inyección de dependencias

Tarea 6: Implementar Interfaz CLI
CREAR cli.py:
  - PATRÓN: Seguir patrón de streaming de examples/cli.py
  - Output codificado por colores con visibilidad de herramientas
  - Manejar async apropiadamente con asyncio.run()
  - Gestión de sesión para contexto de conversación

Tarea 7: Añadir Tests Comprensivos
CREAR tests/:
  - PATRÓN: Reflejar estructura de test de ejemplos
  - Mockear llamadas a API externas
  - Testear camino feliz, casos límite, errores
  - Asegurar cobertura 80%+

Tarea 8: Crear Documentación
CREAR README.md:
  - PATRÓN: Seguir estructura de examples/README.md
  - Incluir setup, instalación, uso
  - Pasos de configuración de API key
  - Diagrama de arquitectura
```

### Pseudocódigo por tarea

```python
# Tarea 2: Herramienta Brave Search
async def search_brave(query: str, api_key: str, count: int = 10) -> List[BraveSearchResult]:
    # PATRÓN: Usar httpx como ejemplos usan aiohttp
    async with httpx.AsyncClient() as client:
        headers = {"X-Subscription-Token": api_key}
        params = {"q": query, "count": count}
        
        # GOTCHA: Brave API retorna 401 si API key es inválida
        response = await client.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers=headers,
            params=params,
            timeout=30.0  # CRÍTICO: Establecer timeout para evitar colgarse
        )
        
        # PATRÓN: Manejo de errores estructurado
        if response.status_code != 200:
            raise BraveAPIError(f"API retornó {response.status_code}")
        
        # Parsear y validar con Pydantic
        data = response.json()
        return [BraveSearchResult(**result) for result in data.get("web", {}).get("results", [])]

# Tarea 5: Agente de Investigación con Agente de Email como Herramienta
@research_agent.tool
async def create_email_draft(
    ctx: RunContext[AgentDependencies],
    recipient: str,
    subject: str,
    context: str
) -> str:
    """Crear borrador de email basado en contexto de investigación."""
    # CRÍTICO: Pasar usage para tracking de tokens
    result = await email_agent.run(
        f"Crear un email para {recipient} sobre: {context}",
        deps=EmailAgentDeps(subject=subject),
        usage=ctx.usage  # PATRÓN de documentos multi-agente
    )
    
    return f"Borrador creado con ID: {result.data}"
```

### Puntos de Integración
```yaml
ENVIRONMENT:
  - añadir a: .env
  - vars: |
      # Configuración LLM
      LLM_PROVIDER=openai
      LLM_API_KEY=sk-...
      LLM_MODEL=gpt-4
      
      # Brave Search
      BRAVE_API_KEY=BSA...
      
      # Gmail (ruta a credentials.json)
      GMAIL_CREDENTIALS_PATH=./credentials/credentials.json
      
CONFIG:
  - Gmail OAuth: Primera ejecución abre navegador para autorización
  - Almacenamiento de token: ./credentials/token.json (auto-creado)
  
DEPENDENCIES:
  - Actualizar requirements.txt con:
    - google-api-python-client
    - google-auth-httplib2
    - google-auth-oauthlib
```

## Bucle de Validación

### Nivel 1: Sintaxis y Estilo
```bash
# Ejecuta estos PRIMERO - corrige cualquier error antes de proceder
ruff check . --fix              # Auto-corregir problemas de estilo
mypy .                          # Verificación de tipos

# Esperado: Sin errores. Si hay errores, LEE y corrige.
```

### Nivel 2: Pruebas Unitarias
```python
# test_research_agent.py
async def test_research_with_brave():
    """Testear que agente de investigación busca correctamente"""
    agent = create_research_agent()
    result = await agent.run("investigación de seguridad IA")
    assert result.data
    assert len(result.data) > 0

async def test_research_creates_email():
    """Testear que agente de investigación puede invocar agente de email"""
    agent = create_research_agent()
    result = await agent.run(
        "Investigar seguridad IA y redactar email a john@example.com"
    )
    assert "draft_id" in result.data

# test_email_agent.py  
def test_gmail_authentication(monkeypatch):
    """Testear manejo de flujo OAuth de Gmail"""
    monkeypatch.setenv("GMAIL_CREDENTIALS_PATH", "test_creds.json")
    tool = GmailTool()
    assert tool.service is not None

async def test_create_draft():
    """Testear creación de borrador con codificación apropiada"""
    agent = create_email_agent()
    result = await agent.run(
        "Crear email a test@example.com sobre investigación IA"
    )
    assert result.data.get("draft_id")
```

```bash
# Ejecutar tests iterativamente hasta que pasen:
pytest tests/ -v --cov=agents --cov=tools --cov-report=term-missing

# Si falla: Debuggear test específico, corregir código, re-ejecutar
```

### Nivel 3: Test de Integración
```bash
# Testear interacción CLI
python cli.py

# Interacción esperada:
# Tú: Investigar últimos desarrollos en seguridad IA
# 🤖 Asistente: [Transmite resultados de investigación]
# 🛠 Herramientas Usadas:
#   1. brave_search (query='desarrollos seguridad IA', limit=10)
#
# Tú: Crear un borrador de email sobre esto para john@example.com  
# 🤖 Asistente: [Crea borrador]
# 🛠 Herramientas Usadas:
#   1. create_email_draft (recipient='john@example.com', ...)

# Verificar carpeta de borradores Gmail para borrador creado
```

## Checklist de Validación Final
- [ ] Todos los tests pasan: `pytest tests/ -v`
- [ ] Sin errores de linting: `ruff check .`
- [ ] Sin errores de tipo: `mypy .`
- [ ] Flujo OAuth de Gmail funciona (navegador se abre, token guardado)
- [ ] Brave Search retorna resultados
- [ ] Agente de Investigación invoca Agente de Email exitosamente
- [ ] CLI transmite respuestas con visibilidad de herramientas
- [ ] Casos de error manejados graciosamente
- [ ] README incluye instrucciones de setup claras
- [ ] .env.example tiene todas las variables requeridas

---

## Anti-Patrones a Evitar
- ❌ No hardcodear API keys - usar variables de entorno
- ❌ No usar funciones sync en contexto de agente async
- ❌ No saltarse setup de flujo OAuth para Gmail
- ❌ No ignorar límites de rate para APIs
- ❌ No olvidar pasar ctx.usage en llamadas multi-agente
- ❌ No commitear archivos credentials.json o token.json

## Puntuación de Confianza: 9/10

Alta confianza debido a:
- Ejemplos claros a seguir del codebase
- APIs externas bien documentadas
- Patrones establecidos para sistemas multi-agente
- Puertas de validación comprensivas

Incertidumbre menor en UX de setup OAuth de Gmail por primera vez, pero la documentación proporciona orientación clara.