import pandas as pd
import matplotlib.pyplot as plt

df_libya = pd.read_csv("libya_narratives.csv")
# Assuming df_libya is your dataframe for Libya bot posts
df_libya['post_date'] = pd.to_datetime(df_libya['post_date'])
russia_daily = df_libya.resample('D', on='post_date').size()

# Assuming russia_daily is your resampled daily tweet counts

# Calculate statistical measures
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
plt.title('Temporal Distribution and Trend of Bot Tweets in Libya')
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