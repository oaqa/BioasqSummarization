from deiis.model import Serializer, DataSet

data = Serializer.parse(open('./input/BioASQ-trainingDataset5b.json'), DataSet)
for q in data.questions:
    print q.id
#print data