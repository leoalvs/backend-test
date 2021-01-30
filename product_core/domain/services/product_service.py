from product_core.domain.entities.product import Product
from product_core.infrastructure.data.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.__repo = ProductRepository()

    @classmethod
    def save(cls, entity: Product):
        service = cls()

        product = service.__repo.add(entity)

        return product

    @classmethod
    def update(cls, entity: Product):
        service = cls()

        product = service.__repo.update(entity)

        return product

    @classmethod
    def get_product_by_id(cls, id: str):
        service = cls()

        product = service.__repo.find_by_id(id=id)
        return product

    @classmethod
    def get_product_by_name(cls, name: str):
        service = cls()

        product = service.__repo.find_by_name(name=name)
        return product

    @classmethod
    def get_product_by_ean(cls, ean: str):
        service = cls()

        product = service.__repo.find_by_ean(ean=ean)
        return product


    @classmethod
    def get_products(cls, size):
        service = cls()

        products = service.__repo.find_all(size)

        return products
