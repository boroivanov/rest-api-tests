'''
BaseTest

The class should be the parent class for each non-unit test.
It allows for instantiation of the database dynamically and
it makes sure it's a new blank database each time.
'''
from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    DATABASE_URI = "sqlite://"

    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = BaseTest.DATABASE_URI
        app.config['DEBUG'] = False
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        with app.app_context():
            db.create_all()
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
