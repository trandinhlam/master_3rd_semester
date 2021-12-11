import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats.stats import pearsonr
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score

train = pd.read_csv("../data/house_price_predict/train.csv")
test = pd.read_csv("../data/house_price_predict/test.csv")


def dataPreprocess():
    all_data = pd.concat((train.loc[:, 'MSSubClass':'SaleCondition'],
                          test.loc[:, 'MSSubClass':'SaleCondition']))
    matplotlib.rcParams['figure.figsize'] = (12.0, 6.0)
    prices = pd.DataFrame({"price": train["SalePrice"], "log(price + 1)": np.log1p(train["SalePrice"])})
    print(prices.hist())
    plt.show()
    # log transform the target:
    train["SalePrice"] = np.log1p(train["SalePrice"])

    # log transform skewed numeric features:
    numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index

    skewed_feats = train[numeric_feats].apply(lambda x: skew(x.dropna()))  # compute skewness

    skewed_feats = skewed_feats[skewed_feats > 0.75]
    skewed_feats = skewed_feats.index

    all_data[skewed_feats] = np.log1p(all_data[skewed_feats])
    all_data = pd.get_dummies(all_data)
    # filling NA's with the mean of the column:
    all_data = all_data.fillna(all_data.mean())

    return all_data


def rmse_cv(model, X_train, y):
    rmse = np.sqrt(-cross_val_score(model, X_train, y, scoring="neg_mean_squared_error", cv=5))
    return (rmse)


def RidgeExam(all_data):
    X_train = all_data[:train.shape[0]]
    X_test = all_data[train.shape[0]:]
    y = train.SalePrice
    model_ridge = Ridge()
    alphas = [0.05, 0.1, 0.3, 1, 3, 5, 10, 15, 30, 50, 75]
    cv_ridge = [rmse_cv(Ridge(alpha=alpha), X_train, y).mean() for alpha in alphas]
    print(cv_ridge)
    cv_ridge = pd.Series(cv_ridge, index=alphas)
    cv_ridge.plot(title="Validation - Just Do It")
    plt.xlabel("alpha")
    plt.ylabel("rmse")
    plt.show()
    print(cv_ridge[10])
    # Best alpha =10, rmse =  0.12733734668670754
    model_lasso = LassoCV(alphas=[1, 0.1, 0.001, 0.0005]).fit(X_train, y)
    cv_lasso = [rmse_cv(model_lasso, X_train, y).mean()]
    print(cv_lasso)
    # cv_lasso = pd.Series(cv_lasso, index=alphas)
    # cv_lasso.plot(title=" cv_lasso Validation - Just Do It")
    # plt.xlabel("alpha")
    # plt.ylabel("rmse")
    # plt.show()
    coef = pd.Series(model_lasso.coef_, index=X_train.columns)
    print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " + str(
        sum(coef == 0)) + " variables")
    imp_coef = pd.concat([coef.sort_values().head(10),
                          coef.sort_values().tail(10)])
    matplotlib.rcParams['figure.figsize'] = (8.0, 10.0)
    imp_coef.plot(kind="barh")
    plt.title("Coefficients in the Lasso Model")
    plt.show()


all_data = dataPreprocess()
print(all_data.head())
print(all_data.describe())
RidgeExam(all_data)
