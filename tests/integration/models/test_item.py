from tests.base_test import BaseTest
from models.item import ItemModel


class TestItem(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 123.00)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f'Found an item with name ' +
                              '{item.name}, but expected not to.')

            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 f'Couldn\'t find an item with name ' +
                                 '{item.name}, but expected to.')

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f'Found an item with name {item.name}, ' +
                              'but expected not to.')
