from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# noinspection PyTupleAssignmentBalance
def regression_line(actual, predicted, figsize=None, ax=None):
    plt.figure(figsize=figsize)
    plt.plot(actual, predicted, 'o')
    slope, intercept = np.polyfit(actual, predicted, 1)
    plt.plot(actual, slope * actual + intercept)
    plt.show()


def sns_reg_plot(actual, predicted, figsize=None, ax=None):
    plt.figure(figsize=figsize)
    sns.regplot(actual, predicted)
    plt.show()
