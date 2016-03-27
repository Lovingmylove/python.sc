# -*- coding: utf-8 -*-
from sklearn import linear_model


# LinearRegression
clf = linear_model.LinearRegression()
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_, clf.intercept_
print clf.predict([3,3])


# RidgeRegression
clf = linear_model.Ridge(alpha = .001)
# clf = linear_model.RidgeCV(alphas = [0.1, 0.01, 0.3])
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_, clf.intercept_
# print clf.alpha_
print clf.predict([3,3])


# Lasso(参数较少时使用)
clf = linear_model.Lasso(alpha = .001)
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_, clf.intercept_
print clf.predict([3,3])