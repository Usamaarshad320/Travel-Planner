from travel_planner.state import TravelPlannerState


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

def input_gateway(state: TravelPlannerState) -> TravelPlannerState:
    request = state["user_request"].strip()

    if not request:
        return {
            **state,
            "is_relevant": False,
            "is_safe": True,
            "rejection_reason": "Empty travel request.",
        }

    normalized_request = request.lower()

    if not any(keyword in normalized_request for keyword in TRAVEL_KEYWORDS):
        return {
            **state,
            "is_relevant": False,
            "is_safe": True,
            "rejection_reason": "Request does not appear to be travel-related.",
        }

    return {
        **state,
        "is_relevant": True,
        "is_safe": True,
    }