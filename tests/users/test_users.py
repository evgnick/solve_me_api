import pytest
from src.baseclasses.response_ import ResponseValidator
from src.pydantic_schemas.user import User


def test_getting_users_list(get_users, calculate, make_number):
    """
    Пример описания теста
    :param get_users:
    :param calculate:
    :param make_number:
    :return:
    """
    ResponseValidator(get_users).assert_status_code(200).validate(User)
    # вызов
    # print(calculate(1, 1))
    # print(make_number)


@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_another():
    assert 1 == 1


def test_fail():
    assert 1 == 2


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result',
                         [(1, 1, 2),
                          (2, 2, 4)
                          ])
def test_calculate(calculate, first_value, second_value, result):
    assert calculate(first_value, second_value) == result
