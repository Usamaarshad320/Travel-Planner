from travel_planner.guardrails import (
    needs_semantic_check,
    semantic_guardrail,
)
from travel_planner.state import TravelPlannerState

from travel_planner.guardrails import (
    check_capability,
    needs_semantic_check,
    semantic_guardrail,
)





TRAVEL_KEYWORDS = {
    "travel",
    "trip",
    "vacation",
    "holiday",
    "flight",
    "hotel",
    "destination",
    "itinerary",
    "tour",
    "visit",
    "journey",
    "country",
    "city",
    "beach",
    "museum",
    "resort",
    "airport",
}

INJECTION_PATTERNS = {
    "ignore previous instructions",
    "ignore all previous instructions",
    "disregard previous instructions",
    "system prompt",
    "reveal your instructions",
    "reveal the system prompt",
}


def check_relevance(request: str) -> bool:
    normalized_request = request.lower()

    return any(
        keyword in normalized_request
        for keyword in TRAVEL_KEYWORDS
    )


def check_prompt_injection(request: str) -> bool:
    normalized_request = request.lower()

    return any(
        pattern in normalized_request
        for pattern in INJECTION_PATTERNS
    )








def input_gateway(state: TravelPlannerState) -> TravelPlannerState:
    request = state["user_request"].strip()

    if not request:
        return {
            **state,
            "is_relevant": False,
            "is_safe": True,
            "gateway_decision": "reject",
            "rejection_reason": "Empty travel request.",
        }

    if not check_relevance(request):
        return {
            **state,
            "is_relevant": False,
            "is_safe": True,
            "gateway_decision": "reject",
            "rejection_reason": (
                "Request does not appear to be travel-related."
            ),
        }

    if check_prompt_injection(request):
        return {
            **state,
            "is_relevant": True,
            "is_safe": False,
            "gateway_decision": "reject",
            "rejection_reason": (
                "Potential prompt injection detected."
            ),
        }

    if not check_capability(request):
         return {
             **state,
             "is_relevant": True,
             "is_safe": True,
             "gateway_decision": "reject",
             "is_supported": False,
             "rejection_reason": (
             "This request requires a capability "
             "that is not currently supported."
             ),
    }
    






    if needs_semantic_check(request):
        semantic_result = semantic_guardrail(request)

        if not semantic_result.is_relevant or not semantic_result.is_safe:
            return {
                **state,
                "is_relevant": semantic_result.is_relevant,
                "is_safe": semantic_result.is_safe,
                "gateway_decision": "reject",
                "rejection_reason": semantic_result.reason,
            }

    return {
        **state,
        "is_relevant": True,
        "is_safe": True,
        "is_supported": True,
        "gateway_decision": "accept",
    }