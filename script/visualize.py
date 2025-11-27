import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv('analyzed_reviews.csv')

# Sentiment distribution
sns.countplot(data=df, x='sentiment', hue='bank')
plt.title('Sentiment Distribution by Bank')
plt.savefig('sentiment_dist.png')

# Ratings over time
df['date'] = pd.to_datetime(df['date'])
df.groupby(['date', 'bank'])['rating'].mean().unstack().plot()
plt.title('Average Rating Over Time')
plt.savefig('ratings_time.png')

# Word cloud for negative reviews
negative_text = ' '.join(df[df['sentiment'] == 'negative']['review'])
wordcloud = WordCloud(width=800, height=400).generate(negative_text)
wordcloud.to_file('negative_wordcloud.png')