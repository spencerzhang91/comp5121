# An implementation of hierarchical agglomerative
from pprint import pprint
from kmeans import normalization, dist


def AggloHCsinlink(dataset: list):
    '''
    Agglomerative Hierarchical Clustering using single-linkage method.
    The input is a 2d list, for example:
    dataset = [[row1], [row2], ..., [rown]]
    :param dataset: dataset
    :return: list
    '''
    distmx = gen_dist_matrix(dataset)
    cluster_num = len(dataset)
    while cluster_num > 1:
        min_dist_array = []  # This array tracks min distance pair at one round
        for i in range(len(distmx)):
            curr_min = None
            for j in range(len(distmx)):
                curr_dist = dist(dataset[i], dataset[j])
                if i == j:
                    continue
                if curr_min is None:
                    curr_min = curr_dist
                if curr_min > curr_dist:
                    curr_min = curr_dist
            min_dist_array.append(curr_min)
            print(min_dist_array)
        cluster_num -= 1


def gen_dist_matrix(dataset):
    '''
    Generates the distance matrix for a dataset.
    :param dataset: 2d list
    :return: ad list
    '''
    return [[]]
