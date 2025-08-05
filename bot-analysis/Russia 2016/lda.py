import pandas as pd
import nltk
from stopwordsiso import stopwords
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import preprocess_string, strip_punctuation, strip_numeric, strip_short

# Load the dataset
df = pd.read_csv('IRAhandle_tweets_6.csv', low_memory=False)

# Convert 'publish_date' to datetime
df['publish_date'] = pd.to_datetime(df['publish_date'])

# Filter tweets from 2016 only and in English
filtered_df = df[(df['publish_date'].dt.year == 2016)]

# Check if the filtered dataset is empty
if filtered_df.empty:
    print("The filtered dataframe is empty. Check the filter conditions.")
else:
    print(f"Number of tweets after filtering: {len(filtered_df)}")

# Load English stopwords
english_stopwords = stopwords(["en"])

# Define a function to preprocess the text
def preprocess(text):
    custom_filters = [lambda x: x.lower(), strip_punctuation, strip_numeric, strip_short]
    return [word for word in preprocess_string(text, custom_filters) if word not in english_stopwords]

# Preprocess the text data
texts = filtered_df['content'].dropna().tolist()
processed_texts = [preprocess(text) for text in texts]

# Check if processed_texts contains valid documents
if not processed_texts:
    print("No valid documents after preprocessing.")
else:
    print(f"Number of documents after preprocessing: {len(processed_texts)}")

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_texts)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=10000)
corpus = [dictionary.doc2bow(text) for text in processed_texts]

# Check if the corpus is empty
if not corpus:
    print("The corpus is empty after processing. Adjust the preprocessing steps.")
else:
    # Train the LDA model with 6 topics
    num_topics = 6
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15, random_state=42)

    # Display the topics
    print("LDA Topics:")
    for idx, topic in lda_model.print_topics(-1):
        print(f"Topic {idx}: {topic}")
        print("\n" + "="*50 + "\n")
