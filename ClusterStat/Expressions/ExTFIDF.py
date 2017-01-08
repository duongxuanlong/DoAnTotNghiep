__author__ = 'Long'

from sklearn.feature_extraction.text import TfidfVectorizer


class TfIdf:
    """
    TfIdf use pure documents as input(not split)
    """
    def __init__(self):
        self.mVectorizor = None
        self.mResult = None
        self.mDense = None

    def fit_data(self, corpus):
        # vectorizer = TfidfVectorizer(min_df=1)
        self.mVectorizor = TfidfVectorizer(min_df=1)
        # X = vectorizer.fit_transform(corpus)
        self.mResult = self.mVectorizor.fit_transform(corpus)
        # idf = vectorizer.idf_
        # dense = X.todense()
        self.mDense = self.mResult.todense()
        print "Length of TFIDF: " + str(len(self.mDense))
        # print self.mVectorizor.idf_
        # dense = self.mResult.todense()
        # print self.mResult.todense()

