## Import Area:
# run:
# python -m nltk.downloader stopwords
# python -m nltk.downloader punkt
# python -m nltk.downloader averaged_perceptron_tagger
# pip install --user -U nltk

# python -m spacy download en
# python -m spacy download en_core_web_md
# conda install -c conda-forge spacy

import re
import spacy
from collections import Counter
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Word2sec and Stop_words
word2sec = spacy.load('en_core_web_md')
stop_words = set(stopwords.words("english"))

# Preprocess func
def preprocess(input_sentence):
    # Lowercase all input sentence
    input_sentence = input_sentence.lower()
    # Explain later ****
    input_sentence = re.sub(r'[^\w\s]','', input_sentence)
    tokens = word_tokenize(input_sentence)
    input_sentence = [i for i in tokens if not i in stop_words]
    return(input_sentence)

# Compare Overlap Func
def compare_overlap(user_message, possible_response):
    # Set similar_word equal to 0
    similar_words = 0
    # Check each token/word in user message in condition if token/word in possible_response
    # Then count 1 into similiar_word
    for token in user_message:
        if token in possible_response:
            similar_words += 1
    return similar_words

# Extract Noun Func
def extract_nouns(tagged_message):
    # Explain later ***
    message_nouns = list()
    for token in tagged_message:
        if token[1].startswith("N"):
            message_nouns.append(token[0])
    return message_nouns

# Compute Similarity func
def compute_similarity(tokens, category):
    output_list = list()
    for token in tokens:
        output_list.append([token.text, category.text, token.similarity(category)])
    return output_list

