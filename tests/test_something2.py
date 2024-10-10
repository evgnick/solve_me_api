import requests

from config import BASE_URL
from src.baseclasses.response_ import ResponseValidator
from src.pydantic_schemas.user import User


def test_getting_users_list():
    response = requests.get(BASE_URL)
    test_object = ResponseValidator(response)
    test_object.assert_status_code(300).validate(User)
