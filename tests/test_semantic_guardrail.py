from travel_planner.guardrails import semantic_guardrail


def test_semantic_guardrail_handles_travel_request():
    result = semantic_guardrail(
        "I want to spend a week exploring Turkey."
    )

    assert result.is_relevant is True
    assert result.is_safe is True