import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df_russia = pd.read_csv('russian_tweets.csv', low_memory=False)

# Convert 'tweet_time' column to datetime
df_russia['tweet_time'] = pd.to_datetime(df_russia['tweet_time'])

# Filter for May 2022
may_2022_russia = df_russia[(df_russia['tweet_time'] >= '2016-01-01') & (df_russia['tweet_time'] <= '2016-12-30')]

# Resampling by day to get daily tweet counts for May 2022
russia_daily = may_2022_russia.resample('D', on='tweet_time').size()

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
rolling_mean = russia_daily.rolling(window=30).mean()

# Plotting the temporal distribution and rolling mean (trend)
plt.figure(figsize=(10, 5))
plt.plot(russia_daily, label='Daily Tweet Count')
plt.plot(rolling_mean, color='red', label='30-Day Rolling Mean')
plt.title('Temporal Distribution and Trend of Bot Tweets from Russia in 2016')
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