# plot line of best for multiple robust regression algorithms
from random import random
from random import randint
from random import seed
from numpy import arange
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from matplotlib import pyplot


# prepare the dataset
def get_dataset():
    X, y = make_regression(n_samples=100, n_features=1, tail_strength=0.9, effective_rank=1, n_informative=1, noise=2,
                           bias=50, random_state=1)
    # add some artificial outliers
    seed(1)
    for i in range(10):
        factor = randint(2, 4)
        if random() > 0.5:
            X[i] += factor * X.std()
        else:
            X[i] -= factor * X.std()
    return X, y


# dictionary of model names and model objects
def get_models():
    models = list()
    models.append(LinearRegression(normalize=True))
    models.append(Ridge(alpha=0.1, normalize=True))
    models.append(Lasso(alpha=0.1, normalize=True))
    models.append(HuberRegressor(epsilon=1.0))
    return models


# plot the dataset and the model's line of best fit
def plot_best_fit(X, y, xaxis, model):
    # fit the model on all data
    model.fit(X, y)
    # calculate outputs for grid across the domain
    yaxis = model.predict(xaxis.reshape((len(xaxis), 1)))
    # plot the line of best fit
    pyplot.plot(xaxis, yaxis, label=type(model).__name__)


# load the dataset
X, y = get_dataset()
# define a uniform grid across the input domain
xaxis = arange(X.min(), X.max(), 0.01)
for model in get_models():
    # plot the line of best fit
    plot_best_fit(X, y, xaxis, model)
# plot the dataset
pyplot.scatter(X, y)
# show the plot
pyplot.title('Robust Regression')
pyplot.legend()
pyplot.show()
