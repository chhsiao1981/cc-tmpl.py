import pytest

from {{cookiecutter.pkg_name}} import {{cookiecutter.module}}  # noqa


@pytest.fixture(scope="module", autouse=True)
def init():
    # setup
    yield
    # teardown
