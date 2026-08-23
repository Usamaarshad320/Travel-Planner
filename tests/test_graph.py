from travel_planner.graph import build_graph


def test_graph_preserves_user_request():
    graph = build_graph()

    result = graph.invoke(
        {"user_request": "Plan a 7-day trip to Turkey."}
    )

    assert result["user_request"] == "Plan a 7-day trip to Turkey."
    