from sklearn import tree

clf = tree.DecisionTreeClassifier()

X = [["MA", "M", "Y", "R"],
     ["FE", "M", "N", "R"],
     ["MA", "H", "Y", "N"],
     ['MA', 'H', 'N', 'N'],
     ['FE', 'M', 'N', 'R'],
     ['FE', 'H', 'Y', 'N'],
     ['MA', 'H', 'N', 'N'],
     ['MA', 'H', 'Y', 'R'],
     ['MA', 'M', 'N', 'N'],
     ['MA', 'M', 'Y', 'N'],
     ['FE', 'M', 'N', 'R'],
     ['FE', 'H', 'Y', 'R'],
     ['MA', 'M', 'N', 'N'],
     ['FE', 'H', 'Y', 'R'],
     ['FE', 'H', 'Y', 'N']]

Y = ["L","S","L","P","S","L","P","L","S","P","S","P","L","P","L"]

T = [['FE', 'H', 'Y', 'R', 'S'],
     ['FE', 'H', 'N', 'N', 'S'],
     ['FE', 'M', 'Y', 'R', 'P'],
     ['FE', 'H', 'N', 'N', 'P'],
     ['MA', 'M', 'N', 'R', 'L']]

model = clf.fit(X, Y)
