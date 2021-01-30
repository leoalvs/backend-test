from buslane.commands import CommandHandler
from fastapi import HTTPException

from product_core.domain.commands.create_product_command import CreateProductCommand
from product_core.domain.entities.product import Product
from product_core.domain.services.product_service import ProductService


class CreateProductCommandHandler(CommandHandler[CreateProductCommand]):

    def __init__(self):
        self.__service = ProductService()

    def handle(self, command: CreateProductCommand):
        product_with_name = self.__service.get_product_by_name(command.name)
        if product_with_name:
            raise HTTPException(status_code=400, detail=f'Product with name {command.name} already exists')
        product_with_ean = self.__service.get_product_by_ean(command.ean)
        if product_with_ean:
            raise HTTPException(status_code=400, detail=f'Product with ean {command.ean} already exists')

        return self.__service.save(entity=Product.create(command))
