import pandas as pd
import nltk
from nltk.corpus import stopwords
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import preprocess_string, strip_punctuation, strip_numeric, strip_short
from sklearn.feature_extraction.text import CountVectorizer

# Load the dataframe
df = pd.read_csv('russian_tweets.csv', low_memory=False)

# Fix SSL issue and download stopwords
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Define a function to preprocess the text
def preprocess(text):
    custom_filters = [lambda x: x.lower(), strip_punctuation, strip_numeric, strip_short]
    return [word for word in preprocess_string(text, custom_filters) if word not in stop_words]

# Apply preprocessing
texts = df['tweet_text'].dropna().tolist()
processed_texts = [preprocess(text) for text in texts]

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_texts)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=10000)
corpus = [dictionary.doc2bow(text) for text in processed_texts]

# Train the LDA model
num_topics = 10
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15, random_state=42)

# Display the topics
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}:")
    print(topic)
    print("\n")
