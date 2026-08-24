from travel_planner.llm import get_llm
from travel_planner.schemas import GuardrailResult

def semantic_guardrail(request: str, ) -> GuardrailResult:

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
