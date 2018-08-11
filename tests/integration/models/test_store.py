from models.store import StoreModel
from tests.integration.base_test import BaseTest


class TestStore(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(), [],
                             'Store items length should be 0 ' +
                             'at store creation.')
