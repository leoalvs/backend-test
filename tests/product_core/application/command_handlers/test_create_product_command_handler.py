from unittest import TestCase, mock

from fastapi import HTTPException

from product_core.application.command_handlers.create_product_command_handler import CreateProductCommandHandler
from product_core.domain.entities.product import Product
from tests.factories.commands.create_product_command_factory import CreateProductCommandFactory


class CreateProductCommandHandlerTest(TestCase):

    def setUp(self):
        self.service = mock.MagicMock()
        self.handler = CreateProductCommandHandler()


    def test_handle(self):
        cmd = CreateProductCommandFactory.build()
        self.service.get_product_by_name = mock.MagicMock(return_value=None)
        self.service.get_product_by_ean = mock.MagicMock(return_value=None)
        result = self.handler.handle(cmd)

        self.assertIsNotNone(result)

    def test_handle_with_existing_name(self):

        cmd = CreateProductCommandFactory.build()
        product = Product.create(cmd)
        self.service.get_product_by_name = mock.MagicMock(return_value=product)
        self.assertRaises(HTTPException, lambda: self.handler.handle(cmd))

    def test_handle_with_existing_ean(self):

        cmd = CreateProductCommandFactory.build()
        product = Product.create(cmd)
        self.service.get_product_by_name = mock.MagicMock(return_value=None)
        self.service.get_product_by_ean = mock.MagicMock(return_value=product)

        self.assertRaises(HTTPException, lambda: self.handler.handle(cmd))