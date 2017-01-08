__author__ = 'Long'

from GoogleNews import GoogleNewsParser
from Expressions import ExTFIDF
from Expressions import ExD2V
import os
from gensim.models.doc2vec import Doc2Vec
import Algorithm

import sys


def main():
    # print sys.stdout.encoding
    #Running tfidf
    # parser = GoogleNewsParser.NewsParsers()
    # parser.parse_data_from_tok()

    # tfidf = ExTFIDF.TfIdf()
    # tfidf.fit_data(parser.get_texts())
    # parser.get_texts()
    # print parser.get_texts()

    # running TF-IDF
    parser = GoogleNewsParser.NewsParsers()
    parser.parse_data_from_tok()
    tfidf = ExTFIDF.TfIdf()
    tfidf.fit_data(parser.get_texts())

    # running doc2vec
    # run_doc2vec()

    # algorithm with d2v representation
    # algorithm_d2v()
    # GoogleNewsParser.get_target_labels()


def algorithm_d2v():
    # load_d2v()
    # Algorithm.algorithm_Kmean(load_d2v())
    Algorithm.algorithm_HAC(load_d2v())


def load_d2v():
    print "load_d2v"
    pairs = []
    module = Doc2Vec.load(os.getcwd() + "\\google.d2v")
    print "length " + str(len(module.docvecs))
    labels = GoogleNewsParser.get_only_labels(os.getcwd() + "\\clusters")
    docs = []
    for i in range(len(labels)):
        docs.append(module.docvecs[labels[i]])
    pairs.append(labels)
    pairs.append(docs)
    return pairs


def run_doc2vec():
    print "run_doc2vec"
    path = os.getcwd() + "\\clusters"
    pairs = GoogleNewsParser.get_docs_labels(path=path)
    documents = ExD2V.DocIterator(pairs[0], pairs[1])
    model = Doc2Vec(size=100, window=10, min_count=1, workers=4, alpha=0.025, min_alpha=0.025)
    model.build_vocab(documents)
    for epoch in range(10):
        model.train(documents)
        model.alpha -= 0.002
        model.min_alpha = model.alpha
    print "length of model : " + str(len(model.docvecs))
    model.save(os.getcwd() + "\\google.d2v")


if __name__ == '__main__':
    main()
