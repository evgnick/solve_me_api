from pydantic import BaseModel, field_validator
from src.enums.user_enams import Gender, Status, UserError


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @classmethod
    @field_validator('email')
    def email_format(cls, v):
        if '@' not in v:
            raise ValueError(UserError.WRONG_EMAIL.value)
        return v
