import requests

from config import SERVICE_URL
from src.baseclasses.response import ResponseValidator
from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = ResponseValidator(r)
    response.assert_status_code(200).validate(POST_SCHEMA)


def test_getting_posts_pydantic():
    r = requests.get(url=SERVICE_URL)
    response = ResponseValidator(r)
    response.assert_status_code(200).validate_pydantic(Post)


# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
