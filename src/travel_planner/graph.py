from langgraph.graph import END, START, StateGraph

from travel_planner.nodes.gateway import input_gateway
from travel_planner.state import TravelPlannerState


def build_graph():
    graph = StateGraph(TravelPlannerState)

    graph.add_node("input_gateway", input_gateway)

    graph.add_edge(START, "input_gateway")
    graph.add_edge("input_gateway", END)

    return graph.compile()