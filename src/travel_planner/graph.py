from langgraph.graph import END, START, StateGraph

from travel_planner.nodes import initialize_request
from travel_planner.state import TravelPlannerState


def build_graph():
    graph = StateGraph(TravelPlannerState)

    graph.add_node("initialize_request", initialize_request)

    graph.add_edge(START, "initialize_request")
    graph.add_edge("initialize_request", END)

    return graph.compile()