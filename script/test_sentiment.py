import pandas as pd
import pytest

def test_sentiment_columns():
    df = pd.read_csv('sentiments_reviews.csv')
    assert 'sentiment_label' in df.columns
    assert 'sentiment_score' in df.columns
    assert df['sentiment_label'].isin(['positive', 'negative', 'neutral']).all()