import abc
from abc import abstractmethod

from flask import Flask, request, abort
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import logging
from logging import config

'''
@Author: Khyathi Raghavi Chandu
@Date: October 17 2017

This code contains the abstract class for the BiRanker.
'''

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('bioAsqLogger')

'''
This is an Abstract class that serves as a template for implementations for:
ranking among sentences and ranking with question.
'''
class BiRanker:
	__metaclass__ = abc.ABCMeta
	@classmethod
	def __init__(self):
		self.alpha = 0.5
		self.numSelectedSentences = 10

	@abstractmethod
	def getRankedList(self):
		pass

	@classmethod
	def getSentences(self, question):

		sentences = []
		snippetsText = []
		for snippet in question['snippets']:
			text = unicode(snippet["text"]).encode("ascii", "ignore")
			snippetsText.append(text)
			if text == "":
				continue
			try:
				sentences += sent_tokenize(text)
			except:
				sentences += text.split(". ") # Notice the space after the dot
		return sentences

	@classmethod
	def computePositions(self,snippets):
		pos_dict = {}
		max_rank = len(snippets)
		rank = 0
		for snippet in snippets:
			snippet = unicode(snippet["text"]).encode("ascii","ignore")
			more_sentences = [i.lstrip().rstrip() for i in sent_tokenize(snippet)]
			#print more_sentences
			#rint more_sentences
			#w_input()
			for sentence in more_sentences:
				if sentence not in pos_dict:
				  pos_dict[sentence] = 1-(float(rank)/max_rank)
			rank += 1
		logger.info('Computed position dictionary for Bi Ranking')
		return pos_dict
