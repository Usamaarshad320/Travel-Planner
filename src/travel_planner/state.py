from typing import TypedDict


class TravelPlannerState(TypedDict, total=False):
    user_request: str
    is_relevant: bool
    is_safe: bool
    requirements: dict
    final_response: str
    rejection_reason: str
    is_supported: bool
    gateway_decision: Literal["accept", "reject"]
    