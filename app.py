from fastapi import FastAPI
from routes.router import router
import uvicorn
import logging
from config.database import Base, engine
from models.phishing import Phishing


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")


app = FastAPI(title="Phishing Detector API")

app.include_router(router)

