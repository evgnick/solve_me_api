from jsonschema import validate
from pydantic import BaseModel
from requests import Response

from src.enums.global_enums import GlobalErrorMessages


class ResponseValidator:

    def __init__(self, response: Response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def validate_pydantic(self, pydantic_schema: BaseModel):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                pydantic_schema.model_validate(item)
        else:
            pydantic_schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, expected_status_code):
        if isinstance(expected_status_code, list):
            assert self.response_status in expected_status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == expected_status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
