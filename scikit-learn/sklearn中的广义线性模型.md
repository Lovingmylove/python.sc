#Sklearn中的广义线性模型
##Ordinary Least Squares
**对于符合线性模型的离散数据，利用线性回归的方式得到最小残差平方和的模型便是Ordinary Least Squares：**
###代码
<pre>
# -*- coding: utf-8 -*-
from sklearn import linear_model

# LinearRegression
clf = linear_model.LinearRegression()
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_, clf.intercept_
print clf.predict([3,3])
</pre>
###输出结果
<pre>
[ 0.5  0.5] 2.22044604925e-16
[ 3.]
</pre>
##Ridge Regression
**Ridge Regression 在Oridinary Least Squares的基础上多了加了拟合系数平方和，使其最小以得到最优解：**
###代码
<pre>
# -*- coding: utf-8 -*-
from sklearn import linear_model

# RidgeRegression
clf = linear_model.Ridge(alpha = .001)
# clf = linear_model.RidgeCV(alphas = [0.1, 0.01, 0.3])
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_, clf.intercept_
# print clf.alpha_
print clf.predict([3,3])
</pre>
###输出结果
<pre>
[ 0.49987503  0.49987503] 0.000249937515621
[ 2.99950012]
</pre>
###alpha因子对Ridge Regression拟合的影响
###代码
<pre>
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# X is the 10x10 Hilbert matrix
X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)


###############################################################
# Compute paths

n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)
clf = linear_model.Ridge(fit_intercept=False)

coefs = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X,y)
    coefs.append(clf.coef_)

################################################################
# Display result
ax = plt.gca()
#ax.set_color_cycle(['b'], ['r'], ['g'], ['c'], ['k'], ['y'], ['m'])

ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()
</pre>
![alpha](/Users/Lovingmylove521/Desktop/scikit-learn/alpha_Ridge_Regression.png)
##Lasso
**Lasso模型是另外一种线性回归的模型，主要解决稀疏数据的拟合问题：**
###代码
<pre>
# -*- coding: utf-8 -*-
from sklearn import linear_model

# Lasso(参数较少时使用)
clf = linear_model.Lasso(alpha = .001)
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_, clf.intercept_
print clf.predict([3,3])
</pre>
###输出结果
<pre>
[ 0.9985  0.    ] 0.0015
[ 2.997]
</pre>
##Lasso and Elastic Net for Sparse Signals
###代码
<pre>
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score

################################################################################
# generate some sparse data to play with
np.random.seed(42)

n_samples, n_features = 50, 200
X= np.random.randn(n_samples, n_features)
coef = 3 * np.random.randn(n_features)
inds = np.arange(n_features)
np.random.shuffle(inds)
coef[inds[10:]] = 0 # sparsify coef
y = np.dot(X, coef)

# add noise
y += 0.01 * np.random.normal((n_samples,))

# split data in train set and test set
n_samples = X.shape[0]
X_train, y_train = X[:n_samples / 2], y[:n_samples / 2]
X_test, y_test = X[n_samples / 2:], y[n_samples / 2:]

################################################################################
# Lasso
from sklearn.linear_model import Lasso
alpha = 0.1
lasso = Lasso(alpha=alpha)

y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(lasso)
print("r^2 on test data : %f" % r2_score_lasso)

################################################################################
# ElasticNet
from sklearn.linear_model import ElasticNet
enet = ElasticNet(alpha=alpha, l1_ratio = 0.7)

y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(enet)
print("r^2 on test data : %f" % r2_score_enet)

plt.plot(enet.coef_, label='Elastic net coefficients')
plt.plot(lasso.coef_, label='Lasso coefficients')
plt.plot(coef, '--', label='original coefficients')
plt.legend(loc='best')
plt.title("Lasso R^2: %f, Elastic Net R^2: %f" %(r2_score_lasso, r2_score_enet) )
plt.show()
</pre>
###输出结果
<pre>
Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
   normalize=False, positive=False, precompute=False, random_state=None,
   selection='cyclic', tol=0.0001, warm_start=False)
r^2 on test data : 0.384710
ElasticNet(alpha=0.1, copy_X=True, fit_intercept=True, l1_ratio=0.7,
      max_iter=1000, normalize=False, positive=False, precompute=False,
      random_state=None, selection='cyclic', tol=0.0001, warm_start=False)
r^2 on test data : 0.240176
</pre>
![](/Users/Lovingmylove521/Desktop/scikit-learn/Lasso_and_Elastic_Net_for_Sparse_Signals.png)