import abc
from abc import abstractmethod

import os

from deiis.rabbit import Task
import logging
from logging import config

'''
'''

logging.config.fileConfig('logging.ini')
# logger = logging.getLogger('bioAsqLogger')

class NoneExpander(Task):
	__metaclass__ = abc.ABCMeta
	def __init__(self, host='localhost'): #constructor for the abstract class
		super(NoneExpander, self).__init__('expand.none', host=host)

	def perform(self, sentence):
		return sentence

