from tests.unit.base_test import BaseTest
from models.item import ItemModel


class TestItemModel(BaseTest):
    def test_init(self):
        item = ItemModel('test', 123.00, 1)
        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 123.00)
        self.assertEqual(item.store_id, 1)

    def test_json(self):
        item = ItemModel('test', 123.00, 1)
        self.assertDictEqual(item.json(), {'name': 'test', 'price': 123.00})
        self.assertEqual(item.store_id, 1)
