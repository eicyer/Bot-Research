import pandas as pd

# Load your dataframe (assuming it's named df)
df = pd.read_csv("IRAhandle_tweets_6.csv")

# Replace NaN with 0 for interaction columns (assuming 'retweet' is the interaction metric)
df['retweet'] = df['retweet'].fillna(0)

# Calculate the average of retweets (as it seems to be the primary interaction metric)
avg_retweet_count = df['retweet'].mean()

# Since there seems to be only retweet interaction, total interactions will be equal to retweets
df['total_interactions'] = df['retweet']

# Calculate the average total interactions per tweet
avg_total_interactions = df['total_interactions'].mean()

# Compare the average total interactions per tweet for each post type (assuming post_type differentiates tweet types)
avg_total_interactions_by_post_type = df.groupby('post_type')['total_interactions'].mean()

# Print the results
print(f"Average Retweet Count per Tweet: {avg_retweet_count}")
print(f"Average Total Interactions per Tweet: {avg_total_interactions}")
print("\nAverage Total Interactions per Post Type:")
print(avg_total_interactions_by_post_type)
