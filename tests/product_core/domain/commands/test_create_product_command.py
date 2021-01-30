from unittest import TestCase

from faker import Faker

from product_core.domain.commands.create_product_command import CreateProductCommand


class CreateProductCommandTest(TestCase):

    def setUp(self):
        self.faker = Faker()

    def test_create_product_command(self):
        kwargs = {
            'name': self.faker.pystr(max_chars=128),
            'ean': self.faker.ean(),
            'description': self.faker.pystr(max_chars=1024),
            'images': [self.faker.url()],
            'price': self.faker.pyint(min_value=0, max_value=9999),
            'quantity': self.faker.pyint(min_value=0, max_value=9999)
        }

        command = CreateProductCommand(**kwargs)

        self.assertEqual(command.name, kwargs['name'])
        self.assertEqual(command.ean, kwargs['ean'])
        self.assertEqual(command.description, kwargs['description'])
        self.assertEqual(command.images, kwargs['images'])
        self.assertEqual(command.price, kwargs['price'])
        self.assertEqual(command.quantity, kwargs['quantity'])
