import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('libya_narratives.csv')

# Convert 'post_date' to datetime for time-based analysis
df['post_date'] = pd.to_datetime(df['post_date'])

# Group the data by month to analyze changes over time
df['month'] = df['post_date'].dt.to_period('M')

# Ensure all reaction columns are numeric
df[['Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Thankful']] = df[['Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Thankful']].apply(pd.to_numeric, errors='coerce')

# Fill NaNs with 0
df.fillna(0, inplace=True)

# Summing the reactions by month
monthly_reactions = df.groupby('month')[['Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Thankful']].sum()

# Plotting the reactions over time
plt.figure(figsize=(14, 8))
sns.lineplot(data=monthly_reactions)
plt.title('Reactions to Bot Posts Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Reactions')
plt.legend(title='Reaction Type')
plt.grid(True)
plt.show()

