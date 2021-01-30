from datetime import datetime
from typing import List

from fastapi import HTTPException
from pydantic import BaseModel, HttpUrl

from product_core.domain.commands.create_product_command import CreateProductCommand
from product_core.domain.commands.update_product_command import UpdateProductCommand
from product_core.domain.enums.product_status import ProductStatus


class Product(BaseModel):
    id: str = None
    name: str = None
    ean: str = None
    description: str = None
    images: List[HttpUrl] = None
    status: ProductStatus = None
    price: int = None
    quantity: int = None
    created_at: datetime = None
    updated_at: datetime = None
    deleted_at: datetime = None

    @classmethod
    def create(cls, command: CreateProductCommand):
        product = cls()

        product.id = None
        product.name = command.name
        product.quantity = command.quantity
        product.ean = command.ean
        product.description = command.description
        product.images = command.images
        product.status = ProductStatus.ACTIVE
        product.price = command.price
        product.created_at = datetime.now()

        return product

    def update(self, command: UpdateProductCommand):
        if command.price <= (self.price / 2):
            raise HTTPException(status_code=403, detail=f"Can't drop the price below 50% of it's current price")

        self.name = command.name or self.name
        self.quantity = command.quantity or self.quantity
        self.ean = command.ean or self.ean
        self.description = command.description or self.description
        self.images = command.images or self.images
        self.price = command.price or self.price
        self.updated_at = datetime.now()

        return self

    def delete(self):
        self.status = ProductStatus.DELETED
        self.deleted_at = datetime.now()

        return self

    def activate(self):
        self.status = ProductStatus.ACTIVE

        return self
