from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from pyevals.metrics.regression_metrics import rsquared_score, rmse, mean_absolute_percentage_error, adj_rsquared_score


def linear_regression(X_train=None, X_test=None, y_train=None, y_test=None,
                      samples_size=None, number_of_independent_columns=None):
    """

    """
    lr = LinearRegression()
    lr_model = lr.fit(X_train, y_train)
    y_pred = lr_model.predict(X_test)
    if y_test is not None:
        return y_pred, \
               rsquared_score(y_test, y_pred), \
               rmse(y_test, y_pred), \
               mean_absolute_percentage_error(y_test, y_pred), \
               adj_rsquared_score(y_test, y_pred, n=samples_size,
                                  p=number_of_independent_columns)
    else:
        return "There is no y_test to return the outputs", y_pred


def random_forest_regression(X_train=None, X_test=None, y_train=None, y_test=None,
                             n_estimators=None, max_depth=None,
                             min_samples_leaf=None, criterion=None, random_state=None,
                             samples_size = None, number_of_independent_columns = None):
    """

    """
    random_forest = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth,
                                  min_samples_leaf=min_samples_leaf, criterion=criterion,
                                  random_state=random_state)

    model = random_forest.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    if y_test is not None:
        return y_pred, \
               rsquared_score(y_test, y_pred), \
               rmse(y_test, y_pred), \
               mean_absolute_percentage_error(y_test, y_pred), \
               adj_rsquared_score(y_test, y_pred,
                                  n=samples_size,
                                  p=number_of_independent_columns)
    else:
        return "There is no y_test to return the outputs", y_pred


def decision_tree_regressor(X_train=None, X_test=None, y_train=None, y_test=None,
                            max_depth=None, min_samples_leaf=None,
                            criterion=None, random_state=None):
    """

    """
    dtr = DecisionTreeRegressor(max_depth=max_depth,
                                min_samples_leaf=min_samples_leaf, criterion=criterion,
                                random_state=random_state)
    dtr_model = dtr.fit(X_train, y_train)
    y_pred = dtr_model.predict(X_test)
    if y_test is not None:
        return y_pred, \
               rsquared_score(y_test, y_pred), \
               rmse(y_test, y_pred), \
               mean_absolute_percentage_error(y_test, y_pred), \
               adj_rsquared_score(y_test, y_pred)
    else:
        return "There is no y_test to return the outputs", y_pred


def knn_regressor(X_train, X_test, y_train, y_test, n_neighbors=None):
    """

    """
    model = KNeighborsRegressor(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    if y_test is not None:
        return y_pred, \
               rsquared_score(y_test, y_pred), \
               rmse(y_test, y_pred), \
               mean_absolute_percentage_error(y_test, y_pred), \
               adj_rsquared_score(y_test, y_pred)
    else:
        return "There is no y_test to return the outputs", y_pred


def support_vector_regressor(X_train, X_test, y_train, y_test):
    """

    """
    model = SVR()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    if y_test is not None:
        return y_pred, \
               rsquared_score(y_test, y_pred), \
               rmse(y_test, y_pred), \
               mean_absolute_percentage_error(y_test, y_pred), \
               adj_rsquared_score(y_test, y_pred)
    else:
        return "There is no y_test to return the outputs", y_pred


