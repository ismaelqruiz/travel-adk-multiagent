from travel_assistant.agent import root_agent


def test_root_agent_name():
    assert root_agent.name == "travel_coordinator_agent"


def test_root_agent_has_five_subagents():
    subagent_names = [
        agent.name for agent in root_agent.sub_agents
    ]

    expected_agents = [
        "web_search_agent",
        "itinerary_agent",
        "budget_agent",
        "risk_reviewer_agent",
        "local_culture_agent",
    ]

    assert set(subagent_names) == set(expected_agents)


def test_local_culture_agent_is_registered():
    subagent_names = [
        agent.name for agent in root_agent.sub_agents
    ]

    assert "local_culture_agent" in subagent_names