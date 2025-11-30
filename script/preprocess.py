import pandas as pd
import os

# Load raw data
df = pd.read_csv('Data/raw_reviews.csv')

# Check if DataFrame is empty
if df.empty:
    print("No data found. Please check the raw reviews CSV.")
else:
    # Remove duplicates based on review text
    df.drop_duplicates(subset=['review'], inplace=True)

    # Handle missing data: Drop rows with missing review or rating
    df.dropna(subset=['review', 'rating'], inplace=True)

    # Normalize dates to YYYY-MM-DD
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Handle invalid dates
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    # Basic text cleaning (lowercase, remove punctuation)
    df['review'] = df['review'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

    # Ensure minimum per bank
    bank_counts = df['bank'].value_counts()
    print("Reviews count per bank:")
    print(bank_counts)  # Print counts for review verification

    # Save cleaned CSV
    cleaned_path = 'Data/cleaned_reviews.csv'
    os.makedirs('Data', exist_ok=True)  # Ensure directory exists

    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned {len(df)} reviews and saved to {cleaned_path}.")