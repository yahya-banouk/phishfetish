from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from config.database import Base

class Phishing(Base):
    __tablename__ = "phishing"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(512), nullable=False)  # Define a max length
    is_phishing = Column(Boolean, nullable=False)
