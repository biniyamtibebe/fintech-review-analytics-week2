import pandas as pd
from sqlalchemy import create_engine,text
import os


DATABASE_URL = "postgresql://postgres:main32@localhost:5432/bank_reviews"
engine = create_engine(DATABASE_URL)


# Load final analyzed data from Task 2
df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\thematicanalyzed_reviews.csv')
# Clean and prepare
df = df.rename(columns={'review': 'review_text', 'date': 'review_date'})
df['review_date'] = pd.to_datetime(df['review_date']).dt.date

# Bank mapping
bank_mapping = {
    'CBE': ('Commercial Bank of Ethiopia', 'CBE Birr'),
    'BOA': ('Bank of Abyssinia', 'Abyssinia Mobile'),
    'Dashen': ('Dashen Bank', 'Amole / Dashen Mobile')
}

# Insert banks and get IDs
with engine.begin() as conn:
    for short_name, (full_name, app) in bank_mapping.items():
        conn.execute(text("""
            INSERT INTO banks (bank_name, app_name) 
            VALUES (:name, :app) 
            ON CONFLICT (bank_name) DO NOTHING
        """), {'name': full_name, 'app': app})

# Get bank_id mapping
bank_ids = pd.read_sql("SELECT bank_id, bank_name FROM banks", engine)
bank_id_map = dict(bank_ids.set_index('bank_name')['bank_id'])

# Map short names to full names
short_to_full = {'CBE': 'Commercial Bank of Ethiopia',
                 'BOA': 'Bank of Abyssinia',
                 'Dashen': 'Dashen Bank'}

df['bank_name'] = df['bank'].map(short_to_full)
df['bank_id'] = df['bank_name'].map(bank_id_map)

# Select and reorder columns for insert
reviews_to_insert = df[[
    'bank_id', 'review_text', 'rating', 'review_date',
    'sentiment_label', 'sentiment_score', 'source', 'themes'
]].copy()

# Insert reviews (bulk)
reviews_to_insert.to_sql(
    'review',
    engine,
    if_exists='append',
    index=False,
    method='multi',
    chunksize=1000
)

print(f"Successfully inserted {len(reviews_to_insert)} reviews into PostgreSQL!")