import os
from sqlalchemy import create_engine, text
import pandas as pd

# Correct database URL
DATABASE_URL = "postgresql://postgres:main32@localhost:5432/bank_reviews"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    # Create tables
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS banks (
            bank_id SERIAL PRIMARY KEY,
            bank_name VARCHAR(50) UNIQUE NOT NULL,
            app_name VARCHAR(100)
        );
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            bank_id INTEGER REFERENCES banks(bank_id) ON DELETE CASCADE,
            review_text TEXT NOT NULL,
            rating SMALLINT CHECK (rating BETWEEN 1 AND 5),
            review_date DATE,
            sentiment_label VARCHAR(20),
            sentiment_score NUMERIC(5,4),
            source VARCHAR(50),
            themes TEXT,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """))

    conn.commit()

print("Database 'bank_reviews' and tables created successfully!")
