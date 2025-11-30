import pandas as pd
import pytest

def test_sentiment_columns():
    # Load the sentiment data
    df = pd.read_csv(r'c:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiments_reviews.csv')
    
    # Check if sentiment columns exist
    assert 'sentiment_label' in df.columns, "Column 'sentiment_label' does not exist."
    assert 'sentiment_score' in df.columns, "Column 'sentiment_score' does not exist."
    
    # Check that sentiment labels are within expected values
    assert df['sentiment_label'].isin(['positive', 'negative', 'neutral']).all(), "Sentiment labels contain unexpected values."
    
    # Check that sentiment scores are numeric
    assert pd.api.types.is_numeric_dtype(df['sentiment_score']), "Sentiment scores should be numeric."
    
    # Check that sentiment scores are within expected range
    assert (df['sentiment_score'] >= -1.0).all() and (df['sentiment_score'] <= 1.0).all(), "Sentiment scores should be between -1.0 and 1.0."

# Run pytest when this script is executed
if __name__ == "__main__":
    pytest.main()