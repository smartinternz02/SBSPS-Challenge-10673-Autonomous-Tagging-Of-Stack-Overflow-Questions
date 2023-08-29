'''
All functions for preprocessing the data
'''
import pickle
import nltk
import string
import re
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

'''Load Pickel Files'''
token = pickle.load(open("./TokToktokenizerFinal.pkl", 'rb'))
lemma = pickle.load(open("./WordLemmaFinal.pkl", 'rb'))
tags_features = pickle.load(open("./tags_featureFinal.pkl", 'rb'))


def most_common(tags):
    tags_filtered = []
    for i in range(0, len(tags)):
        if tags[i] in tags_features:
            tags_filtered.append(tags[i])
    return tags_filtered

''' Import Tokenizer as Token 
token=ToktokTokenizer()
'''
def remove_punctuation(text):
    words=token.tokenize(text)
    filtered=[]
    for w in words:
        if w not in tags_features:
            new_w=w.translate(str.maketrans('', '', string.punctuation))
            filtered.append(new_w)
        else:
            filtered.append(w)
    s = " "
    s=s.join(filtered)
    return s

''' Regular Expression '''
def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub(r"\'\n", " ", text)
    text = re.sub(r"\'\xa0", " ", text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text

''' Lemmetization
    Lemma = WordNetLemmatizer()
 '''
def lemitizeWords(text):
    words=token.tokenize(text)
    listLemma=[]
    for w in words:
        x=lemma.lemmatize(w, pos="v")
        listLemma.append(x)
    return ' '.join(map(str, listLemma))

def stopWordsRemove(text):
    stop_words = set(stopwords.words("english"))
    words=token.tokenize(text)
    filtered = [w for w in words if not w in stop_words]
    return ' '.join(map(str, filtered))

def preprocess_text(text):
    text = clean_text(text)
    text = remove_punctuation(text)
    text = lemitizeWords(text)
    text = stopWordsRemove(text)
    return text

