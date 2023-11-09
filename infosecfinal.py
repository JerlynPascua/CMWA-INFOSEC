import streamlit as st
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import pandas as pd
import streamlit as st


def detect_profanity(profanity):
    # Assuming profanity_words.csv has a 'profanity' column with the profanity words
    df = pd.read_csv('profanity.csv')
    profanity_words = df['text'].tolist()

    for word in profanity_words:
        if word in profanity.lower():
            return True
    return False

st.title("Profanity Detector")
user_input = st.text_input("Enter a message to check for profanity:")

if user_input:
    if detect_profanity(user_input):
        st.write("There is a profanity in this message.")
    else:
        st.write("This message does not contain any profanity.")
