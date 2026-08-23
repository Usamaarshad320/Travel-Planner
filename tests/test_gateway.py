from travel_planner.graph import build_graph


def test_valid_request_continues():
    graph = build_graph()

    result = graph.invoke(
        {"user_request": "Plan a 7-day trip to Turkey."}
    )

    assert result["is_relevant"] is True
    assert result["is_safe"] is True
    assert "final_response" not in result


def test_empty_request_is_rejected():
    graph = build_graph()

    result = graph.invoke({"user_request": "   "})

    assert result["is_relevant"] is False
    assert result["rejection_reason"] == "Empty travel request."
    assert result["final_response"] is not None