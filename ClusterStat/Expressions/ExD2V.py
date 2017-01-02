__author__ = 'Long'

import gensim
from gensim.models.doc2vec import Doc2Vec



class DocIterator:
    def __init__(self, doclist, labellist):
        self.DocList = doclist
        self.LabelList = labellist

    def __iter__(self):
        for idx, doc in enumerate(self.DocList):
            # yield gensim.models.doc2vec.LabeledSentence(words=doc.split(), labels=[self.LabelList[idx]])
            yield gensim.models.doc2vec.TaggedDocument(doc.split(), [self.LabelList[idx]])

