import os
import re
import pandas as pd
import torch
from transformers import pipeline

# Set environment variables for TensorFlow and logging
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "4"  # Suppress TensorFlow logs

# Load preprocessed data
input_path = r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\preprocessed_reviews.csv'
df = pd.read_csv(input_path)

# Function to remove Amharic text
def remove_amharic(text):
    if pd.isna(text):
        return text
    return re.sub(r'[\u1200-\u137F]+', '', text)

# Clean the 'review' column
df['preprocessed_reviews'] = df['review'].apply(remove_amharic)

# Initialize DistilBERT sentiment pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"  # Using PyTorch
)

# Function to get sentiment
def get_sentiment(text):
    if not isinstance(text, str) or not text.strip():  # Handle NaN, None, or empty
        return 'neutral', 0.0
    
    result = sentiment_pipeline(text)[0]
    label = result['label'].lower()
    score = result['score'] if label == 'positive' else -result['score']
    
    # Threshold small signals as neutral
    if abs(score) < 0.1:
        label = 'neutral'
        
    return label, score

# Apply sentiment analysis to preprocessed_reviews
df[['sentiment_label', 'sentiment_score']] = (
    df['preprocessed_reviews']
    .fillna('')
    .apply(lambda x: pd.Series(get_sentiment(x)))
)

# Aggregate: Mean sentiment by bank and rating
agg = df.groupby(['bank', 'rating'])['sentiment_score'].mean().reset_index()

# Save aggregated results and updated DataFrame
agg_output_path = r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiment_aggregates.csv'
sentiment_output_path = r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiment_reviews.csv'

agg.to_csv(agg_output_path, index=False)
df.to_csv(sentiment_output_path, index=False)

# Output results
print(f"Analyzed sentiment for {len(df)} reviews.")
print(agg)