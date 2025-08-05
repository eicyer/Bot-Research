import pandas as pd
df = pd.read_csv("libya_narratives.csv")
interaction_columns = ['Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Thankful']
df[interaction_columns] = df[interaction_columns].fillna(0)

# Calculate the average of each type of interaction per tweet
avg_likes = df['Likes'].mean()
avg_comments = df['Comments'].mean()
avg_shares = df['Shares'].mean()
avg_love = df['Love'].mean()
avg_wow = df['Wow'].mean()
avg_haha = df['Haha'].mean()
avg_sad = df['Sad'].mean()
avg_angry = df['Angry'].mean()
avg_thankful = df['Thankful'].mean()

# Calculate the total interactions per tweet
df['total_interactions'] = df[interaction_columns].sum(axis=1)

# Calculate the average total interactions per tweet
avg_total_interactions = df['total_interactions'].mean()

# Compare the average total interactions per tweet for each value of 'plurality' (or any other categorical variable)
avg_total_interactions_by_plurality = df.groupby('plurality')['total_interactions'].mean()
avg_total_interactions_by_plurality_sorted = avg_total_interactions_by_plurality.sort_values(ascending=False)
# Print the results
tweets_count_by_plurality = df['plurality'].value_counts()

# Filter to show only the pluralities of interest
pluralities_of_interest = ['UK', 'Jordan', 'Netherlands', 'Location hidden', 'Malta', "Qatar", "Russia"]
tweets_count_by_plurality_filtered = tweets_count_by_plurality.loc[pluralities_of_interest]

# Print the results
print("Number of Tweets Sent from Each Plurality:")
print(tweets_count_by_plurality_filtered)


avg_post_views = df['Post.Views'].mean()

# Calculate the average Total.Views per tweet
avg_total_views = df['Total.Views'].mean()

# Print the results
import pandas as pd

# Load your dataframe (assuming it's named df)
# df = pd.read_csv('your_file.csv')

# Replace NaN with 0 for interaction columns that could be missing
interaction_columns = ['Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Thankful']
df[interaction_columns] = df[interaction_columns].fillna(0)

# Calculate the total interactions per tweet
df['total_interactions'] = df[interaction_columns].sum(axis=1)

# Calculate the avg total_interactions/total_views value
df['interaction_per_view'] = df['total_interactions'] / df['Total.Views']
avg_interaction_per_view = df['interaction_per_view'].mean()

# Handle cases where Total.Views is 0 to avoid division by zero (optional, depending on your data)
df['interaction_per_view'] = df['interaction_per_view'].replace([float('inf'), -float('inf')], 0).fillna(0)

# Calculate the total views per plurality
total_views_by_plurality = df.groupby('plurality')['Total.Views'].mean()

# Get the top 5 pluralities with the most total views
top_5_pluralities_by_views = total_views_by_plurality.sort_values(ascending=False).head(5)

# Print the results
print(f"Average Total Interaction per Total View: {avg_interaction_per_view}")
print("\nTop 5 Pluralities with Most Total Views:")
print(top_5_pluralities_by_views)

# Load your dataframe (assuming it's named df)
# df = pd.read_csv('your_file.csv')

# Replace NaN with 0 for interaction columns that could be missing
interaction_columns = ['Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Thankful']
df[interaction_columns] = df[interaction_columns].fillna(0)

# Calculate the total interactions per tweet
df['total_interactions'] = df[interaction_columns].sum(axis=1)

# Calculate the average views per tweet for the specified pluralities
pluralities_of_interest_views = ['UK', 'Malta', 'Location hidden', 'Jordan', 'Netherlands']
avg_views_per_tweet = df[df['plurality'].isin(pluralities_of_interest_views)].groupby('plurality')['Total.Views'].mean()

# Calculate the average interactions per tweet for the specified pluralities
pluralities_of_interest_interactions = ['Qatar', 'Jordan', 'Russia', 'UK', 'Netherlands']
avg_interactions_per_tweet = df[df['plurality'].isin(pluralities_of_interest_interactions)].groupby('plurality')['total_interactions'].mean()

# Print the results
print("Average Views per Tweet for Selected Pluralities:")
print(avg_views_per_tweet)
print("\nAverage Interactions per Tweet for Selected Pluralities:")
print(avg_interactions_per_tweet)
