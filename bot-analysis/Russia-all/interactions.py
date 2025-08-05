import pandas as pd

# Load your dataframe (assuming it's named df)
df = pd.read_csv('russian_tweets.csv')

# Replace NaN with 0 for interaction columns
df[['quote_count', 'reply_count', 'like_count', 'retweet_count']] = df[['quote_count', 'reply_count', 'like_count', 'retweet_count']].fillna(0)

# Calculate the average of each type of interaction per tweet
avg_quote_count = df['quote_count'].mean()
avg_reply_count = df['reply_count'].mean()
avg_like_count = df['like_count'].mean()
avg_retweet_count = df['retweet_count'].mean()

# Calculate the total interactions per tweet
df['total_interactions'] = df[['quote_count', 'reply_count', 'like_count', 'retweet_count']].sum(axis=1)

# Calculate the average total interactions per tweet
avg_total_interactions = df['total_interactions'].mean()

# Compare the average total interactions per tweet for tweet types
avg_total_interactions_original = df[df['is_retweet'] == False]['total_interactions'].mean()
avg_total_interactions_retweet = df[df['is_retweet'] == True]['total_interactions'].mean()

# Print the results
print(f"Average Quote Count per Tweet: {avg_quote_count}")
print(f"Average Reply Count per Tweet: {avg_reply_count}")
print(f"Average Like Count per Tweet: {avg_like_count}")
print(f"Average Retweet Count per Tweet: {avg_retweet_count}")
print(f"Average Total Interactions per Tweet: {avg_total_interactions}")
print(f"Average Total Interactions per Original Tweet: {avg_total_interactions_original}")
print(f"Average Total Interactions per Retweet: {avg_total_interactions_retweet}")
