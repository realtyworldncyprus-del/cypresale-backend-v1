from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    print("❌ Database connection failed:", e)
