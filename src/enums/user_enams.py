from enum import Enum


class Gender(Enum):
    male = "male"
    female = "female"


class Status(Enum):
    active = "active"
    inactive = "inactive"


class UserError(Enum):
    WRONG_EMAIL = "Email does not contain @ character"
