from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Determine which .env file to load based on ENV
env = os.getenv("ENV", "dev")  # Default to "dev" if ENV is not set
env_file = f".env.{env}"

# Load the appropriate .env file
print(f"Loading environment from: {env_file}")
load_dotenv(env_file, verbose=True, override=True)

# Fetch credentials and DB configuration
ENV = os.getenv("ENV")
print(f"Current ENV: {ENV}")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base class for models
Base = declarative_base()
