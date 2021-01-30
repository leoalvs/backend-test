from datetime import datetime
import random
from unittest import TestCase
from freezegun import freeze_time

from product_core.domain.entities.product import Product
from product_core.domain.enums.product_status import ProductStatus
from tests.factories.commands.create_product_command_factory import CreateProductCommandFactory
from tests.factories.commands.update_product_command_factory import UpdateProductCommandFactory


class ProductTest(TestCase):

    @freeze_time(datetime.now())
    def test_create(self):
        cmd = CreateProductCommandFactory.build()

        product = Product.create(command=cmd)

        self.assertEqual(product.name, cmd.name)
        self.assertEqual(product.ean, cmd.ean)
        self.assertEqual(product.description, cmd.description)
        self.assertEqual(product.images, cmd.images)
        self.assertEqual(product.status, ProductStatus.ACTIVE)
        self.assertEqual(product.price, cmd.price)
        self.assertEqual(product.quantity, cmd.quantity)
        self.assertEqual(product.created_at, datetime.now())
        self.assertIsNone(product.updated_at)
        self.assertIsNone(product.deleted_at)

    @freeze_time(datetime.now())
    def test_update(self):
        cmd = CreateProductCommandFactory.build(price=random.randint(90, 100))
        update_cmd = UpdateProductCommandFactory.build(price=random.randint(90, 100))
        product = Product.create(command=cmd)
        product.update(command=update_cmd)

        self.assertEqual(product.name, update_cmd.name)
        self.assertEqual(product.ean, update_cmd.ean)
        self.assertEqual(product.description, update_cmd.description)
        self.assertEqual(product.images, update_cmd.images)
        self.assertEqual(product.price, update_cmd.price)
        self.assertEqual(product.quantity, update_cmd.quantity)
        self.assertEqual(product.updated_at, datetime.now())
        self.assertIsNone(product.deleted_at)


    @freeze_time(datetime.now())
    def test_delete(self):
        cmd = CreateProductCommandFactory.build()
        product = Product.create(command=cmd)
        product.delete()

        self.assertEqual(product.status, ProductStatus.DELETED)
        self.assertEqual(product.deleted_at, datetime.now())
