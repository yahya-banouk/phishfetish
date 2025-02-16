import random
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sentence_transformers import SentenceTransformer, util
from models.phishing import Phishing

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

def check_database(content: str, db: Session):
    """Check if content exists in the phishing database using semantic similarity"""
    # Fetch all phishing entries
    records = db.query(Phishing).all()
    
    if not records:
        return None  # No records in database

    content_embedding = model.encode(content)

    best_match = None
    highest_similarity = 0

    for record in records:
        db_embedding = model.encode(record.content)
        similarity = util.cos_sim(content_embedding, db_embedding).item()  # Compute similarity

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = record

    # If similarity is above threshold, classify as phishing
    threshold = 0.75
    if best_match and highest_similarity >= threshold:
        return {"record": best_match, "similarity": highest_similarity}

    return None  # No highly similar records found


def ai_phishing_analysis(content: str):
    """Mock AI function for phishing detection"""
    risk_score = random.randint(1, 100)
    advice = "⚠️ Be cautious! This looks suspicious." if risk_score > 50 else "✅ This seems safe."
    return {"risk_score": risk_score, "advice": advice}
