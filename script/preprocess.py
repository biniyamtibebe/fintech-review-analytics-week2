import pandas as pd

# Load raw data
df = pd.read_csv('Data/Dashnraw_reviews.csv')

# Remove duplicates based on review text
df.drop_duplicates(subset=['review'], inplace=True)

# Handle missing data: Drop rows with missing review or rating
df.dropna(subset=['review', 'rating'], inplace=True)

# Normalize dates to YYYY-MM-DD
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Basic text cleaning (lowercase, remove extras - more in NLP step)
df['review'] = df['review'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

# Ensure minimum per bank
print(df['bank'].value_counts())  # Check counts

# Save cleaned CSV
df.to_csv('Data/Dashncleaned_reviews.csv', index=False)
print(f"Cleaned {len(df)} reviews.")