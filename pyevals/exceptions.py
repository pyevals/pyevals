# Exceptions/ errors for the library


class MetricRootError(Exception):
    """

    Main exception for all the forth coming errors.
    """
    pass


class MetricValueError(MetricRootError, ValueError):
    """

    A bad value or no value has been passed into the function
    """
    pass


class MetricModelError(MetricRootError):
    """

    Raise this error for a problem caused while interacting with sklearn or any other ml framework.
    """
    pass


class MetricTypeError(MetricRootError, TypeError):
    """

    Raise this error when there is an unexpected type or none type passed as input.
    """
    pass


class MetricKeyError(MetricRootError, KeyError):
    """

    An invalid key is used.
    """
    pass

