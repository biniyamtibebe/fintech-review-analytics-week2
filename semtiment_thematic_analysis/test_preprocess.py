import pandas as pd
import pytest

# Test preprocessing function
def test_preprocessing():
    # Load the preprocessed data
    df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\preprocessed_reviews.csv')
    
    # Check if the processed_review column exists
    assert 'processed_review' in df.columns, "Column 'processed_review' does not exist."
    
    # Check that there are no empty values in the processed_review column
    assert df['processed_review'].notnull().all(), "There are empty values in 'processed_review'."
    
    # Check data type of processed_review to ensure it's a string
    assert df['processed_review'].dtype == 'object', "The data type of 'processed_review' should be string."
    
    # Check if the length of processed reviews matches the original reviews
    assert len(df['processed_review']) == len(df), "Mismatch in number of reviews after preprocessing."
    
    # Test for non-empty strings (optional)
    assert (df['processed_review'].str.strip() != '').all(), "Some processed reviews are empty strings."

# Run pytest when this script is executed
if __name__ == "__main__":
    pytest.main()