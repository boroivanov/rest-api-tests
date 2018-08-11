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
    def setUp(self):
        # make sure the db exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # create the app client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # blank the db
        with app.app_context():
            db.session.remove()
            db.drop_all()
