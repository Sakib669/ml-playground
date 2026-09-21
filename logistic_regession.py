from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

iris = datasets.load_iris()
# print(list(iris.keys()))
# print(list(iris['data']))
# print(list(iris['target']))

x = iris["data"][:, 3:]
y = (iris["target"] == 2).astype(int)
# print(y)


# train a logistic regresstion classifier to predict whether a flower is iris virginca or not

clf = LogisticRegression()
clf.fit(x, y)

example = clf.predict(([[2.5]]))
# print(example)


# using matplottlib to plot the visualization
x_new = np.linspace(0, 3, 1000).reshape(-1, 1)
# print(x_new)
x_prob = clf.predict_proba(x_new)
plt.plot(x_new, x_prob[:, 1], "g-", label="virginica")
plt.show()
