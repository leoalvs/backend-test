from unittest import TestCase

from bson import ObjectId
from faker import Faker

from product_core.domain.commands.update_product_command import UpdateProductCommand


class UpdateProductCommandTest(TestCase):

    def setUp(self):
        self.faker = Faker()

    def test_update_product_command(self):
        kwargs = {
            'id': str(ObjectId()),
            'name': self.faker.pystr(max_chars=128),
            'ean': self.faker.ean(),
            'description': self.faker.pystr(max_chars=1024),
            'images': [self.faker.url()],
            'price': self.faker.pyint(min_value=0, max_value=9999),
            'quantity': self.faker.pyint(min_value=0, max_value=9999)
        }

        command = UpdateProductCommand(**kwargs)

        self.assertEqual(command.id, kwargs['id'])
        self.assertEqual(command.name, kwargs['name'])
        self.assertEqual(command.ean, kwargs['ean'])
        self.assertEqual(command.description, kwargs['description'])
        self.assertEqual(command.images, kwargs['images'])
        self.assertEqual(command.price, kwargs['price'])
        self.assertEqual(command.quantity, kwargs['quantity'])
