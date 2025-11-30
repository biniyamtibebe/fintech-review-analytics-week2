import pandas as pd
import spacy
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
    logging.info("Loaded spaCy model successfully.")
except Exception as e:
    logging.error(f"Error loading spaCy model: {e}")
    raise

# Load cleaned data
input_path = r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\cleaned_reviews.csv'

# Check if the file exists
if not os.path.exists(input_path):
    logging.error(f"Input file does not exist: {input_path}")
    raise FileNotFoundError(f"Input file not found: {input_path}")

df = pd.read_csv(input_path)

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
output_path = r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\preprocessed_reviews.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure directory exists

df.to_csv(output_path, index=False)
logging.info(f"Preprocessed {len(df)} reviews and saved to {output_path}.")