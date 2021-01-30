from typing import List

from api.routers import command_bus
from product_core.application.queries.product_query import ProductQuery
from product_core.domain.commands.create_product_command import CreateProductCommand
from product_core.domain.commands.delete_product_command import DeleteProductCommand
from product_core.domain.commands.update_product_command import UpdateProductCommand
from product_core.domain.entities.product import Product
from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=Product)
def create_product(command: CreateProductCommand):
    return command_bus.execute(command=command)


@router.put("/", response_model=Product)
def update_product(command: UpdateProductCommand):
    return command_bus.execute(command=command)


@router.delete("/", response_model=Product)
def delete_product(command: DeleteProductCommand):
    return command_bus.execute(command=command)


@router.get("/{id}", response_model=Product)
def get_product(id: str):
    return ProductQuery.get_product(id)


@router.get("/", response_model=List[Product])
def list_products(size: int = 10):
    return ProductQuery.get_products(size)
