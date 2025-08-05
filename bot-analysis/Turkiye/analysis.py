import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df_deleted = pd.read_csv('deleted.csv')
df_metadata = pd.read_csv('metadata.csv')
df_text = pd.read_csv('turkey_text.csv')
# Print the schema of the DataFrame (column names and their data types)

# First, merge df_metadata and df_text on the 'id' column
merged_df = pd.merge(df_metadata, df_text, on='id', how='inner')

df_turkey = merged_df

df_turkey['created_at'] = pd.to_datetime(df_turkey['created_at'])

# Filter for May 2022
may_2022_turkey = df_turkey[(df_turkey['created_at'] >= '2022-05-16') & (df_turkey['created_at'] <= '2022-05-30')]

# Resampling by day to get daily tweet counts for May 2022
russia_daily = may_2022_turkey.resample('D', on='created_at').size()

mean_value = russia_daily.mean()
std_deviation = russia_daily.std()
median_value = russia_daily.median()
min_value = russia_daily.min()
max_value = russia_daily.max()

# Print the statistical measures
print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Median: {median_value}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")

# Calculate rolling mean (for trend analysis)
rolling_mean = russia_daily.rolling(window=7).mean()

# Plotting the temporal distribution and rolling mean (trend)
plt.figure(figsize=(10, 5))
plt.plot(russia_daily, label='Daily Tweet Count')
plt.plot(rolling_mean, color='red', label='7-Day Rolling Mean')
plt.title('Temporal Distribution and Trend of Bot Tweets in Turkey')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.legend()
plt.grid(True)
plt.show()


if not russia_daily.empty:
    skewness = russia_daily.skew()
    kurtosis = russia_daily.kurt()

    print(f"Skewness: {skewness}")
    print(f"Kurtosis: {kurtosis}")