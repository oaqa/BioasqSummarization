import re, math
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter


class SimilarityMeasure(object):
    def __init__(self, sentence1, sentence2):
        self.sentence1 = sentence1
        self.sentence2 = sentence2
        self.stopWords = set(stopwords.words('english'))

    def calculateSimilarity(self, sentence1, sentence2):
        pass


class SimilarityJaccard(SimilarityMeasure):
	def calculateSimilarity(self, s1, s2):
		set1 = set([i.lower() for i in word_tokenize(self.sentence1) if i.lower() not in self.stopWords])
		set2 = set([i.lower() for i in word_tokenize(self.sentence2) if i.lower() not in self.stopWords])
		return float(len(set1.intersection(set2)))/len(set1.union(set2))


class SimilarityCosine(SimilarityMeasure):

    def text_to_vector(self, text):
        words = self.WORD.findall(text)
        return Counter(words)

    def calculateSimilarity(self):
        self.WORD = re.compile(r'\w+')
        vec1 = self.text_to_vector(self.sentence1)
        vec2 = self.text_to_vector(self.sentence2)

        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])

        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator