from bson import ObjectId
from pydantic import BaseModel, validator
from buslane.commands import Command


class DeleteProductCommand(Command, BaseModel):
    id: str

    @validator('id')
    def validate_object_id(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError(f'{value} is not a valid ObjectId')
        return value
