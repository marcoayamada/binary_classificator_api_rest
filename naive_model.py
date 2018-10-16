# can't import
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import BernoulliNB

from sklearn.externals import joblib
import pickle
import numpy as np

classifier = joblib.load('./pickles/text_binary_clas.save')
vectorizer = pickle.load(open(r'vectorizer/list_frequency.vec', 'rb'))

def phrase_pred(body):
	phrases = body.get('phrases', None)
	preds = classifier.predict(vectorizer.transform(phrases)).tolist()

	result={}
	for a,b in zip(phrases, preds):
		result[a] = b

	return result