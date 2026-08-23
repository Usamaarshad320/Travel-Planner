from langgraph.graph import END, START, StateGraph

from travel_planner.nodes.gateway import input_gateway
from travel_planner.state import TravelPlannerState


def route_after_gateway(state: TravelPlannerState) -> str:
    if not state.get("is_relevant", False):
        return "reject"

    if not state.get("is_safe", False):
        return "reject"

    return "continue"


def reject_request(state: TravelPlannerState) -> TravelPlannerState:
    return {
        **state,
        "final_response": (
            f"Request rejected: "
            f"{state.get('rejection_reason', 'Request cannot be processed.')}"
        ),
    }


def build_graph():
    graph = StateGraph(TravelPlannerState)

    graph.add_node("input_gateway", input_gateway)
    graph.add_node("reject_request", reject_request)

    graph.add_edge(START, "input_gateway")

    graph.add_conditional_edges(
        "input_gateway",
        route_after_gateway,
        {
            "continue": END,
            "reject": "reject_request",
        },
    )

    graph.add_edge("reject_request", END)

    return graph.compile()