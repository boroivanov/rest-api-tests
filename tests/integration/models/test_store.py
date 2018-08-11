from models.store import StoreModel
from models.item import ItemModel
from tests.integration.base_test import BaseTest


class TestStore(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(), [],
                             'Store items length should be 0 ' +
                             'at store creation.')

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            self.assertIsNone(StoreModel.find_by_name('test'),
                              'Test store already exists in the database.')

            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 'Test store is not in the database.')

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('test'),
                              'Test store was not deleted from the database.')

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test_item', 123.00, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1,
                             'Store items should have a length of 1.')
            self.assertEqual(store.items.first().name, 'test_item',
                             'test_item not in test_store items.')
