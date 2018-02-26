import abc
from abc import abstractmethod

import os

from deiis.rabbit import Task
import logging
from logging import config

'''
@Author: Khyathi Raghavi Chandu
@Date: October 17 2017

This is an Abstract Class to perform Concept Expansions. This class cannot be instantiated as all the abstract methods are not
implemented.
The subclass that extends the abstract class is valid if and only if all the abstract methods are implemented.
'''

logging.config.fileConfig('logging.ini')
# logger = logging.getLogger('bioAsqLogger')

class NoneExpander(Task):
	__metaclass__ = abc.ABCMeta
	def __init__(self, route, host='localhost'): #constructor for the abstract class
		super(NoneExpander, self).__init__('expand.none', host=host)

	def perform(self, sentence):
		return sentence



#If this part is uncommented in the code and run then it should throw an error because the abstract methods are not implemented.
'''
instance = Expander("John has cancer")
print instance.getExpansions()
'''
