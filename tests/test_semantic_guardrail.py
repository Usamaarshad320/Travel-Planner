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

    from travel_planner.guardrails import (
    needs_semantic_check,
    semantic_guardrail,
)
from travel_planner.schemas import GuardrailResult


def test_semantic_guardrail_handles_travel_request(mocker):
    mock_llm = mocker.patch(
        "travel_planner.guardrails.get_llm"
    )

    structured_llm = (
        mock_llm.return_value.with_structured_output.return_value
    )

    structured_llm.invoke.return_value = GuardrailResult(
        is_relevant=True,
        is_safe=True,
        reason=None,
    )

    result = semantic_guardrail(
        "I want to spend a week exploring Turkey."
    )

    assert isinstance(result, GuardrailResult)
    assert result.is_relevant is True
    assert result.is_safe is True
    assert result.reason is None


def test_short_request_does_not_need_semantic_check():
    assert needs_semantic_check("Trip to Turkey") is False


def test_detailed_request_needs_semantic_check():
    assert needs_semantic_check(
        "Plan a seven day family trip to Turkey within our budget."
    ) is True



from travel_planner.guardrails import check_capability


def test_supported_request():
    assert check_capability(
        "Plan a trip to Turkey."
    ) is True


def test_unsupported_booking_request():
    assert check_capability(
        "Book a flight to Istanbul."
    ) is False