import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns
import numpy as np


def roc_auc_curve(actual, predicted, figsize=None, ax=None):
    """

    :param actual:
    :param predicted:
    :return:
    """
    plt.figure(figsize=figsize)
    fpr, tpr, threshold = metrics.roc_curve(actual, predicted)
    roc_auc = metrics.auc(fpr, tpr)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()


def confusion_matrix_plot(actual, predicted, figsize=None, ax=None):
    """

    :param actual:
    :param predicted:
    :return:
    """
    plt.figure(figsize=figsize)
    cf_matrix = metrics.confusion_matrix(actual, predicted)
    sns.heatmap(cf_matrix / np.sum(cf_matrix), annot=True,ax=ax,
                fmt='.2%', cmap='Blues')
    plt.show()


def classification_report_plot(actual, predicted, figsize=None, ax=None):

    plt.figure(figsize=figsize)

    xticks = ['precision', 'recall', 'f1-score', 'support']
    yticks = list(np.unique(actual))
    yticks += ['avg']
    rep = np.array(metrics.precision_recall_fscore_support(actual, predicted)).T
    avg = np.mean(rep, axis=0)
    avg[-1] = np.sum(rep[:, -1])
    rep = np.insert(rep, rep.shape[0], avg, axis=0)

    sns.heatmap(rep,
                annot=True,
                cbar=False,
                xticklabels=xticks,
                yticklabels=yticks,
                ax=ax,
                cmap='Blues')
    plt.show()
