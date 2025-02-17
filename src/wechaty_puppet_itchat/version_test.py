"""
version unit test, this file will be updated in deploy stage.
"""
# import pytest   # type: ignore

from .version import VERSION


def test_version() -> None:
    """
    Unit Test for version file
    """

    assert VERSION == '0.0.2', 'version should be 0.0.2'
