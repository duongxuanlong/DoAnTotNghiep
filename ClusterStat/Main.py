__author__ = 'Long'

from GoogleNews import GoogleNewsParser
from Expressions import ExTFIDF

import sys

def main():
    # print sys.stdout.encoding
    parser = GoogleNewsParser.NewsParsers()
    parser.parse_data_from_tok()

    tfidf = ExTFIDF.TfIdf()
    tfidf.fit_data(parser.get_texts())
    # parser.get_texts()
    # print parser.get_texts()

if __name__ == '__main__':
    main()