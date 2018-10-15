from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np

classifier = joblib.load('./pickles/text_binary_clas.save')
vectorizer = pickle.load(open(r'vectorizer/list_frequency.vec', 'rb'))

def phrase_pred(phrase):
    aaa = phrase.get("p1", None)
    x = np.array([aaa])
    return str(classifier.predict(vectorizer.transform(x)).tolist())