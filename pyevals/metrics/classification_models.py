from sklearn.tree import DecisionTreeClassifier
from pyevals.metrics.classification_metrics import accuracy, roc_auc, recall, precision, classification_matrix


def decisiontree(X_train=None, y_train=None, X_test=None, y_test=None, max_depth=None, min_samples_leaf=None,
                 criterion=None):
    """
    :params:
    """
    dt = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf, criterion=criterion)
    dt_model = dt.fit(X_train, y_train)
    y_pred = dt_model.predict(X_test)
    if y_test is not None:
        return y_pred, \
               accuracy(y_test, y_pred), \
               precision(y_test, y_pred), \
               recall(y_test, y_pred), \
               roc_auc(y_test, y_pred), \
               classification_matrix(y_test, y_pred)
    elif y_test is None:
        return "There is no y_test to give metrics.", y_pred
