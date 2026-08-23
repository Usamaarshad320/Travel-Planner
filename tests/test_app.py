def test_application_initializes():
    from travel_planner.app import main

    assert main() is None