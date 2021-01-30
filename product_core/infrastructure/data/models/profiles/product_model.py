from mongoengine import Document, StringField, IntField, ObjectIdField, DateTimeField, ListField


class ProductModel(Document):
    id = ObjectIdField(primary_key=True)
    name = StringField()
    ean = StringField()
    description = StringField()
    images = ListField(StringField())
    price = IntField()
    quantity = IntField()
    status = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    deleted_at = DateTimeField()

    meta = {'collection': 'product'}
