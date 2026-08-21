import pytest


@pytest.fixture(scope="package", autouse=True)
def init():
    # setup
    yield
    # teardown
