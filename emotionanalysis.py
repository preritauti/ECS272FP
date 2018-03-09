'''
(1) Creates dictionary with raw tweet, id, date
(2) Preprocessing on tweets (stemming/lemmatizing)
'''
import re
import argparse
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordLemmatizer
import pickle
#from preprocess import preprocessTweets, createDictFromFile


if __name__=="__main__":
	# for testing
	filename="data/@BarackObama_tweets_dict.p"
	#filename=''

	parser=argparse.ArgumentParser()
	parser.add_argument('filename',action='store', help="Complete path of pickled (preprocessed tweets) file")
	args=parser.parse_args() 
		
	if not filename:
		filename=args.filename

	# dictionary storing all values 
	tweetdata=pickle.load(open(filename))

	for tweetid in tweetdata:
		for word in tweetdata[tweetid]['words']:
			
	