import pandas as pd
import nltk
from stopwordsiso import stopwords
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import preprocess_string, strip_punctuation, strip_numeric, strip_short

# Load the CSV files into DataFrames
df_deleted = pd.read_csv('deleted.csv', low_memory=False)
df_metadata = pd.read_csv('metadata.csv', low_memory=False)
df_text = pd.read_csv('turkey_text.csv', low_memory=False)

# Merge df_metadata and df_text on the 'id' column
df = pd.merge(df_metadata, df_text, on='id', how='inner')

# Load Turkish stopwords from stopwords-iso
turkish_stopwords = stopwords(["tr"])

# Define a function to preprocess the text
def preprocess(text):
    custom_filters = [lambda x: x.lower(), strip_punctuation, strip_numeric, strip_short]
    return [word for word in preprocess_string(text, custom_filters) if word not in turkish_stopwords]

# Preprocess the text data
texts = df['text'].dropna().tolist()
processed_texts = [preprocess(text) for text in texts]

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_texts)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=10000)
corpus = [dictionary.doc2bow(text) for text in processed_texts]

# Train the LDA model with 5 topics
num_topics = 5
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15, random_state=42)

# Display the topics
print("LDA Topics:")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}")
    print("\n" + "="*50 + "\n")
