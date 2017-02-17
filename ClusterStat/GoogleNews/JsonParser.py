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
                    # result_json = json.dumps(file_txt.read(), separators=(',', ':'))
                    result_json = json.load(file_txt)
                    docs.append(result_json["Content"])
                    # print result_json["Content"]
                    # print result_json
                    # print "Length of json: " + str(len(result_json))
                    # docs.append(file_txt.read())
                    newlabel = get_label(file_path)
                    print newlabel
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


def get_only_labels(path):
    labels = []
    for root, dirs, files in os.walk(path):
        for txt in files:
            if txt.endswith(".tok.json"):
                file_path = os.path.join(root, txt)
                label = get_label(file_path)
                labels.append(label)
                # labels.append(txt)
    return labels


def get_target_labels():
    # path = os.getcwd() + "\\Data"
    path = os.getcwd() + "\\clusters"
    labels = []
    dirs = os.listdir(path)
    # print dirs
    # idx = 0
    label = 0
    for single_dir in dirs:
        for root, sedirs, files in os.walk(path + "\\" + single_dir):
            for childdirs in sedirs:
                newpath = path + "\\" + single_dir + "\\" + childdirs
                # print newpath
                for newroot, newdirs, newfiles in os.walk(newpath):
                    for txt in newfiles:
                        if txt.endswith(".tok.json"):
                            labels.append(label)
                label += 1
    print "Length of labels : " + str(len(labels))
    return labels


def get_texts(path):
    docs = []

    list_dirs = os.listdir(path)
    for curdir in list_dirs:
        for root, dirs, files in os.walk(path + "\\" + curdir):
            for txt in files:
                if txt.endswith(".tok.json"):
                    file_path = os.path.join(root, txt)
                    file_txt = codecs.open(file_path, "r", "utf-8")
                    result_json = json.load(file_txt)
                    docs.append(result_json["Content"])
                    file_txt.close()

    print "length of docs: " + str(len(docs))
    return docs

