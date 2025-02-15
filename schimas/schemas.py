from pydantic import BaseModel

class CheckContentRequest(BaseModel):
    content: str

class PhishingResponse(BaseModel):
    found_in_db: bool
    is_phishing: bool = None
    message: str

class AIResponse(BaseModel):
    risk_score: int
    advice: str
