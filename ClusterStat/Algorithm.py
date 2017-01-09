__author__ = 'long.duongxuan'


from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics

from GoogleNews import GoogleNewsParser


def algorithm_Kmean(pairs):
    # Number of full clusters: 2305
    # Number of half clusters: 1236
    # Number of quad clusters: 495 : 4 - 10
    # Number of eight: 262 : 4 - 6
    # Number of one cluster: 147
    print "algorithm Kmean"
     #Google
    kmeans = KMeans(n_clusters=147, init='k-means++', n_init=100)
    if (len(pairs) == 2):
        kmeans.fit(pairs[1])
    else:
        kmeans.fit(pairs)
    print "Kmeans"

    print "Original label"
    print GoogleNewsParser.get_target_labels()
    print "Kmeans label"
    print kmeans.labels_
    # Google
    print "ARI: " + str(metrics.adjusted_rand_score(GoogleNewsParser.get_target_labels(), kmeans.labels_))
    print "NMI: " + str(metrics.adjusted_mutual_info_score(GoogleNewsParser.get_target_labels(), kmeans.labels_))


def algorithm_HAC(pairs):
    print "algorithm HAC"
    #Google
    hac = AgglomerativeClustering(n_clusters=147, linkage='ward')

    if len(pairs) == 2:
        hac.fit(pairs[1])
    else:
        hac.fit(pairs)

    print "HAC"

    # Google
    print "ARI: " + str(metrics.adjusted_rand_score(GoogleNewsParser.get_target_labels(), result.labels_))
    print "NMI: " + str(metrics.adjusted_mutual_info_score(GoogleNewsParser.get_target_labels(), result.labels_))
    # for label in result.labels_:
    #     print str(label) + "\n"