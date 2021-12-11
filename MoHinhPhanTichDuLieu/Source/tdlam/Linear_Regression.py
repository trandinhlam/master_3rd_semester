import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read csv (comma separated value) into data
source = './data/column_2C_weka.csv'
data = pd.read_csv(source)


# print(plt.style.available) # look at available plot styles
def EDA():
    print(data.head())
    print(data.info())
    print(data.describe())
    color_list = ['red' if i == 'Abnormal' else 'green' for i in data.loc[:, 'class']]
    pd.plotting.scatter_matrix(data.loc[:, data.columns != 'class'],
                               c=color_list,
                               figsize=[15, 15],
                               diagonal='hist',
                               alpha=0.5,
                               s=200,
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


from sklearn.linear_model import LinearRegression

data1 = data[data['class'] == 'Abnormal']
x = np.array(data1.loc[:, 'pelvic_incidence']).reshape(-1, 1)
y = np.array(data1.loc[:, 'sacral_slope']).reshape(-1, 1)
# Predict space
predict_space = np.linspace(min(x), max(x)).reshape(-1, 1)


def LR():
    # create data1 that includes pelvic_incidence that is feature and sacral_slope that is target variable
    # Scatter
    plt.figure(figsize=[10, 10])
    plt.scatter(x=x, y=y)
    plt.xlabel('pelvic_incidence')
    plt.ylabel('sacral_slope')
    # plt.show()
    # LinearRegression
    reg = LinearRegression()
    # train
    reg.fit(x, y)
    # Predict
    predicted = reg.predict(predict_space)
    # R^2
    print('R^2 score: ', reg.score(x, y))
    showRegResult(predicted)


def showRegResult(predicted):
    # Plot regression line and scatter
    plt.plot(predict_space, predicted, color='black', linewidth=3)
    plt.scatter(x=x, y=y)
    plt.xlabel('pelvic_incidence')
    plt.ylabel('sacral_slope')
    plt.show()


from sklearn.model_selection import cross_val_score, train_test_split


def CV():
    reg = LinearRegression()
    k = 5
    cv_result = cross_val_score(reg, x, y, cv=k)  # uses R^2 as score
    print('CV Scores: ', cv_result)
    print('CV scores average: ', np.sum(cv_result) / k)


from sklearn.linear_model import Ridge, Lasso, Huber


def RidgeReg():
    # x = np.array(data1.loc[:, ['pelvic_incidence', 'pelvic_tilt numeric', 'lumbar_lordosis_angle', 'pelvic_radius']])
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.3)
    ridge = Ridge(alpha=0.1, normalize=True)
    ridge.fit(x_train, y_train)
    ridge_predict = ridge.predict(x_test)
    print('Ridge score: ', ridge.score(x_test, y_test))
    print('Ridge coefficients: ', ridge.coef_)
    # showRegResult(ridge_predict)


def LassoReg():
    # x = np.array(data1.loc[:, ['pelvic_incidence', 'pelvic_tilt numeric', 'lumbar_lordosis_angle', 'pelvic_radius']])
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.3)
    lasso = Lasso(alpha=0.1, normalize=True)
    lasso.fit(x_train, y_train)
    lasso_predict = lasso.predict(x_test)
    print('lasso score: ', lasso.score(x_test, y_test))
    print('Lasso coefficients: ', lasso.coef_)
    # showRegResult(lasso_predict)

def HuberReg():
    # x = np.array(data1.loc[:, ['pelvic_incidence', 'pelvic_tilt numeric', 'lumbar_lordosis_angle', 'pelvic_radius']])
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.3)
    huber = Huber(alpha=0.1, normalize=True)
    huber.fit(x_train, y_train)
    lasso_predict = huber.predict(x_test)
    print('huber score: ', huber.score(x_test, y_test))
    print('Lasso coefficients: ', huber.coef_)
    # showRegResult(lasso_predict)


# EDA()
# KNN()
LR()
CV()
RidgeReg()
LassoReg()
HuberReg()
