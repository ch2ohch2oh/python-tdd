import random
import pytest


@pytest.fixture
def random_name():
    names = ['John', 'Jane', 'Marry']
    return random.choice(names)


def test_fixture_usage(random_name):
    assert random_name