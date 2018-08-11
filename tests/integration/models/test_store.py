from models.store import StoreModel
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
