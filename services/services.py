import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.phishing import Phishing

def check_database(content: str, db):
    """Check if content exists in the phishing database"""
    result = db.execute(select(Phishing).where(Phishing.content == content))
    record = result.scalars().first()
    return record


def ai_phishing_analysis(content: str):
    """Mock AI function for phishing detection"""
    risk_score = random.randint(1, 100)
    advice = "⚠️ Be cautious! This looks suspicious." if risk_score > 50 else "✅ This seems safe."
    return {"risk_score": risk_score, "advice": advice}
