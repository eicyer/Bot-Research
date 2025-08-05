# 🛰️ Comparative Analysis of Bot Behavior Across Geopolitical Events

This repository supports the research paper titled **"Comparative Analysis of Bot Behavior Across Different Geopolitical Events to Evaluate Bot Strategy and Impact"**, exploring how bot campaigns function in different international contexts using real-world Twitter/X datasets.

## 📊 Objective

Analyze bot activity across four key datasets to understand:
- Temporal tweet patterns
- Interaction behavior (likes, retweets, comments)
- Narrative strategies via Topic Modeling (LDA)
- Sentiment and tone of messages (VADER)
- Impact of coordinated vs. non-coordinated bot operations

## 🗂️ Datasets Used

| Dataset | Description |
|--------|-------------|
| **Russia (General, 2012–2018)** | From the Twitter Moderation Research Consortium |
| **Russia (2016 US Election)** | From the FiveThirtyEight IRA dataset |
| **Turkey (May 2022)** | From Elmas (2023) — Ephemeral Astroturfing Dataset |
| **Libya (April 2019)** | From Grossman et al. — Harvard Dataverse |

> Due to licensing and size, raw datasets are not hosted here. You may access them from the original sources linked in the paper.

## 🧪 Methodology

- **Temporal Analysis**: `pandas` resampling & descriptive stats
- **Trend Detection**: 30-day rolling means
- **Topic Modeling**: `gensim` LDA models on preprocessed text
- **Sentiment Analysis**: `vaderSentiment` for emotional tone scoring
- **Visualization**: `matplotlib` for daily activity plots and sentiment histograms

## 🧾 Example Usage

```python
# Load and preprocess Russian dataset
df_russia = pd.read_csv('russian_tweets.csv', low_memory=False)
df_russia['tweet_time'] = pd.to_datetime(df_russia['tweet_time'])

# Filter for 2016
df_2016 = df_russia[(df_russia['tweet_time'] >= '2016-01-01') & (df_russia['tweet_time'] <= '2016-12-30')]
daily_counts = df_2016.resample('D', on='tweet_time').size()

# Stats
print("Mean:", daily_counts.mean())
print("Kurtosis:", daily_counts.kurt())
