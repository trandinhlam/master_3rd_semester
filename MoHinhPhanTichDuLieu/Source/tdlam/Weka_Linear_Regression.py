import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso, HuberRegressor, ElasticNet
from sklearn.model_selection import cross_val_score, train_test_split

# read csv (comma separated value) into data
# https://www.kaggle.com/uciml/biomechanical-features-of-orthopedic-patients

source = f'./data/weka/column_2C_weka.csv'
data = pd.read_csv(source)

# x1Label = 'pelvic_radius'
x2Label = 'pelvic_tilt_numeric'
x3Label = 'lumbar_lordosis_angle'
x4Label = 'sacral_slope'
x5Label = 'pelvic_incidence'
# x6Label = 'degree_spondylolisthesis'
columns = [x2Label, x3Label, x4Label, x5Label]
xLabel = x5Label
yLabel = x2Label


# print(plt.style.available) # look at available plot styles
def EDA():
    print(data.head())
    print(data.info())
    print(data.describe())
    color_list = ['red' if i == 'Abnormal' else 'green' for i in data.loc[:, 'class']]
    pd.plotting.scatter_matrix(data.loc[:, columns],
                               c=color_list,
                               figsize=[50, 50],
                               diagonal='hist',
                               alpha=0.5,
                               s=100,
                               marker='*',
                               edgecolor="black")
    plt.show()
    sns.countplot(x="class", data=data)
    data.loc[:, 'class'].value_counts()


def KNN():
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=3)
    x, y = data.loc[:, data.columns != 'class'], data.loc[:, 'class']
    knn.fit(x, y)
    prediction = knn.predict(x)
    print('Prediction: {}'.format(prediction))
    # ... so on using notebook


data1 = data[data['class'] == 'Abnormal']
x = np.array(data1.loc[:, xLabel]).reshape(-1, 1)
y = np.array(data1.loc[:, yLabel]).reshape(-1, 1)

# Predict space
predict_space = np.linspace(min(x), max(x)).reshape(-1, 1)


def prepare_x():
    return np.array(data1.loc[:, [x3Label, x4Label]])
    # return np.array(data1.loc[:, [x1Label, x2Label, x3Label, x4Label, x6Label]])
    # return np.array(data1.loc[:, [x1Label, x2Label, x3Label, x4Label, x6Label]])
    # return np.array(data1.loc[:, [xLabel]])


def showRegResult(name, x_test, predicted, r2_score):
    results.append([x_test, predicted, name, r2_score])
    plt.figure(figsize=[50, 50])
    for i in range(len(results)):
        rs = results[i]
        # Plot regression line and scatter
        plt.plot(rs[0], rs[1], color=colors[i], linewidth=3, label="%s: R2 score = %.3f" % (rs[2], rs[3]))
        legend = plt.legend(
            loc="lower right", frameon=False, title="R2 Score Regressor", prop=dict(size="large")
        )
    plt.scatter(x=x, y=y, alpha=0.5, s=100, marker='*')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


def LR():
    data = prepare_x()
    x_train, x_test, y_train, y_test = train_test_split(data, y, random_state=2, test_size=0.3)
    reg = LinearRegression()
    # train
    reg.fit(x_train, y_train)
    # Predict
    predicted = reg.predict(x_test)
    # R^2
    score = reg.score(x_test, y_test)
    print('LR R^2 score: ', reg.score(x_test, y_test))
    print('LR coefficients: ', reg.coef_)
    showRegResult("LR", x_test, predicted, score)


results = []
colors = ['black', 'green', 'red', 'blue', 'yellow']


def CV():
    reg = LinearRegression()
    k = 5
    data = prepare_x()
    x_train, x_test, y_train, y_test = train_test_split(data, y, random_state=2, test_size=0.3)
    reg.fit(x_train, y_train)
    cv_result = cross_val_score(reg, data, y, cv=k)  # uses R^2 as score
    cv_avg = np.sum(cv_result) / k
    print('CV Scores: ', cv_result)
    print('CV scores average: ', cv_avg)
    # train
    predicted = reg.predict(x_test)
    # R^2
    score = reg.score(x_test, y_test)
    print('LR-CV R^2 score: ', reg.score(x_test, y_test))
    print('LR-CV coefficients: ', reg.coef_)
    showRegResult("LR-CV", x_test, predicted, score)


def RidgeReg():
    data = prepare_x()
    x_train, x_test, y_train, y_test = train_test_split(data, y, random_state=2, test_size=0.3)
    ridge = Ridge(alpha=0.1, normalize=True)
    ridge.fit(x_train, y_train)
    ridge_predict = ridge.predict(x_test)
    score = ridge.score(x_test, y_test)
    print('Ridge score: ', ridge.score(x_test, y_test))
    print('Ridge coefficients: ', ridge.coef_)
    showRegResult("Ridge", x_test, ridge_predict, score)


def LassoReg():
    data = prepare_x()
    x_train, x_test, y_train, y_test = train_test_split(data, y, random_state=2, test_size=0.3)
    lasso = Lasso(alpha=0.1, normalize=True)
    lasso.fit(x_train, y_train)
    lasso_predict = lasso.predict(x_test)
    score = lasso.score(x_test, y_test)
    print('Lasso R2 score: ', lasso.score(x_test, y_test))
    print('Lasso coefficients: ', lasso.coef_)
    showRegResult("Lasso", x_test, lasso_predict, score)


def ElasticNetReg():
    data = prepare_x()
    x_train, x_test, y_train, y_test = train_test_split(data, y, random_state=2, test_size=0.3)
    elastic = ElasticNet(alpha=0.1, normalize=True)
    elastic.fit(x_train, y_train)
    lasso_predict = elastic.predict(x_test)
    score = elastic.score(x_test, y_test)
    print('ElasticNet R2 score: ', elastic.score(x_test, y_test))
    print('ElasticNet coefficients: ', elastic.coef_)
    showRegResult("ElasticNet", x_test, lasso_predict, score)


def HuberReg():
    data = prepare_x()
    x_train, x_test, y_train, y_test = train_test_split(data, y, random_state=2, test_size=0.3)
    huber = HuberRegressor(epsilon=1, alpha=0.1)
    huber.fit(x_train, y_train)
    huber_predict = huber.predict(x_test)
    r2 = huber.score(x_test, y_test)
    print('Huber score: ', r2)
    print('Huber coefficients: ', huber.coef_)
    showRegResult("HuberReg", x_test, huber_predict, r2)


EDA()
# KNN()
LR()
CV()
RidgeReg()
LassoReg()
# ElasticNetReg()
HuberReg()
# ....
