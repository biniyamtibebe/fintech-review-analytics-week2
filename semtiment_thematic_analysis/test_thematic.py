import pandas as pd
import pytest

def test_themes():
    # Load the thematic analysis data
    df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\thematicanalyzed_reviews.csv')

    # Check if the 'themes' column exists
    assert 'themes' in df.columns, "Column 'themes' does not exist."

    # Check that there are no missing values in the 'themes' column
    assert df['themes'].notnull().all(), "There are missing values in the 'themes' column."

    # Check at least 2 themes on average
    avg_themes = df['themes'].apply(lambda x: len(x.split(',')) if x else 0).mean()
    assert avg_themes >= 2, f"Average number of themes is {avg_themes}, expected at least 2."

    # Check the maximum number of themes in a single entry (optional)
    max_themes = df['themes'].apply(lambda x: len(x.split(',')) if x else 0).max()
    assert max_themes > 0, "There should be at least one theme in some entries."
    
    print(f"Average themes: {avg_themes}")

# Run pytest when this script is executed
if __name__ == "__main__":
    pytest.main()
    