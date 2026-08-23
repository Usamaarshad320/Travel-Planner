from travel_planner.state import TravelPlannerState


def input_gateway(state: TravelPlannerState) -> TravelPlannerState:
    request = state["user_request"].strip()

    if not request:
        return {
            **state,
            "is_relevant": False,
            "is_safe": True,
            "rejection_reason": "Empty travel request.",
        }

    return {
        **state,
        "is_relevant": True,
        "is_safe": True,
    }