import pandas as pd
import pytest

def test_no_duplicates():
    df = pd.read_csv('Data/cleaned_reviews.csv')
    assert df.duplicated(subset=['review']).sum() == 0

def test_no_missing():
    df = pd.read_csv('Data/cleaned_reviews.csv')
    assert df[['review', 'rating']].isnull().sum().sum() == 0