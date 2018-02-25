from deiis.model import DataSet, Question, Serializer
from deiis.rabbit import Task, Message

import logging
from logging import config
logging.config.fileConfig('logging.ini')

try:
    basestring
except:
    basestring = str


class ResultsCollector(Task):
    """
    The last service in any pipeline.  The ResultsCollector collects all the
    ranked sentences in a list object and then writes the list to a file when
    it receives a ``SAVE`` command message.
    """

    def __init__(self, host='localhost'):
        super(ResultsCollector, self).__init__('results', host=host)
        self.logger.info('Created Results task')
        self.count = 0
        self.questions = list()

    def perform(self, input):
        self.logger.info('Received results')

        question = Question(input)
        self.logger.debug("Received results for question %s", question.id)
        self.questions.append(question)

        # if isinstance(message.body, basestring):
        #     print message.body
        # elif isinstance(message.body, list):
        #     for i, question in enumerate(message.body):
        #         print '{}. {}'.format(i, question)
        # else:
        #     self.logger.error("Unhandled message body type: " + str(type(message.body)))
        #     print str(message.body)

    def command(self, cmd):
        if cmd == 'SAVE':
            self.logger.info('Received the SAVE command')
            parts = cmd.split(' ')
            if (len(parts) > 1):
                self.save(parts[1])
            else:
                self.save()
        elif cmd == 'RESET':
            self.logger.inf0('Received the RESET command')
            self.questions = list()
        else:
            self.logger.error('Recevied and unknown command: ' + cmd)

    def save(self, path=None):
        if path is None:
            path = '/tmp/submission.json'

        self.logger.debug("Saving dataset to %s", path)
        dataset = DataSet()
        dataset.questions = self.questions
        json = Serializer.to_pretty_json(dataset)
        fp = open(path, 'w')
        fp.write(json)
        fp.close()
        self.logger.info("Wrote %s", path)
        self.questions = []