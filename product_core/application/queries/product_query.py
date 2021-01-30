from product_core.domain.services.product_service import ProductService


class ProductQuery:

    def __init__(self):
        self.__service = ProductService()

    @classmethod
    def get_product(cls, id: str):
        query = cls()

        return query.__service.get_product_by_id(id)

    @classmethod
    def get_products(cls, size):
        query = cls()

        return query.__service.get_products(size)
