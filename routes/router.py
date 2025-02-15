from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from models.phishing import Phishing
from schimas.schemas import CheckContentRequest, PhishingResponse, AIResponse
from services.services import check_database, ai_phishing_analysis

router = APIRouter()

@router.post("/check-phishing/", response_model=PhishingResponse)
def check_phishing(request: CheckContentRequest, db=Depends(get_db)):
    content = request.content
    record = check_database(content, db)  
    if record:
        is_phishing = bool(record.is_phishing)
        message = "⚠️ This is a known phishing attempt!" if is_phishing else "✅ This content is safe."
        return {"found_in_db": True, "is_phishing": is_phishing, "message": message}
    # AI Analysis if not found
    ai_result = ai_phishing_analysis(content)  
    return {"found_in_db": False, "message": "Content not found in DB", **ai_result}

@router.post("/add-phishing/")
def add_phishing_entry(request: CheckContentRequest, is_phishing: bool, db=Depends(get_db)):
    """Manually add phishing data"""
    record = Phishing(content=request.content, is_phishing=is_phishing)
    db.add(record)
    db.commit()  
    return {"message": "Content added successfully!"}
