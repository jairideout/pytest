class PytestWarning(UserWarning):
    """Base class for all warnings emitted by pytest"""


class RemovedInPytest4Warning(PytestWarning, DeprecationWarning):
    """warning class for features that will be removed in pytest 4.0"""
