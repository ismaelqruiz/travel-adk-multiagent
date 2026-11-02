from travel_assistant.tools.risk_tools import assess_basic_travel_risks


def test_assess_risks_cusco():
    result = assess_basic_travel_risks("Cusco", "temporada alta")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert len(result["risks"]) >= 2


def test_assess_risks_rainy_season():
    result = assess_basic_travel_risks("Lima", "temporada de lluvia")

    assert result["status"] == "success"
    assert any("impermeable" in risk for risk in result["risks"])


def test_assess_risks_invalid_destination():
    result = assess_basic_travel_risks("", "temporada alta")

    assert result["status"] == "error"


def test_assess_risks_invalid_season():
    result = assess_basic_travel_risks("Cusco", "")

    assert result["status"] == "error"