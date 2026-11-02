from google.adk.agents import Agent
from google.adk.tools import google_search

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-3.1-flash-lite",
    description="Busca información actualizada sobre destinos turísticos.",
    instruction="""
    Eres un agente especializado en búsqueda de información turística.

    Utiliza Google Search cuando el usuario necesite información actualizada.

    Investiga:
    - Atracciones turísticas.
    - Horarios y recomendaciones.
    - Restricciones de viaje.
    - Información turística oficial.
    - Cambios recientes que puedan afectar el viaje.

    Reglas:
    1. Prioriza fuentes oficiales y confiables.
    2. Resume la información de forma clara.
    3. No inventes precios ni horarios.
    4. Indica que la información debe verificarse antes de reservar.
    5. Responde en español.
    """,
    tools=[google_search],
)