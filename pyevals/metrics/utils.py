# Defining classification utils.

from sklearn.metrics._classification import _check_targets, unique_labels
from sklearn.utils.validation import check_array
from pyevals.exceptions import MetricTypeError, MetricValueError
import numpy as np
from contextlib import suppress
import numbers


def complex_data(array):
    if hasattr(array, 'dtype') and array.dtype is not None and hasattr(array.dtype, 'kind') and array.dtype.kind == 'c':
        raise MetricValueError('Complex data is not supported {}'.format(array))


def samples(input_array_list):
    """
    Params:
    -------
    input_array_list: The input array/ list.

    Returns:
    --------
        Returns the length of the array or list after converting the list to array and also after checking the shape.
    """
    if not hasattr(input_array_list, '__len__') and not hasattr(input_array_list, 'shape'):
        if hasattr(input_array_list, '__array__'):
            input_array_list = np.asarray(input_array_list)
        else:
            raise MetricTypeError('Expected a sequence or an array like input %s' % type(input_array_list))
    if hasattr(input_array_list, 'shape') and input_array_list.shape is not None:
        if len(input_array_list.shape) == 0:
            raise MetricTypeError('The input array %r cannot be considered'
                                  % input_array_list)
        if isinstance(input_array_list.shape[0], numbers.Integral):
            return input_array_list.shape[0]
    try:
        return len(input_array_list)
    except TypeError as ex:
        raise MetricTypeError('Expected a sequence or an array like input %s' % type(input_array_list)) from ex


def equal_lengths(*arrays):
    """
    Checks if all the arrays/ inputs are of the equal length.
    """
    _length = [samples(val) for val in arrays if val is not None]
    _unique = np.unique(_length)
    if len(_unique) > 1:
        raise MetricValueError(' The lengths of input variables are not equal %r' % [int(val) for val in _length])


def check_type(actual, predicted):
    if actual is not None and predicted is not None:
        _check_targets(actual, predicted)
    else:
        raise MetricValueError('The inputs{0}{1} should not be none'.format(len(actual), len(predicted)))


def unique(*array):
    if not array:
        raise MetricValueError('No argument passed')
    elif array is None:
        raise MetricValueError('The input(s) should not be none')
    else:
        unique_labels(array)

    # Defining the regression utils.


from pyevals.exceptions import MetricTypeError, MetricValueError
import numpy as np
from contextlib import suppress
import numbers


def complex_data(array):
    if hasattr(array, 'dtype') and array.dtype is not None and hasattr(array.dtype, 'kind') and array.dtype.kind == 'c':
        raise MetricValueError('Complex data is not supported {}'.format(array))


def check_type(array, dtype='numeric'):
    # Checking the type of the error.
    dtype_numeric = isinstance(dtype, str) and dtype == 'numeric'
    original_dtype = getattr(array, 'dtype', None)
    if not hasattr(original_dtype, 'kind'):
        original_dtype = None
    multiple_dtypes = None
    if hasattr(array, 'dtypes') and hasattr(array.dtypes, '__array__'):
        with suppress(ImportError):
            from pandas.api.types import is_sparse
            if (not hasattr(array, 'sparse') and array.dtypes.apply(is_sparse).any()):
                print(' The input values are of sparse type. Converting them to dense numpy array')

    if dtype_numeric:
        if original_dtype is not None and original_dtype.kind == 'O':
            # Object type input is being converted to float.
            dtype = np.float64
        else:
            dtype = None

    if isinstance(dtype, (list, tuple)):
        if original_dtype is not None and original_dtype in dtype:
            dtype = None

    return array


def input_regression(actual, predicted, dtype='numeric'):
    """
        Parameters
        ----------
        actual: Your y_test
        predicted: Your y_pred

        Returns
        -------
        Can be used to define the inputs for any regression metric.
    """
    equal_lengths(actual, predicted)
    actual = check_type(actual, dtype=dtype)
    predicted = check_type(predicted, dtype=dtype)
    actual, predicted = np.array(actual), np.array(predicted)
    if actual.ndim == 1:
        actual = actual.reshape((-1, 1))

    if predicted.ndim == 1:
        predicted = predicted.reshape((-1, 1))

    if actual.shape[1] != predicted.shape[1]:
        raise MetricValueError('Actual and predicted have different outputs.')

    outputs = actual.shape[1]
    type_actual = 'continuous' if outputs == 1 else 'continuous-multioutput'
    return type_actual, actual, predicted


def samples(input_array_list):
    """
    Params:
    -------
    input_array_list: The input array/ list.

    Returns:
    --------
        Returns the length of the array or list after converting the list
        to array and also after checking the shape.
    """
    if not hasattr(input_array_list, '__len__') and not hasattr(input_array_list,
                                                                'shape'):
        if hasattr(input_array_list, '__array__'):
            input_array_list = np.asarray(input_array_list)
        else:
            raise MetricTypeError('Expected a sequence or an array like input %s'
                                  % type(input_array_list))
    if hasattr(input_array_list, 'shape') and input_array_list.shape is not None:
        if len(input_array_list.shape) == 0:
            raise MetricTypeError('The input array %r cannot be considered'
                                  % input_array_list)
        if isinstance(input_array_list.shape[0], numbers.Integral):
            return input_array_list.shape[0]
    try:
        return len(input_array_list)
    except TypeError as ex:
        raise MetricTypeError('Expected a sequence or an array like input %s'
                              % type(input_array_list)) from ex


def simple_error(actual: np.ndarray, predicted: np.ndarray):
    """ Simple error """
    return actual - predicted


def equal_lengths(*arrays):
    """
    Checks if all the arrays/ inputs are of the equal length.
    """
    _length = [samples(val) for val in arrays if val is not None]
    _unique = np.unique(_length)
    if len(_unique) > 1:
        raise MetricValueError(' The lengths of input variables are not equal %r'
                               % [int(val) for val in _length])
