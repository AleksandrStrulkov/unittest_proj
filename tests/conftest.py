import pytest
from utils import arrs, dicts


@pytest.fixture
def fixture_get_list():
    return [1, 2, 3]


@pytest.fixture
def fixture_my_slice():
    return [1, 2, 3, 4]


@pytest.fixture
def fixture_my_slice_none():
    return []


@pytest.fixture
def fixture_get_val():
    return {"pk": 1}


@pytest.fixture
def fixture_get_val_def():
    return 'git'
