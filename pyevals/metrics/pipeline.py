from pyevals.metrics.classification_metrics import accuracy, precision, recall, classification_matrix, f1_score
from pyevals.metrics.regression_metrics import rmse
from pyevals.metrics.regression_metrics import rsquared_score
from pyevals.metrics.regression_metrics import adj_rsquared_score
from pyevals.metrics.classification_plots import classification_report_plot, confusion_matrix_plot, roc_auc_curve
from pyevals.metrics.regression_metrics import mean_absolute_percentage_error
from pyevals.metrics.regression_plots import regression_line, sns_reg_plot
from pyevals.metrics.regression_models import linear_regression, \
    random_forest_regression, \
    decision_tree_regressor, \
    knn_regressor, \
    support_vector_regressor
from pyevals.metrics.classification_models import decisiontree
from pyevals import exceptions
import numpy as np


def evaluate(predicted, actual, method=None,
             figsize=None, ax=None,
             plots=True, reports=True,
             samples_size=None,
             number_of_independent_columns=None):
    """

    :param actual: Your y_true
    :param predicted:Your y_pred
    :param figsize:Figure size
    :param ax:axes
    :param plots:True if you want all plots and is true by default
    :param method: Classification or regression
    :param reports: True by default and if you want reports you need to leave it as True
    :param samples_size: Size of the sample and also to be used only for adj_r2_score
    :param number_of_independent_columns: Number of columns which are independent and can only for adj_r2_score
    :return: Returns all the classification metrics


    """

    # Classification

    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The length of actual {0} and length of "
                                          "predicted {1} are not the same".format(len(actual), len(predicted)))

    elif method == 'Classification':
        print("\n---------------------\033[1mReports\033[0m-------------------------\n")
        print("\033[1mAccuracy score:\033[0m {}".format(accuracy(actual, predicted)))
        print("\033[1mRecall score:\033[0m {}".format(recall(actual, predicted)))
        print("\033[1mPrecision score:\033[0m {}".format(precision(actual, predicted)))
        print("\033[1mF1 score:\033[0m {}".format(f1_score(actual, predicted)))
        print("\n---------------------\033[1mPlots\033[0m-------------------------\n")
        print("\033[1mClassification report:\033[0m: ")
        classification_report_plot(actual, predicted, figsize=figsize, ax=ax)
        print("\033[1mConfusion Matrix:\033[0m: ")
        confusion_matrix_plot(actual, predicted, figsize, ax)
        print("\033[1mROC curve:\033[0m ")
        roc_auc_curve(actual, predicted, figsize, ax)

        # Regression
    if method == 'Regression':
        actual = np.array(actual)
        predicted = np.array(predicted)

        print("\n-----------------------\033[1mReports\033[0m------------------------\n")
        print("\033[1mRMSE:\033[0m {}".format(rmse(actual, predicted)))
        print("\033[1mMAPE:\033[0m {}".format(mean_absolute_percentage_error(actual, predicted)))
        print("\033[1mR2 score:\033[0m {}".format(rsquared_score(actual, predicted)))
        print("\033[1mAdj R2 score:\033[0m {}".format(adj_rsquared_score(actual,
                                                                         predicted,
                                                                         samples_size,
                                                                         number_of_independent_columns)))

        print("\n---------------------\033[1mPlots\033[0m-------------------------\n")
        print("\033[1mRegression Plot 1:\033[0m ")
        regression_line(actual, predicted)
        print("\033[1mRegression Plot 2:\033[0m ")
        sns_reg_plot(actual, predicted)


