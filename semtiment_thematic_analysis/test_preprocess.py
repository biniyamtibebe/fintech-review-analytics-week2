import pandas as pd
import pytest

def test_preprocessing():
    df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\preprocessed_reviews.csv')
    assert 'processed_review' in df.columns
    assert df['processed_review'].notnull().all()  # No empty after preprocess