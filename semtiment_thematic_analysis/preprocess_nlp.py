# preprocess_nlp.py
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load spaCy model (assume en_core_web_sm downloaded)
nlp = spacy.load('en_core_web_sm')

# Load cleaned data
df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\cleaned_reviews.csv')

# Preprocessing function
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.is_alpha]
    return ' '.join(tokens)
# Fix NaN / floats
df["review"] = df["review"].fillna("").astype(str)
# Apply preprocessing
df['processed_review'] = df['review'].apply(preprocess_text)

# Save preprocessed data
df.to_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data/preprocessed_reviews.csv', index=False)
print(f"Preprocessed {len(df)} reviews.")