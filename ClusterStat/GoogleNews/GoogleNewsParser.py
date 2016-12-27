__author__ = 'long.duongxuan'

import os
from gensim import corpora
import NewsData
# import nltk


class NewsParsers:
    def __init__(self):
        self.mText_Data = []
        self.mFrequent_Doc = []
        self.mFolder = "\\clusters"
        self.mExtension = ".tok"
        
    def parse_data_from_tok(self):
        print "parse_data_from_tok"
        # path = os.getcwd() + "\\Data"
        path = os.getcwd() + self.mFolder
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for se_file in files:
                    file_path = os.path.join(root, se_file)
                    print "File Path : {}".format(file_path)
                    # print "FileNames : {}".format(se_file)
                    # print "Root : {}".format(root)
                    # if file_path.endswith(".tok"):
                    if file_path.endswith(self.mExtension):
                        news_data = NewsData.NewsData()
                        split_dirs = root.split("\\")
                        news_data.mFileName = split_dirs[-1] + "_" + se_file
                        news_data.mFullPath = file_path
                        # print "File Name : {}".format(news_data.mFileName)
                        f = open(file_path, "r")
                        text = f.read()
                        news_data.mText_Doc = text.split()
                        self.mText_Data.append(news_data)
        print "Number of Text_Doc {}".format(str(len(self.mText_Data)))
                        # print "Text {}".format(text)
                # print "Root : {}".format(root)
                # for child_dir in dirs:
                #     child_dir_path = os.path.join(root, child_dir)
                #     print "child_dir_path : {} ".format(child_dir_path)
                #     for child_dir_root, se_dir, se_files in os.walk(child_dir_path):
                #         for se_file in se_files:
                #             if se_file.endswith("tok"):
                #                 file_path = os.path.join(child_dir_root, se_file)
                #                 f = open(file_path, "r")
                #                 text = f.read()
                #                 print "File Name : {}".format(f.name)
                #                 print "Text : {}".format(text)
                #                 self.mText_Doc.append(text)
                #                 f.close()

    def parse_data_into_matrix(self):
        path = os.getcwd()

        texts = []
        for data in self.mText_Data:
            texts.append(data.mText_Doc)

        dictionary = corpora.Dictionary(texts)
        print "Dictionary length : {}".format(str(len(texts)))
        dictionary.save(path + "\\dictionary.dict")

        corpus = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(path + "\\corpus.mm", corpus)

        print "Number of docs : {}".format(str(dictionary.num_docs))
        print "Number of words: {}".format(str(len(dictionary.token2id.items())))

        features = len(dictionary.token2id.items())
        path += "\\Matrix"
        row = 1
        set_doc_terms = []
        for doc in corpus:
            doc_terms = [0] * features
            if len(doc) > 0:
                row += 1
                for term in doc:
                    doc_terms[term[0]] = term[1]
                set_doc_terms.append(doc_terms)
        matrix = open(path + "\\matrix.txt", "w")
        for line in set_doc_terms:
            for i in range(len(line)):
                matrix.write(str(line[i]) + " ")
            matrix.write("\n")
        matrix.close()
        print "Actual Rows : {}".format(str(row))

    def get_texts(self):
        data = []
        for text in self.mText_Data:
            data.append(text.mText_Doc)
        return data

    def run(self):
        self.parse_data_from_tok()
        self.parse_data_into_matrix()


def get_docs_labels(path):
    pairs = []
    docs = []
    labels = []

    for root, dirs, files in os.walk(path):
        for txt in files:
            if txt.endswith(".tok"):
                file_path = os.path.join(root, txt)
                file_txt = open(file_path, "r")
                docs.append(file_txt.read())
                labels.append(txt)
                file_txt.close()
    pairs.append(docs)
    pairs.append(labels)
    return pairs


def get_only_labels(path):
    labels = []
    for root, dirs, files in os.walk(path):
        for txt in files:
            if txt.endswith(".tok"):
                labels.append(txt)
    return labels


def get_target_labels():
    path = os.getcwd() + "\\Data"
    labels = []
    dirs = os.listdir(path)
    # print dirs
    # idx = 0
    label = 0
    for single_dir in dirs:
        for root, sedirs, files in os.walk(path + "\\" + single_dir):
            for txt in files:
                if txt.endswith(".tok"):
                    labels.append(label)
        label += 1
    # print labels
    return labels
