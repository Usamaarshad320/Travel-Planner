from travel_planner.graph import build_graph


def main() -> None:
    graph = build_graph()

    result = graph.invoke(
        {"user_request": "Plan a 7-day trip to Turkey."}
    )

    print(result)


if __name__ == "__main__":
    main()