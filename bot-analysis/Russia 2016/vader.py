import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('IRAhandle_tweets_6.csv', low_memory=False)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Ensure that the 'content' column is a string and handle missing data
df['content'] = df['content'].fillna('').astype(str)

# Apply VADER sentiment analysis to each tweet's content
df['sentiment'] = df['content'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Overall Sentiment Analysis
overall_sentiment = df['sentiment'].mean()
print(f"Overall Sentiment Score: {overall_sentiment}")

# Convert 'publish_date' to datetime for time-based analysis
df['publish_date'] = pd.to_datetime(df['publish_date'])

# Aggregate sentiment over time (e.g., by day, week, or month)
df['month'] = df['publish_date'].dt.to_period('M')  # Group by month
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
