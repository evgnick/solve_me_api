from itertools import product

from src.baseclasses.response_ import ResponseValidator
from src.pydantic_schemas.user import User


def test_getting_users_list(get_users, calculate, make_number):
    ResponseValidator(get_users).assert_status_code(200).validate(User)
    # вызов
    print(calculate(1, 1))
    print(make_number)
