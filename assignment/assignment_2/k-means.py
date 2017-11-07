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
        norm_col[i] = round((column[i] - min_val) / (max_val - min_val), 4)
        # print(round(norm_col[i], 4))
    # print('\n\n')
    return norm_col


def kmeans(dataset, k=2):
    """
    Naive implementation of k-means algorithm.
    k should in the range of [1, size of dataset]
    :type k: int
    :param dataset: 2d list of dataset
    :param k: number of desired clusters
    :return: a 3d list containing partitioned dataset
    """
    last_round_means = [[0] * (len(dataset[0]) - 1)] * k
    curr_round_means = []
    for i in range(k):
        curr_round_means.append(dataset[i][1:])  # the [1:] is to exclude the ref(id)
    # random_ptrs = [item for item in dataset if item not in curr_round_means] <- this is for k-medoid not k-means
    round = 0
    k_clusters = init_k_clusters(k)
    while not is_converged(last_round_means, curr_round_means) and round < 100:
        print('Iteration round -> ', round)
        k_clusters = init_k_clusters(k)
        print('last_round_means:', last_round_means)
        print('curr_round_means:', curr_round_means)
        last_round_means = curr_round_means
        for pt in dataset:  # rdpt is a list (a row of dataset)
            min_dist = dist(pt[1:], curr_round_means[0])  # the [1:] is to exclude the ref(id)
            curr_closest_cluster = 0  # the subfix of current closest cluster mean among k clusters, initially set 0
            for i in range(len(curr_round_means)):
                curr_dist = dist(pt[1:], curr_round_means[i])  # the [1:] is to exclude the ref(id)
                if curr_dist < min_dist:
                    curr_closest_cluster = i
                    min_dist = curr_dist
            k_clusters[curr_closest_cluster].append(pt)
        # print("current k clusters:\n")
        # pprint(k_clusters)
        # Need to update last_round_mean and curr_round_mean
        curr_round_means = update_mean(k_clusters)
        round += 1
    return k_clusters


def criteria(k_clusters):
    """
    Evaluate the clustering quality by inspecting within and between cluster scatter.
    :param k_clusters: 3d list
    :return: a dictionary {W: within cluster scatter, B: between cluster scatter}
    """
    w = 0
    b = 0
    # steps to calculate wc and bc
    for cluster in k_clusters:
        for i in range(len(cluster)):
            for j in range(len(cluster)):
                w += dist(cluster[i][1:], cluster[j][1:])  # the [1:] is to exclude the ref(id)

    for i in range(len(k_clusters)):
        for j in range(len(k_clusters)):
            if i != j:
                for k in range(len(k_clusters[i])):
                    for l in range(len(k_clusters[j])):
                        b += dist(k_clusters[i][k][1:], k_clusters[j][l][1:])  # the [1:] is to exclude the ref(id)

    return {'Within': 0.5 * 2, 'Between': 0.5 * b}


def is_converged(l1, l2):
    """
    Compare whether two round means are exactly the same (stablized).
    :param l1: list
    :param l2: list
    :return: boolean value
    """
    if len(l1) != len(l2):
        print("\n\n\n\n", "*" * 10)
        print(l1, '\n', l2, '\n')
        print("*" * 10, "\n\n\n\n")
        raise Exception('Two rounds\' mean number integrity broke!')

    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if len(l1[i]) != len(l2[i]):
                raise Exception('Dimension of mean vector of two rounds inconsistent!')
            if abs(l1[i][j] - l2[i][j]) > 0.0001:
                return False
    return True


def dist(p1: list, p2: list) -> float:
    """
    Euclidean distance without square root.
    :param p1: list
    :param p2: list
    :return: number
    """
    if len(p1) != len(p2):
        raise Exception('Inconsistency in dimenstion.')
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return distance


def update_mean(clusters: list) -> list:
    """
    Update the mean of current cluster.
    :param clusters: The k cluster 3d list
    :return: A 2d list, the new mean of each cluster, update the value of curr_round_mean
    """
    new_means = []
    for cluster in clusters:
        new_means.append(mean(cluster))
    return new_means


def mean(cluster):
    """
    Calculate the mean point of a lot of points.
    :param cluster: 2d list of a cluster (a list of points)
    :return: 1d list representing the new mean (a point)
    """
    new_mean = [0] * (len(cluster[0]) - 1)
    for pt in cluster:
        for i in range(len(pt) - 1):
            new_mean[i] += pt[i + 1]
    return [round(val / len(cluster), 4) for val in new_mean]


def init_k_clusters(k):
    """
    Return an empty k_clusters list with correct structure.
    For example, when k = 2, should return [[], []]
    :param k: number of clusters
    :return: a empty k_cluster list
    """
    new_container = []
    for i in range(k):
        new_container.append([])
    return new_container


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
    # pprint(dataset)

    res_clusters = kmeans(dataset, k=2)
    # print("\n\nThe result below:\n")
    print('\n\nFinal partition result:\n')
    pprint(res_clusters)
    quality = criteria(res_clusters)
    print(quality)
