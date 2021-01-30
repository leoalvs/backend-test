from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, HttpUrl, Field, validator
from buslane.commands import Command
from stdnum.ean import is_valid as is_valid_ean


class UpdateProductCommand(Command, BaseModel):
    id: str
    name: Optional[str] = Field(max_length=128)
    ean: Optional[str] = Field(max_length=13)
    description: Optional[str] = Field(max_length=1024)
    images: Optional[List[HttpUrl]]
    price: Optional[int] = Field(gt=0, description="The quantity must be greater than zero")
    quantity: Optional[int] = Field(gt=0, description="The quantity must be greater than zero")

    @validator('id')
    def validate_object_id(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError(f'{value} is not a valid ObjectId')
        return value

    @validator('ean')
    def validate_ean(cls, value):
        if value is None:
            return value
        if not is_valid_ean(value):
            raise ValueError(f'{value} is not a valid EAN-13')
        return value
