import pytest

from travel_planner.llm import get_llm


@pytest.mark.integration
def test_real_llm_connection():
    llm = get_llm()

    response = llm.invoke(
        "Reply with exactly: integration test successful."
    )

    assert response.content