from buslane.commands import CommandHandler
from fastapi import HTTPException

from product_core.domain.commands.update_product_command import UpdateProductCommand
from product_core.domain.enums.product_status import ProductStatus
from product_core.domain.services.product_service import ProductService


class UpdateProductCommandHandler(CommandHandler[UpdateProductCommand]):

    def __init__(self):
        self.__service = ProductService()

    def handle(self, command: UpdateProductCommand):
        product = self.__service.get_product_by_id(id=command.id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {command.id} not found")
        if product.status == ProductStatus.DELETED:
            raise HTTPException(status_code=403, detail=f"Can't update deleted products")

        return self.__service.update(entity=product.update(command))
