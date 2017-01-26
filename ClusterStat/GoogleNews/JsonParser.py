__author__ = 'Long'

import os
import codecs
import json


def get_docs_labels(path):
    pairs = []
    docs = []
    labels = []

    list_dirs = os.listdir(path)
    for curdir in list_dirs:
        for root, dirs, files in os.walk(path + "\\" + curdir):
            for txt in files:
                if txt.endswith(".tok.json"):
                    file_path = os.path.join(root, txt)
                    # print file_path
                    # file_txt = open(file_path, "r")
                    file_txt = codecs.open(file_path, "r", "utf-8")
                    result_json = json.dumps(file_txt.read())
                    print result_json
                    # docs.append(file_txt.read())
                    newlabel = get_label(file_path)
                    # labels.append(txt)
                    labels.append(newlabel)
                    file_txt.close()
    pairs.append(docs)
    pairs.append(labels)
    return pairs


def get_label(file_path):
    parts = file_path.split('\\')
    index = len(parts)
    newpath = parts[index - 2] + "_" + parts[index - 1]
    # print newpath
    return newpath

