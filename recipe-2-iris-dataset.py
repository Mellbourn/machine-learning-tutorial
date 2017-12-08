"""https://www.youtube.com/watch?v=tNa99PG8hR8"""
from sklearn.datasets import load_iris

IRIS = load_iris()
print(IRIS.feature_names)
print(IRIS.target_names)
