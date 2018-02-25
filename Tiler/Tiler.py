import abc
from abc import abstractmethod

from deiis.rabbit import Task
from deiis.model import Question

'''
@Author: Khyathi Raghavi Chandu
@Date: October 17 2017

This code contains the abstract class for Tiler.
'''


'''
This is an Abstract class that serves as a template for implementations for tiling sentences.
Currently there is only one technique implemented which is simple concatenation.
'''
class Tiler(Task):
	#__metaclass__ = abc.ABCMeta
	#@classmethod
	def __init__(self, route, host='localhost'):
		super(Tiler, self).__init__(route, host=host) #, host='172.17.0.2')

	def perform(self, input):
		question = Question(input)
		#TODO exact or ideal answer should be parameterized.
		question.exact_answer = self.tileSentences(question.ranked, 7)
		return question

	#abstract method that should be implemented by the subclass that extends this abstract class
	@abstractmethod
	def tileSentences(self, sentences, pred_length):
		pass
	

'''
instance = Tiler(["John"," has cancer"])
print instance.sentenceTiling()
'''
