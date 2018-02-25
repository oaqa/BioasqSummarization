from BiRanker import *
from CoreMMR import CoreMMR

import logging
from logging import config

logging.config.fileConfig('logging.ini')


# Class that inherits the class CoreMMR which extends the abstract class BiRanker
class HardMMR2(CoreMMR):

    # constructor to instantiate CoreMMR since we want to change certain class variables, which are shown as follows
    def __init__(self, host='localhost', alpha=0.5, selected=1):
        super(HardMMR2, self).__init__(route='mmr.hard2', host=host, alpha=alpha, selected=selected)
        self.pos_dict = {}

    # abstract method that takes a question and returns a string
    def getRankedList(self, question):
        # selectedSentences = []
        # snippets = question.snippets
        self.beta = 0
        snippet = unicode(question.snippets[0].text).encode("ascii", "ignore")  # first snippet
        sentences = [i.lstrip().rstrip() for i in sent_tokenize(snippet)]

        # selecting 1 sentence from the first snippet
        selected_sents = self.getRankedList(question)

        summary = selected_sents[0]
        leftover = set(sentences).difference(set(selected_sents))

        for snippet in question.snippets[1:]:
            snippet = unicode(snippet.text).encode("ascii", "ignore")
            more_sentences = [i.lstrip().rstrip() for i in sent_tokenize(snippet)]
            leftover = leftover.union(set(more_sentences))
        # selecting the remaining 9 sentences from the leftover
        self.sentences = list(leftover)
        # The class variable that is set to 1 in the constructor is changed here
        self.numSelectedSentences = 9
        selected_sents = self.getRankedList(question)
        self.logger.info('Performed Hard Constrainted MMR')
        return selected_sents

