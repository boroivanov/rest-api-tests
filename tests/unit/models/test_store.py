from models.store import StoreModel
from tests.unit.base_test import BaseTest


class TestStoreModel(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        self.assertEqual(store.name, 'test',
                         'The name of the store does not equal ' +
                         'the constructor argument')
