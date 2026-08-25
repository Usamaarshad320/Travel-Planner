from travel_planner.llm import get_llm
from travel_planner.schemas import GuardrailResult


def semantic_guardrail(request: str) -> GuardrailResult:
    llm = get_llm()

    structured_llm = llm.with_structured_output(GuardrailResult)

    prompt = f"""
Classify this user request for a travel planning application.

Determine:
1. Is it relevant to travel planning?
2. Is it safe to process?
3. If it should not be processed, briefly explain why.

User request:
{request}
"""

    return structured_llm.invoke(prompt)


def needs_semantic_check(request: str) -> bool:
    return len(request.split()) > 5

def check_capability(request: str) -> bool:
    """
    Determine whether the request is within the broad
    capabilities of the travel planning application.

    This is intentionally conservative for now.
    """
    unsupported_patterns = {
        "book a flight",
        "purchase a ticket",
        "make a payment",
        "send money",
    }

    normalized_request = request.lower()

    return not any(
        pattern in normalized_request
        for pattern in unsupported_patterns
    )