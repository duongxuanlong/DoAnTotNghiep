__author__ = 'long.duongxuan'


from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics

from GoogleNews import GoogleNewsParser


def algorithm_Kmean(pairs):
     #Google
    kmeans = KMeans(n_clusters=18, init='k-means++', n_init=100)
    kmeans.fit(pairs[1])
    print "Kmeans"

    print "Original label"
    print GoogleNewsParser.get_target_labels()
    print "Kmeans label"
    print kmeans.labels_
    # Google
    print "ARI: " + str(metrics.adjusted_rand_score(GoogleNewsParser.get_target_labels(), kmeans.labels_))
    print "NMI: " + str(metrics.adjusted_mutual_info_score(GoogleNewsParser.get_target_labels(), kmeans.labels_))


def algorithm_HAC(pairs):
    #Google
    result = AgglomerativeClustering(n_clusters=18, linkage='ward').fit(pairs[1])

    print "HAC"

    # Google
    print "ARI: " + str(metrics.adjusted_rand_score(GoogleNewsParser.get_target_labels(), result.labels_))
    print "NMI: " + str(metrics.adjusted_mutual_info_score(GoogleNewsParser.get_target_labels(), result.labels_))
    # for label in result.labels_:
    #     print str(label) + "\n"