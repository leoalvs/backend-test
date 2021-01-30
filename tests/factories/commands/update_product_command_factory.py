import random
import factory
from bson import ObjectId
from faker import Faker

from product_core.domain.commands.update_product_command import UpdateProductCommand


class UpdateProductCommandFactory(factory.Factory):
    class Meta:
        model = UpdateProductCommand

    faker = Faker()

    id = str(ObjectId())
    name = faker.pystr(max_chars=128)
    ean = faker.ean()
    description = faker.pystr(max_chars=1024)
    images = [faker.url()]
    price = random.randint(1, 100)
    quantity = random.randint(1, 100)
