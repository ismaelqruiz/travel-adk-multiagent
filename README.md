# Travel ADK Multiagent

Sistema multiagente inteligente para la planificación de viajes turísticos, desarrollado con Python y Google Agent Development Kit (ADK).

## Objetivo

Proporcionar asistencia en la planificación de viajes mediante agentes especializados que colaboran para generar itinerarios, estimar presupuestos, identificar riesgos y ofrecer información cultural y turística.

## Arquitectura multiagente

El sistema cuenta con un agente coordinador y cinco agentes especializados:

- **Travel Coordinator:** coordina las solicitudes y distribuye las tareas.
- **Web Search Agent:** busca información turística actualizada.
- **Itinerary Agent:** organiza las actividades del viaje.
- **Budget Agent:** estima los gastos del viaje.
- **Risk Reviewer Agent:** identifica riesgos y proporciona recomendaciones.
- **Local Culture Agent:** proporciona información cultural y costumbres locales.

## Tecnologías utilizadas

- Python 3.11
- Google ADK
- Gemini API
- Poetry
- Pytest
- Ruff
- GitHub Actions
- SonarCloud

## Instalación

```bash
poetry install
```

## Configuración

Crear un archivo `.env` a partir de `.env.example` y configurar la variable `GOOGLE_API_KEY` con una clave propia.

## Ejecución

```bash
poetry run adk run travel_assistant
```

Para iniciar la interfaz web:

```bash
poetry run adk web
```

## Pruebas y calidad de código

Ejecutar las pruebas automatizadas:

```bash
poetry run python -m pytest
```

Verificar la calidad del código:

```bash
poetry run ruff check .
```

## Estructura del proyecto

- `travel_assistant/`: agentes y herramientas del sistema.
- `tests/`: pruebas automatizadas.
- `.github/workflows/`: flujos de integración continua.

## Autoría

Proyecto académico desarrollado como parte del curso de Sistemas Inteligentes.