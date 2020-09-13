# Calculating accuracy
from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score, classification_report, f1_score
from pyevals import exceptions
# from pyevals.metrics import utils


def accuracy(actual, predicted):
    """

    :param actual:
    :param predicted:
    :return:
    """
    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The lengths of the inputs should be equal."
                                          "The shape of the inputs are {0}{1}".format(len(actual), len(predicted)))
    else:
        output = accuracy_score(actual, predicted)
    return output


def recall(actual, predicted):
    """

    :param actual:
    :param predicted:
    :return:
    """
    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The lengths of the inputs should be equal."
                                          "The shape of the inputs are {0}{1}".format(len(actual), len(predicted)))
    else:
        output = recall_score(actual, predicted)
    return output


def precision(actual, predicted):
    """

    :param actual:
    :param predicted:
    :return:
    """
    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The lengths of the inputs should be equal."
                                          "The shape of the inputs are {0}{1}".format(len(actual), len(predicted)))
    else:
        output = precision_score(actual, predicted)
    return output


def roc_auc(actual, predicted):
    """

    :param actual:
    :param predicted:
    :return:
    """
    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The lengths of the inputs should be equal."
                                          "The shape of the inputs are {0}{1}".format(len(actual), len(predicted)))
    else:
        output = roc_auc_score(actual, predicted)
    return output


def f1score(actual, predicted):
    """

    :param actual:
    :param predicted:
    :return:
    """
    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The lengths of the inputs should be equal."
                                          "The shape of the inputs are {0}{1}".format(len(actual), len(predicted)))
    else:
        output = f1_score(actual, predicted)
    return output


def classification_matrix(actual, predicted):
    """

    :param actual:
    :param predicted:
    :return:
    """
    if len(actual) != len(predicted):
        raise exceptions.MetricValueError("The lengths of the inputs should be equal."
                                          "The shape of the inputs are {0}{1}".format(len(actual), len(predicted)))
    else:
        output = classification_report(actual, predicted)
    return output
