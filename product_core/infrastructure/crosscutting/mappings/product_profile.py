from mapper.object_mapper import ObjectMapper

from product_core.domain.entities.product import Product
from product_core.infrastructure.data.models.profiles.product_model import ProductModel


class ProductProfile(ObjectMapper):

    def __init__(self):
        super().__init__()
        self.configure()

    def configure(self):
        self.__map_entity_to_model()
        self.__map_model_to_entity()

    def __map_model_to_entity(self):
        self.create_map(ProductModel, Product, {'id': lambda model: str(model.id),
                                                'images': lambda model: [image for image
                                                                         in
                                                                         model.images]})

    def __map_entity_to_model(self):
        self.create_map(Product, ProductModel)
