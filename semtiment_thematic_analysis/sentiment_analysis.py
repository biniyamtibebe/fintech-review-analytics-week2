import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "4"  # stop TF logs

import torch
from transformers import pipeline
import pandas as pd

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

# sentiment analysis 
import pandas as pd
from transformers import pipeline
import torch as torch

 # <-- FIXED

# Load preprocessed data
df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\preprocessed_reviews.csv')

import re

def remove_amharic(text):
    if pd.isna(text):
        return text
    # Ethiopic script ranges: \u1200–\u137F
    return re.sub(r'[\u1200-\u137F]+', '', text)

df['preprocessed_reviews'] = df['review'].apply(remove_amharic)

# Initialize DistilBERT sentiment pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"   # <--- Forces PyTorch
)

# Function to get sentiment
def get_sentiment(text):
    if not text.strip():  # Skip empty
        return 'neutral', 0.0
    result = sentiment_pipeline(text)[0]
    label = result['label'].lower()
    score = result['score'] if label == 'positive' else -result['score']
    if abs(score) < 0.1:  # Threshold for neutral
        label = 'neutral'
    return label, score

def get_sentiment(text):
    if not isinstance(text, str) or not text.strip():  # handle NaN, None, empty
        return 'neutral', 0.0
    
    result = sentiment_pipeline(text)[0]
    label = result['label'].lower()
    score = result['score'] if label == 'positive' else -result['score']
    
    # threshold small signals as neutral
    if abs(score) < 0.1:
        label = 'neutral'
        
    return label, score
#Apply sentiment to processed_review
df[['sentiment_label', 'sentiment_score']] = (
    df['processed_review']
    .fillna('')
    .apply(lambda x: pd.Series(get_sentiment(x)))
)


# Aggregate: Mean sentiment by bank and rating
agg = df.groupby(['bank', 'rating'])['sentiment_score'].mean().reset_index()
agg.to_csv('sentiment_aggregates.csv', index=False)

# Save updated DF
df.to_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiments_reviews.csv', index= False)
print(f"Analyzed sentiment for {len(df)} reviews.")
print(agg)