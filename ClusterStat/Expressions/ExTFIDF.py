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
        self.mResult = self.mVectorizor.fit_transform(corpus).toarray()
        # idf = vectorizer.idf_
        # dense = X.todense()
        # self.mDense = self.mResult.todense()
        print str(len(self.mResult[0]))
        # print "Length of TFIDF: " + str(len(self.mDense))
        # print "length of data: " + str(len(self.mDense.data))
        # print "Row length: " + str(len(self.mDense[0]))
        # index = 0
        # for row in self.mDense:
        #     print row
        #     if index == 0:
        #         break
        # print "First Row: :"
        # print self.mDense[0][0]
        # print self.mDense

        # print self.mVectorizor.idf_
        # dense = self.mResult.todense()
        # print self.mResult.todense()

    def get_data_as_vector(self):
        return self.mResult

