import pandas as pd
from sqlalchemy import create_engine

# Load data
df = pd.read_csv('analyzed_reviews.csv')

# Connect to Postgres
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')

# Create schema/table
df.to_sql('reviews', engine, if_exists='replace', index=False)

print("Data stored in Postgres.")