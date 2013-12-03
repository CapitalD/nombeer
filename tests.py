#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import Beer, Location

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_empty_db(self):
        response = self.app.get('/list')
        assert 'No beers' in response.data

    def test_add_beer(self):
        b1 = Beer(name='Test Beer',kegged_date=1385982000,abv=5.0,ibu=45)
        db.session.add(b1)
        db.session.commit()
        response = self.app.get('/list')
        assert 'No beers' not in response.data
        assert 'Test Beer' in response.data
        assert '1385982000' not in response.data
        assert '2013-12-03' in response.data

    def test_locations(self):
        response = self.app.get('/locations')
        assert 'No locations' in response.data

        l1 = Location(name='Test Location')
        db.session.add(l1)
        db.session.commit()
        response = self.app.get('/locations')
        assert 'Test Location' in response.data

if __name__ == '__main__':
    unittest.main()
