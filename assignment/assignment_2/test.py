# Test for created classes.

from ID3 import *
import sqlite3
conn = sqlite3.connect('recommendation.db')
c = conn.cursor()
try:
    c.execute("DROP TABLE training")
    c.execute("DROP TABLE testing")
except sqlite3.OperationalError:
    print("Starts new test below:\n")
else:
    print("Starts new test below clean:\n")

# create training data table
c.execute("CREATE TABLE training (id integer NOT NULL PRIMARY KEY , gender text, sp text, ast text, tpr text, reco text)")
c.execute("INSERT INTO training VALUES (1, 'M', 'M', 'Y', 'R', 'L')")
c.execute("INSERT INTO training VALUES (2, 'F', 'M', 'N', 'R', 'S')")
c.execute("INSERT INTO training VALUES (3, 'M', 'H', 'Y', 'N', 'L')")
c.execute("INSERT INTO training VALUES (4, 'M', 'H', 'N', 'N', 'P')")
c.execute("INSERT INTO training VALUES (5, 'F', 'M', 'N', 'R', 'S')")
c.execute("INSERT INTO training VALUES (6, 'F', 'H', 'Y', 'N', 'L')")
c.execute("INSERT INTO training VALUES (7, 'M', 'H', 'N', 'N', 'P')")
c.execute("INSERT INTO training VALUES (8, 'M', 'H', 'Y', 'R', 'L')")
c.execute("INSERT INTO training VALUES (9, 'M', 'M', 'N', 'N', 'S')")
c.execute("INSERT INTO training VALUES (10, 'M', 'M', 'Y', 'N', 'P')")
c.execute("INSERT INTO training VALUES (11, 'F', 'M', 'N', 'R', 'S')")
c.execute("INSERT INTO training VALUES (12, 'F', 'H', 'Y', 'R', 'P')")
c.execute("INSERT INTO training VALUES (13, 'M', 'M', 'N', 'N', 'L')")
c.execute("INSERT INTO training VALUES (14, 'F', 'H', 'Y', 'R', 'P')")
c.execute("INSERT INTO training VALUES (15, 'F', 'H', 'Y', 'N', 'L')")

#create testing data table
c.execute("CREATE TABLE testing (id INTEGER PRIMARY KEY AUTOINCREMENT, gender text, sp text, ast text, tpr text, reco text)")
c.execute("INSERT INTO testing (gender, sp, ast, tpr, reco) VALUES ('F', 'H', 'Y', 'R', 'S')")
c.execute("INSERT INTO testing (gender, sp, ast, tpr, reco) VALUES ('F', 'H', 'N', 'N', 'S')")
c.execute("INSERT INTO testing (gender, sp, ast, tpr, reco) VALUES ('F', 'M', 'Y', 'R', 'P')")
c.execute("INSERT INTO testing (gender, sp, ast, tpr, reco) VALUES ('F', 'H', 'N', 'N', 'P')")
c.execute("INSERT INTO testing (gender, sp, ast, tpr, reco) VALUES ('M', 'M', 'N', 'R', 'L')")

conn.commit()

"""
attrs_dict = {'gender': ['M', 'F'], 'sp': ['M', 'H'], 'ast': ['Y', 'N'], 'tpr': ['R', 'N']}
for attr in attrs_dict.keys():
    print("\n\n--------------------\n")
    print("test for attrs:", attr, " starts:\n")
    row_num = list(*c.execute("SELECT COUNT(*) FROM training WHERE ast= 'Y' AND gender = 'F'"))[0]
    print('row num ->', row_num, '\n')
    info = 0
    for val in attrs_dict[attr]:
        print('branch -> ', val)
        col_pred = []
        this_num = list(*c.execute("SELECT COUNT(*) FROM training WHERE ast = 'Y' AND gender = 'F' AND %s = '%s'"   % (attr, val)))[0]
        for row in c.execute("SELECT id, gender, reco FROM training WHERE ast = 'Y' AND gender = 'F' AND %s = '%s'" % (attr, val)):
            print(row)
            col_pred.append(row[-1])
        print('col_rep:', col_pred)
        if col_pred:
            print('content:', infoContent(col_pred, ['L', 'S', 'P']))
            print('portion:', this_num, '/', row_num)
            info += this_num/row_num * infoContent(col_pred, ['L', 'S', 'P'])
        else:
            print()
        print('\n')
    print('info', info)
    print("test ended")
"""


attr_list = ['gender', 'sp', 'ast', 'tpr']
training_total_c = list(*(c.execute("SELECT COUNT(*) FROM training")))
# print('fuck!!!', training_total_c[0])
for row in list(c.execute("SELECT * FROM testing")):

    p_c = list(*(c.execute("SELECT COUNT(*) FROM training WHERE reco = '%s'" % str(row[-1]))))
    print("==========(",'Row %d of testing dataset: '%row[0],'P(%s) = ' % row[-1], p_c[0], '/', 15, ")===========")
    PC = p_c[0] / 15.0
    print("test of this row: ", row, "goes below-->\n{")
    for cl in ['L', 'S', 'P']:
        print("\t # Probability of classified as class %s -> " % cl, '{')
        joint_probability = 1
        for attr in attr_list:
            print('\t\t',cl, '-->', attr, '=', row[attr_list.index(attr)+1])
            # variable attr_c is the number of attribute of certain value given the specific class label
            attr_c = list(*c.execute("SELECT COUNT(*) FROM training WHERE reco = '%s' AND %s = '%s'" % (cl, attr, row[attr_list.index(attr)+1])))[0]
            print("\t\t attr count: ", attr_c)

            # this line below counts the number of rows that is marked as a certain class label in the training data set
            class_c = list(*c.execute("SELECT COUNT(*) FROM training WHERE reco = '%s'" % cl))[0]

            print("\t\t class count: ", class_c)
            print("\t\t# Conditional Probability: P(%s=%s|%s) =" % (attr,row[attr_list.index(attr)+1], cl), "%s / %s" % (attr_c, class_c))
            joint_probability *= (attr_c / class_c)
        print("\t>>> joint probability: ", joint_probability * class_c/training_total_c[0])
        print('\t}')
    print("}\n-*-*-*-*-*-End of listing of previous row-*-*-*-*-*-\n\n\n")