import pytest
from random import randrange
from src.generators.player import Player


@pytest.fixture
def get_number():
    return randrange(0, 100)


# можем использовать эту функцию, например, для удаления каки-то данных,
# изменять какие-то поля, добавлять / удалять
def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return None


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    number = randrange(0, 100)
    yield number
    # print("Teardown")


@pytest.fixture
def player_generator():
    return Player()
