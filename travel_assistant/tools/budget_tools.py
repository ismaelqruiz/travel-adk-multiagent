
def estimate_trip_budget(
    destination: str,
    days: int,
    daily_budget_usd: float
) -> dict:
    """
    Calcula el presupuesto referencial de un viaje.

    Args:
        destination: Destino del viaje.
        days: Cantidad de días.
        daily_budget_usd: Presupuesto diario en dólares.

    Returns:
        Diccionario con el cálculo del presupuesto.
    """

    if not isinstance(destination, str) or not destination.strip():
        return {
            "status": "error",
            "message": "El destino debe ser válido."
        }

    if not isinstance(days, int) or isinstance(days, bool) or days <= 0:
        return {
            "status": "error",
            "message": "La cantidad de días debe ser mayor que cero."
        }

    if (
        not isinstance(daily_budget_usd, (int, float))
        or isinstance(daily_budget_usd, bool)
        or daily_budget_usd <= 0
    ):
        return {
            "status": "error",
            "message": "El presupuesto diario debe ser mayor que cero."
        }

    total = days * daily_budget_usd

    return {
        "status": "success",
        "destination": destination.strip(),
        "days": days,
        "daily_budget_usd": daily_budget_usd,
        "estimated_total_usd": round(total, 2),
        "message": "Presupuesto calculado correctamente."
    }
