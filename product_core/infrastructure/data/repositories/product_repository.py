from bson import ObjectId
from product_core.domain.entities.product import Product
from product_core.infrastructure.crosscutting.mappings.product_profile import ProductProfile
from product_core.infrastructure.data.models.profiles.product_model import ProductModel


class ProductRepository:

    def __init__(self):
        self.__mapper = ProductProfile()

    def add(self, entity):
        model = self.map_model(entity)
        model.id = ObjectId()
        model.save()
        return self.map_entity(model)

    def update(self, entity):
        model = self.map_model(entity)
        model.save()
        return self.map_entity(model)

    def find_by_id(self, id):

        model = ProductModel.objects(id=id)

        return self.map_entity(model[0]) if model else None

    def find_by_name(self, name):

        model = ProductModel.objects(name=name)

        return self.map_entity(model[0]) if model else None

    def find_by_ean(self, ean):

        model = ProductModel.objects(ean=ean)

        return self.map_entity(model[0]) if model else None

    def find_all(self, size):

        models = ProductModel.objects()[:size].order_by('-id')

        return [self.map_entity(model) for model in models]

    def map_model(self, entity: Product) -> ProductModel:
        return self.__mapper.map(entity, ProductModel)

    def map_entity(self, model: ProductModel) -> Product:
        return self.__mapper.map(model, Product)
