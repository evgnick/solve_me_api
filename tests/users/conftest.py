import pytest
import requests

from config import BASE_URL


@pytest.fixture
def get_users():
    response = requests.get(BASE_URL)
    return response
