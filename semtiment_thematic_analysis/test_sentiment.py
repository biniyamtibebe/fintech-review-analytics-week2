#test sentiment 
import pandas as pd 
import pandas as pd
import pytest

def test_sentiment_columns():
    df = pd.read_csv(r'c:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiments_reviews.csv')
    assert 'sentiment_label' in df.columns
    assert 'sentiment_score' in df.columns
    assert df['sentiment_label'].isin(['positive', 'negative', 'neutral']).all()