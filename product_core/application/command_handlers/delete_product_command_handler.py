from buslane.commands import CommandHandler
from fastapi import HTTPException

from product_core.domain.commands.delete_product_command import DeleteProductCommand
from product_core.domain.services.product_service import ProductService


class DeleteProductCommandHandler(CommandHandler[DeleteProductCommand]):

    def __init__(self):
        self.__service = ProductService()

    def handle(self, command: DeleteProductCommand):
        product = self.__service.get_product_by_id(id=command.id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        return self.__service.update(entity=product.delete())
