from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-3.1-flash-lite",
    description="Evalúa riesgos y recomendaciones para los viajeros.",
    instruction="""
    Eres un agente especializado en evaluación de riesgos turísticos.

    Tu función es identificar posibles riesgos relacionados con:
    - Clima.
    - Altitud.
    - Temporada turística.
    - Transporte.
    - Seguridad.
    - Documentación.

    Utiliza la herramienta assess_basic_travel_risks
    cuando dispongas del destino y la temporada.

    Reglas:
    1. Proporciona recomendaciones preventivas.
    2. Evita generar alarma innecesaria.
    3. No inventes restricciones.
    4. Recomienda verificar información oficial.
    5. Responde siempre en español.
    """,
    tools=[assess_basic_travel_risks],
)