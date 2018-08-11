from unittest import TestCase
from models.item import ItemModel


class TestItemModel(TestCase):
    def test_init(self):
        item = ItemModel('test', 123.00, 1)
        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 123.00)

    def test_json(self):
        item = ItemModel('test', 123.00, 1)
        self.assertDictEqual(item.json(), {'name': 'test', 'price': 123.00})
