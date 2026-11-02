
def assess_basic_travel_risks(destination: str, season: str) -> dict:
    """
    Identifica riesgos comunes según el destino y la temporada.
    """

    if not isinstance(destination, str) or not destination.strip():
        return {
            "status": "error",
            "message": "El destino debe ser válido."
        }

    if not isinstance(season, str) or not season.strip():
        return {
            "status": "error",
            "message": "La temporada debe ser válida."
        }

    destination_normalized = destination.lower().strip()
    season_normalized = season.lower().strip()

    risks = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        risks.append(
            "Considerar la altitud y permitir tiempo para aclimatarse."
        )

    if "lluvia" in season_normalized or "rain" in season_normalized:
        risks.append(
            "Llevar ropa impermeable y revisar las condiciones de las rutas."
        )

    if "alta" in season_normalized or "high" in season_normalized:
        risks.append(
            "Reservar alojamiento y entradas con anticipación."
        )

    if not risks:
        risks.append(
            "Consultar el clima, transporte, documentación y recomendaciones locales."
        )

    return {
        "status": "success",
        "destination": destination.strip(),
        "season": season.strip(),
        "risks": risks
    }
