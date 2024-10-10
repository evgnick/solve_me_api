from pydantic import BaseModel, field_validator, Field


class Post(BaseModel):
    id: int # = Field(le=2) - валидатор на длину поля
    title: str
    # name: str = Field(alias="_name") - если нам надо спарстить по имени, отличающемся в самом json

    @classmethod
    @field_validator('title')
    def title_length(cls, v):
        if len(v) < 5:
            raise ValueError('Title must be at least 5 characters')
        return v
