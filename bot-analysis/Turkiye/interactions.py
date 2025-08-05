import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df_deleted = pd.read_csv('deleted.csv')
df_metadata = pd.read_csv('metadata.csv')
df_text = pd.read_csv('turkey_text.csv')
# Print the schema of the DataFrame (column names and their data types)

# First, merge df_metadata and df_text on the 'id' column
df = pd.merge(df_metadata, df_text, on='id', how='inner')

# Replace NaN with 0 for interaction columns
df[['quote_count', 'reply_count']] = df[['quote_count', 'reply_count']].fillna(0)

# Calculate the average of each type of interaction per tweet
avg_retweet_count = df['retweet_count'].mean()
avg_favorite_count = df['favorite_count'].mean()
avg_quote_count = df['quote_count'].mean()
avg_reply_count = df['reply_count'].mean()

# Calculate the total interactions per tweet
df['total_interactions'] = df[['retweet_count', 'favorite_count', 'quote_count', 'reply_count']].sum(axis=1)

# Calculate the average total interactions per tweet
avg_total_interactions = df['total_interactions'].mean()

# Compare the average total interactions per tweet for each tweet type
avg_total_interactions_by_type = df.groupby('tweet_type')['total_interactions'].mean()

# Print the results
print(f"Average Retweet Count per Tweet: {avg_retweet_count}")
print(f"Average Favorite Count per Tweet: {avg_favorite_count}")
print(f"Average Quote Count per Tweet: {avg_quote_count}")
print(f"Average Reply Count per Tweet: {avg_reply_count}")
print(f"Average Total Interactions per Tweet: {avg_total_interactions}")
print("\nAverage Total Interactions per Tweet Type:")
print(avg_total_interactions_by_type)
