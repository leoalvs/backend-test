from bson import ObjectId
import factory
import random

from faker import Faker

from product_core.domain.enums.product_status import ProductStatus
from product_core.infrastructure.data.models.profiles.product_model import ProductModel

faker = Faker()

class ProductModelFactory(factory.Factory):
    class Meta:
        model = ProductModel


    id = str(ObjectId())
    name = faker.pystr(max_chars=128)
    ean = faker.ean()
    description = faker.pystr(max_chars=1024)
    images = [faker.url()]
    price = random.randint(1, 100)
    quantity = random.randint(1, 100)
    status = random.choice([ProductStatus.ACTIVE, ProductStatus.DELETED])
    created_at = faker.date()
    updated_at = faker.date()
    deleted_at = faker.date()