# K-means algorithm implementation
from pprint import pprint


def normalization(column):
    """
    Normalize a column of data
    :param column: list
    :return: list
    """
    max_val = max(column)
    min_val = min(column)
    norm_col = column.copy()
    for i in range(len(column)):
        norm_col[i] = (column[i] - min_val) / (max_val - min_val)
        # print(round(norm_col[i], 4))
    # print('\n\n')
    return norm_col


def kmeans(dataset, k=2):
    """
    Naive implementation of k-means algorithm.
    :param dataset: 2d list of dataset
    :param k: number of desired clusters
    :return: a 3d list containing partitioned dataset
    """
    k_clusters = []
    last_round_mean = []
    curr_round_mean = []
    for i in range(k):
        k_clusters.append([dataset[i]])
        curr_round_mean.append(dataset[i])
    random_ptrs = [item for item in dataset if item not in curr_round_mean]
    print("current k clusters:", k_clusters)
    print("curr_round_mean:", curr_round_mean)

    while is_different(last_round_mean, curr_round_mean):
        last_round_mean = curr_round_mean
        for rdpt in random_ptrs:
            # pt is a list (a row of dataset)
            min_dist = dist(rdpt, curr_round_mean[0])
            curr_closest_cluster = 0  # the subfix of current closest cluster mean among k clusters
            for i in range(len(curr_round_mean)):

                curr_dist = dist(rdpt, curr_round_mean[i])
                if curr_dist < dist(rdpt, curr_round_mean[0]):
                    curr_closest_cluster = i
                    min_dist = curr_dist
            k_clusters[curr_closest_cluster].append(rdpt)
        # Need to update {last_round_mean and curr_round_mean
        curr_round_mean = update_mean(k_clusters) # TODO


def is_different(l1, l2):
    """
    Compare whether two lists are exactly equal.
    :param l1: list
    :param l2: list
    :return: boolean value
    """
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def dist(p1: list, p2: list) -> int:
    """
    Euclidean distance without square root.
    :param p1: list
    :param p2: list
    :return: number
    """
    if len(p1) != len(p2):
        raise Exception("Inconsistency in dimenstion.")
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return distance


if __name__ == "__main__":
    """
    Here goes multiple test cases of this problem.
    """

    # Below is the dataset from the assignment 2 of comp 5121
    # columns:
    ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    age = [54, 59, 38, 18, 27, 29, 17, 22, 34, 46, 38, 35, 39, 18]
    sex = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
    income = [3000, 4000, 7800, 8500, 14000, 31000, 7500, 7900, 24700, 31110, 21000, 30000, 40500, 7800]
    married = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]
    service = [100, 600, 200, 600, 100, 1600, 600, 200, 100, 600, 600, 1600, 1600, 1000]
    extra = [0, 54, 31, 311, 211, 25, 254, 31, 7, 0, 64, 0, 50, 290]

    # normalization of data:
    norm_age = normalization(age)
    norm_income = normalization(income)
    norm_service = normalization(service)
    norm_extra = normalization(extra)

    # data consitency check
    if not len(age) == len(sex) == len(income) == len(married) == len(service) == len(extra):
        raise Exception('Unmatching row number')

    dataset = [[ref[i], norm_age[i], sex[i], norm_income[i], married[i], norm_service[i], norm_extra[i]] for i in
               range(len(ref))]
    pprint(dataset)

    kmeans(dataset)
