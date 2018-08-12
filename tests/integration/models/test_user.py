from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            err_msg = 'Found an user with name "test" before save_to_db'
            self.assertIsNone(UserModel.find_by_username('test'), err_msg)
            err_msg = 'Found an user with id "1" before save_to_db'
            self.assertIsNone(UserModel.find_by_id(1), err_msg)

            user.save_to_db()

            err_msg = 'Did not find an user with name "test" after save_to_db'
            self.assertIsNotNone(UserModel.find_by_username('test'), err_msg)
            err_msg = 'Did not find an user with id "1" after save_to_db'
            self.assertIsNotNone(UserModel.find_by_id(1), err_msg)
