from pydantic import BaseModel


class GuardrailResult(BaseModel):
    is_relevant: bool
    is_safe: bool
    reason: str | None = None