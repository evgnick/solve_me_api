from pydantic import BaseModel
from requests import Response

from src.enums.global_enums import GlobalErrorMessages


class ResponseValidator:

    def __init__(self, response: Response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, pydantic_schema: BaseModel):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                pydantic_schema.model_validate(item)
        else:
            pydantic_schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, expected_status_code):
        if isinstance(expected_status_code, list):
            assert self.response_status in expected_status_code, self
        else:
            assert self.response_status == expected_status_code, self
        return self

    def __str__(self):
        return f"Status code: {self.response_status}" \
               f"\nRequest url: {self.response.url}" \
               f"\nResponse body: {self.response_json}"
