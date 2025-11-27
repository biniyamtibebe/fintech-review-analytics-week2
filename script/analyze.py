import pandas as pd
from textblob import TextBlob
from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Load cleaned data
df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\cleaned_reviews.csv')

# Sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

df['sentiment'] = df['review'].apply(get_sentiment)

# Thematic analysis (keyword extraction)
rake = Rake()
def extract_themes(text):
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()[:5]  # Top 5 themes

df['themes'] = df['review'].apply(extract_themes)

# Group by bank and sentiment
summary = df.groupby(['bank', 'sentiment']).size().unstack()
print(summary)

# Identify common pain points (e.g., filter negative reviews for keywords)
pain_points = df[df['sentiment'] == 'negative']['review'].str.contains('slow|crash|error|bug', regex=True).sum()
print(f"Complaints related to speed/crashes: {pain_points}")

# Save analyzed data
df.to_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\analyzed_reviews.csv', index=False)