"""my first machine learning tutorial https://www.youtube.com/watch?v=cKxRvEZd3Mw"""

from sklearn import tree
FEATURES = [[140, 1], [130, 1], [150, 0], [170, 0]]
LABELS = [0, 0, 1, 1]
CLF = tree.DecisionTreeClassifier()
CLF = CLF.fit(FEATURES, LABELS)
print(CLF.predict([[160, 0]]))
