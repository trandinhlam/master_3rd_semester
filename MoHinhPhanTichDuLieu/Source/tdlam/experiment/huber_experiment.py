import numpy as np
from sklearn.linear_model import HuberRegressor, LinearRegression
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)
X, y, coef = make_regression(n_samples=2000, n_features=2, noise=40.0, coef=True, random_state=0)
X[:4] = rng.uniform(10, 20, (4, 2))
y[:4] = rng.uniform(10, 20, 4)
huber = HuberRegressor().fit(X, y)
huber.score(X, y)
huber.predict(X[:1, ])
linear = LinearRegression().fit(X, y)
print("True coefficients:", coef)
# True
# coefficients: [20.4923...  34.1698...]
print("Huber coefficients:", huber.coef_)
# Huber coefficients: [17.7906... 31.0106...]
print("Linear Regression coefficients:", linear.coef_)
# Linear Regression
# coefficients: [-1.9221...  7.0226...]
