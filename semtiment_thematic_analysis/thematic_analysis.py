# Thematic Analysis (Keyword Extraction & Clustering)
'Extract keywords/n-grams using TF-IDF (weights important terms) and spaCy (for phrases). '
'Then, rule-based cluster into 3-5 themes per bank (document logic, e.g., if keyword contains "login/error", assign to "Account Access Issues"). '
'This identifies themes like "Transaction Performance" (pain point: slow transfers) or "Feature Requests" (driver: fingerprint login)'

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from collections import Counter

# Load data with sentiments
df = pd.read_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\sentiments_reviews.csv')
#Add this before calling vectorizer.fit_transform(...):
df['processed_review'] = df['processed_review'].fillna("")

# TF-IDF for keyword extraction
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, ngram_range=(1,3), stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['processed_review'])
feature_names = vectorizer.get_feature_names_out()

# Get top keywords per review
def top_keywords(row, top_n=5):
    row_index = row.name
    row_values = tfidf_matrix[row_index].toarray().flatten()
    top_indices = row_values.argsort()[-top_n:]
    return [feature_names[i] for i in top_indices]

df['keywords'] = df.apply(top_keywords, axis=1)

# Use spaCy for better n-grams/entities
nlp = spacy.load('en_core_web_sm')
def extract_ngrams(text):
    doc = nlp(text)
    ngrams = [chunk.text for chunk in doc.noun_chunks]
    return ngrams[:5]  # Top 5

df['ngrams'] = df['processed_review'].apply(extract_ngrams)

# Combine keywords and ngrams
df['all_phrases'] = df.apply(lambda row: list(set(row['keywords'] + row['ngrams'])), axis=1)

# Rule-based clustering into themes (document logic)
theme_rules = {
    'Account Access Issues': ['login', 'error', 'password', 'access', 'authentication'],
    'Transaction Performance': ['slow', 'transfer', 'loading', 'speed', 'crash', 'bug'],
    'User Interface & Experience': ['ui', 'design', 'easy', 'user friendly', 'navigation'],
    'Customer Support': ['support', 'help', 'customer service', 'response'],
    'Feature Requests': ['fingerprint', 'biometric', 'new feature', 'add', 'request']
}

def assign_themes(phrases):
    themes = []
    for theme, keywords in theme_rules.items():
        if any(any(kw in p.lower() for kw in keywords) for p in phrases):
            themes.append(theme)
    return themes if themes else ['Other']

df['themes'] = df['all_phrases'].apply(assign_themes)

# Aggregate themes per bank
theme_agg = df.explode('themes').groupby(['bank', 'themes']).size().reset_index(name='count')
theme_agg = theme_agg[theme_agg['themes'] != 'Other']  # Filter if needed
print(theme_agg)

# Ensure 3+ themes per bank (if not, adjust rules)
for bank in df['bank'].unique():
    bank_themes = theme_agg[theme_agg['bank'] == bank]
    print(f"{bank}: {bank_themes['themes'].unique()}")

# Save final analyzed CSV (review, ..., sentiment_label, sentiment_score, themes as comma-str)
df['themes'] = df['themes'].apply(lambda x: ','.join(x))
df.to_csv(r'C:\Users\hp\Pictures\fintech-review-analytics\fintech-review-analytics-week2\Data\thematicanalyzed_reviews.csv', index=False)