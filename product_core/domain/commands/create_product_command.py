from typing import List

from pydantic import BaseModel, HttpUrl, Field, validator
from buslane.commands import Command
from stdnum.ean import is_valid as is_valid_ean


class CreateProductCommand(Command, BaseModel):
    name: str = Field(max_length=128)
    ean: str = Field(max_length=13)
    description: str = Field(max_length=1024)
    images: List[HttpUrl]
    price: int = Field(gt=0, description="The price must be greater than zero")
    quantity: int = Field(gt=0, description="The quantity must be greater than zero")

    @validator('ean')
    def validate_ean(cls, value):
        if not is_valid_ean(value):
            raise ValueError(f'{value} is not a valid EAN-13')
        return value
