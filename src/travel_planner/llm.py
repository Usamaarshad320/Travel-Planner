from langchain_groq import ChatGroq

from travel_planner.config import GROQ_API_KEY, LLM_MODEL


def get_llm() -> ChatGroq:
    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY is not configured.")

    return ChatGroq(
        model=LLM_MODEL,
        api_key=GROQ_API_KEY,
    )