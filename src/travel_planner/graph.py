from langgraph.graph import END, START, StateGraph

from travel_planner.state import TravelPlannerState


def build_graph():
    graph = StateGraph(TravelPlannerState)

    graph.add_node("start", lambda state: state)

    graph.add_edge(START, "start")
    graph.add_edge("start", END)

    return graph.compile()