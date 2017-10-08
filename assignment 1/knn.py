from pprint import pprint

def knn(neighbors:list, point:list, K:int):
    '''
    Calculate the distances between the point and its neighbors.
    For assignment 1 only.
    '''
    for neighbor in neighbors:
        neighbor['dis2p'] = dist((point['ANF'],point['ANMF'],point['NDPC']),
                                 (neighbor['ANF'],neighbor['ANMF'],neighbor['NDPC'])
                                 )
    sorted_neighbors = sorted(neighbors, key=lambda k: k['dis2p'])
    # pprint(neighbors)
    print("******* below sorted *******\n")
    pprint(sorted_neighbors)

def knn_regression(neighbors:list, point:list, K:int):
    '''
    Use K-NN to solve regression problem.
    For assignment 1 only.
    '''
    for neighbor in neighbors:
        neighbor['dis2p'] = dist((point['ANF'],point['NDPC']),
                                 (neighbor['ANF'],neighbor['NDPC'])
                                 )
    sorted_neighbors = sorted(neighbors, key=lambda k: k['dis2p'])
    # pprint(neighbors)
    pprint(sorted_neighbors)



def dist(point:tuple, target:tuple):
    '''
    Return the distance of the two points.
    '''
    distance = 0
    if len(point) != len(target):
        print(point)
        print(target)
        raise Exception('Wrong dimension comparation!')
    for i in range(len(point)):
        distance += (point[i] - target[i]) ** 2
    return distance ** 0.5

def find_max(neighbors, *args):
    '''
    Find max value of the whole value space
    '''
    curr_max = [None] * len(args)
    for i in range(len(args)):
        curr_max[i] = neighbors[0][args[i]]
    # this loop below finds the bigges value of a feature
    for neighbor in neighbors:
        for j in range(len(args)):
            if neighbor[args[j]] > curr_max[j]:
                curr_max[j] = neighbor[args[j]]
            # print(curr_max)
    return curr_max

def find_min(neighbors, *args):
    '''
    Find min value of the whole value space.
    '''
    curr_min = [None] * len(args)
    for i in range(len(args)):
        curr_min[i] = neighbors[0][args[i]]
    # this loop below finds the smallest value of a feature
    for neighbor in neighbors:
        for j in range(len(args)):
            if neighbor[args[j]] < curr_min[j]:
                curr_min[j] = neighbor[args[j]]
            # print(curr_mix)
    return curr_min

def norm(neighbors, max_vals, min_vals, *args):
    # this loop below normalizes the values
    norm_neighbors = neighbors.copy()
    for neighbor in norm_neighbors:
        for k in range(len(args)):
            # below the normalization formula:
            neighbor[args[k]] = (neighbor[args[k]] - min_vals[k])/(max_vals[k] - min_vals[k])
    return norm_neighbors


if __name__ == "__main__":

    neighbors = [{'id':1,  'ANF':29, 'ANMF':2921.8,'NDPC':879, 'dicision':'R','dis2p':0},
                 {'id':2,  'ANF':62, 'ANMF':2867.3,'NDPC':705, 'dicision':'D','dis2p':0},
                 {'id':3,  'ANF':17, 'ANMF':2440.5,'NDPC':929, 'dicision':'R','dis2p':0},
                 {'id':4,  'ANF':34, 'ANMF':2113.3,'NDPC':223, 'dicision':'D','dis2p':0},
                 {'id':5,  'ANF':50, 'ANMF':2437.8,'NDPC':724, 'dicision':'D','dis2p':0},
                 {'id':6,  'ANF':11, 'ANMF':2187.6,'NDPC':143, 'dicision':'U','dis2p':0},
                 {'id':7,  'ANF':9,  'ANMF':2691.1,'NDPC':1015,'dicision':'U','dis2p':0},
                 {'id':8,  'ANF':34, 'ANMF':2921.1,'NDPC':335, 'dicision':'U','dis2p':0},
                 {'id':9,  'ANF':39, 'ANMF':1592.3,'NDPC':975, 'dicision':'D','dis2p':0},
                 {'id':10, 'ANF':73, 'ANMF':2804.9,'NDPC':544, 'dicision':'U','dis2p':0},
                 {'id':11, 'ANF':78, 'ANMF':2685.1,'NDPC':84,  'dicision':'D','dis2p':0},
                 {'id':12, 'ANF':25, 'ANMF':2741.6,'NDPC':100, 'dicision':'U','dis2p':0},
                 {'id':13, 'ANF':80, 'ANMF':2401.2,'NDPC':800, 'dicision':'R','dis2p':0},
                 {'id':14, 'ANF':50, 'ANMF':1929.7,'NDPC':882, 'dicision':'R','dis2p':0},
                 {'id':15, 'ANF':45, 'ANMF':3370.0,'NDPC':707, 'dicision':'U','dis2p':0}]

    point = [{'id':16, 'ANF':25, 'ANMF':2050.0,'NDPC':790, 'dicision':'','dis2p':0}]
    point2 = [{'id':17, 'ANF':58, 'ANMF':0,'NDPC':650, 'dicision':'','dis2p':0}]

    K = 5

    # a)
    neighbors_a = neighbors.copy()
    print("\n\nFrom below is problem a)\n")
    max_values = find_max(neighbors_a+point, 'ANF', 'ANMF', 'NDPC')
    min_values = find_min(neighbors_a+point, 'ANF', 'ANMF', 'NDPC')
    print(max_values)
    print(min_values)
    norm_neighbors = norm(neighbors_a, max_values, min_values, 'ANF', 'ANMF', 'NDPC')
    norm_point = norm(point, max_values, min_values, 'ANF', 'ANMF', 'NDPC')

    pprint(norm_neighbors)

    knn(norm_neighbors, norm_point[0], K)

    # b)
    print("\n\nFrom below is problem b)\n")
    max_values_r = find_max(neighbors+point2, 'ANF', 'NDPC')
    min_values_r = find_min(neighbors, 'ANF', 'NDPC')
    print(max_values_r)
    print(min_values_r)
    norm_neighbors_r = norm(neighbors, max_values_r, min_values_r, 'ANF', 'NDPC')
    norm_point_r = norm(point2, max_values_r, min_values_r, 'ANF', 'NDPC')

    knn_regression(norm_neighbors_r, norm_point_r[0], K)
