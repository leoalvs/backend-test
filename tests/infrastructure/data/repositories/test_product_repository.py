from unittest import TestCase

from product_core.domain.entities.product import Product
from product_core.infrastructure.data.repositories.product_repository import ProductRepository
from tests.factories.commands.create_product_command_factory import CreateProductCommandFactory
from tests.factories.models.product_model_factory import ProductModelFactory


class ProductRepositoryTest(TestCase):

    def setUp(self):

        self.repo = ProductRepository()

    def test_map_model(self):
        cmd = CreateProductCommandFactory.build()
        product = Product.create(cmd)

        model = self.repo.map_model(product)

        self.assertEqual(model.id, product.id)
        self.assertEqual(model.name, product.name)
        self.assertEqual(model.ean, product.ean)
        self.assertEqual(model.description, product.description)
        self.assertEqual(model.images, product.images)
        self.assertEqual(model.status, product.status)
        self.assertEqual(model.price, product.price)
        self.assertEqual(model.quantity, product.quantity)
        self.assertEqual(model.created_at, product.created_at)
        self.assertEqual(model.updated_at, product.updated_at)
        self.assertEqual(model.deleted_at, product.deleted_at)


    def test_map_entity(self):
        model = ProductModelFactory.build()

        product = self.repo.map_entity(model)

        self.assertEqual(model.name, product.name)
        self.assertEqual(model.ean, product.ean)
        self.assertEqual(model.description, product.description)
        self.assertEqual(model.images, product.images)
        self.assertEqual(model.status, product.status)
        self.assertEqual(model.price, product.price)
        self.assertEqual(model.quantity, product.quantity)
        self.assertEqual(model.created_at, product.created_at)
        self.assertEqual(model.updated_at, product.updated_at)
        self.assertEqual(model.deleted_at, product.deleted_at)