import random
import factory
from faker import Faker

from product_core.domain.commands.create_product_command import CreateProductCommand


class CreateProductCommandFactory(factory.Factory):
    class Meta:
        model = CreateProductCommand

    faker = Faker()

    name = faker.pystr(max_chars=128)
    ean = faker.ean()
    description = faker.pystr(max_chars=1024)
    images = [faker.url()]
    price = random.randint(1, 100)
    quantity = random.randint(1, 100)