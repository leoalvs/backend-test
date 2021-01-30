from unittest import TestCase

from bson import ObjectId
from product_core.domain.commands.delete_product_command import DeleteProductCommand


class DeleteProductCommandTest(TestCase):

    def test_delete_product_command(self):
        kwargs = {
            'id': str(ObjectId())
        }

        command = DeleteProductCommand(**kwargs)

        self.assertEqual(command.id, kwargs['id'])
