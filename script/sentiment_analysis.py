import pandas as pd
from transformers import pipeline

# Load preprocessed data
df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\preprocessed_reviews.csv')

# Initialize DistilBERT sentiment pipeline
sentiment_pipeline = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

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

# Apply to processed reviews
df[['sentiment_label', 'sentiment_score']] = df['processed_review'].apply(lambda x: pd.Series(get_sentiment(x)))

# Aggregate: Mean sentiment by bank and rating
agg = df.groupby(['bank', 'rating'])['sentiment_score'].mean().reset_index()
agg.to_csv('sentiment_aggregates.csv', index=False)

# Save updated DF
df.to_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiments_reviews.csv', index=False)
print(f"Analyzed sentiment for {len(df)} reviews.")
print(agg)