import pytest


@pytest.fixture(scope="module", autouse=True)
def init():
    # setup
    yield
    # teardown


def test_dummy(init):
    assert True
