import pandas as pd
import pytest

def test_themes():
    df = pd.read_csv('analyzed_reviews.csv')
    assert 'themes' in df.columns
    # Check at least 2 themes on average
    avg_themes = df['themes'].apply(lambda x: len(x.split(',')) if x else 0).mean()
    assert avg_themes >= 2