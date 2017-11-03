# The python implementation of ID3 algorithm
from math import log2


def ID3(dataset, pred_col_num):
    """
    The ID3 algorithm to grow a decision tree
    :param dataset: data set
    :param pred_col_num: predicting attribute's column number.
    :return: a built decision tree.
    """
    return 0

# Helper functions:
def infoGain(records, attr):
    """
    This function to calculate information needed to classify
    :param records: all tuples(rows) in a data set(or sub date set)
    :param attr: used to partition dataset into smaller sets of data.
    :return: return the entropy of information
    """
    return 0


def infoContent(col, distinct):
    """
    This function calculates the information content of the column of one attribute
    :param col: a list(column) of records
    :param distinct: a list distinct values
    :return: float
    """
    dis_dict = {}  # distinct value dictionary
    prob_dict = {} # probability of each value
    rec_num = len(col)
    for val in distinct:
        val_num = col.count(val)
        dis_dict.update({val: val_num})
        prob_dict.update({val: val_num / rec_num})
    # print(dis_dict)
    # print(prob_dict)
    info = 0
    for prob in prob_dict.values():
        if prob != 0:
            info += prob * log2(prob)
    return -1 * info

def aveInfoContent(table, split_attr, predict_attr):
    """

    :param table: a list of dictionaries
    :param split_attr: the attr which use to devide the table into n sub sets.
    :param predict_attr: predicting attr
    :return: float
    """
    col_split = []
    col_predict = []
    sub_pred_set = {}
    split_prob = {}
    for row in table:
        col_split.append(row[split_attr])
    distinct_split = set(col_split)

    for val in distinct_split:
        split_prob.update({val: col_split.count(val) / len(col_split)})

    # TODO





def readCSV(file):
    """
    This function reads table from csv.
    :param file:
    :return:
    """






