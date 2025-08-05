import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df_deleted = pd.read_csv('deleted.csv', low_memory=False)
df_metadata = pd.read_csv('metadata.csv', low_memory=False)
df_text = pd.read_csv('turkey_text.csv', low_memory=False)

# Merge df_metadata and df_text on the 'id' column
df = pd.merge(df_metadata, df_text, on='id', how='inner')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Ensure that the 'content' column is a string and handle missing data
df['text'] = df['text'].fillna('').astype(str)

# Apply VADER sentiment analysis to each tweet's content
df['sentiment'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Overall Sentiment Analysis
overall_sentiment = df['sentiment'].mean()
print(f"Overall Sentiment Score: {overall_sentiment}")

# Convert 'publish_date' to datetime for time-based analysis
df['created_at'] = pd.to_datetime(df['created_at'])

# Aggregate sentiment over time (e.g., by day, week, or month)
df['month'] = df['created_at'].dt.to_period('M')  # Group by month
monthly_sentiment = df.groupby('month')['sentiment'].mean()

# Plotting Overall Sentiment Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['sentiment'], bins=30, kde=True)
plt.title('Overall Sentiment Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Plotting Sentiment Over Time
plt.figure(figsize=(12, 6))
monthly_sentiment.plot(marker='o')
plt.title('Sentiment Over Time')
plt.xlabel('Month')
plt.ylabel('Average Sentiment Score')
plt.grid(True)
plt.show()