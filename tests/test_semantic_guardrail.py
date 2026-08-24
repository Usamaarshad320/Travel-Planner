from travel_planner.guardrails import semantic_guardrail


def test_semantic_guardrail_handles_travel_request(mocker):
    mock_llm = mocker.patch(
        "travel_planner.guardrails.get_llm"
    )

    structured_llm = mock_llm.return_value.with_structured_output.return_value

    structured_llm.invoke.return_value = {
        "is_relevant": True,
        "is_safe": True,
        "reason": None,
    }

    result = semantic_guardrail(
        "I want to spend a week exploring Turkey."
    )

    assert result.is_relevant is True
    assert result.is_safe is True