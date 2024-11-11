from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# Ganti `SUPABASE_DATABASE_URL` dengan URL database dari Supabase Anda
SUPABASE_DATABASE_URL = "postgresql://postgres.chjuivjgmjekpdgqlvji:@SupaMick18@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

engine = create_engine(SUPABASE_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
