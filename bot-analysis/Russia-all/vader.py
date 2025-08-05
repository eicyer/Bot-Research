import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('russian_tweets.csv', low_memory=False)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Ensure that the 'tweet_text' column is a string and handle missing data
df['tweet_text'] = df['tweet_text'].fillna('').astype(str)

# Apply VADER sentiment analysis to each tweet's content
df['sentiment'] = df['tweet_text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Convert 'tweet_time' to datetime for time-based analysis
df['tweet_time'] = pd.to_datetime(df['tweet_time'])

# Filter data between November 2015 and January 2018
start_date = '2015-11-01'
end_date = '2018-01-31'
mask = (df['tweet_time'] >= start_date) & (df['tweet_time'] <= end_date)
df_filtered = df.loc[mask]

# Calculate the average sentiment in this period
average_sentiment = df_filtered['sentiment'].mean()
print(f"Average Sentiment Score from November 2015 to January 2018: {average_sentiment}")

# Aggregate sentiment over time within this period (e.g., by month)
df_filtered['month'] = df_filtered['tweet_time'].dt.to_period('M')
monthly_sentiment = df_filtered.groupby('month')['sentiment'].mean()

# Plotting Overall Sentiment Distribution for the filtered period
plt.figure(figsize=(10, 6))
sns.histplot(df_filtered['sentiment'], bins=30, kde=True)
plt.title('Sentiment Distribution (November 2015 to January 2018)')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Plotting Sentiment Over Time for the filtered period
plt.figure(figsize=(12, 6))
monthly_sentiment.plot(marker='o')
plt.title('Sentiment Over Time (November 2015 to January 2018)')
plt.xlabel('Month')
plt.ylabel('Average Sentiment Score')
plt.grid(True)
plt.show()
