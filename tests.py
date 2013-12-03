#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import Beer

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
        rv = self.app.get('/list')
        assert 'No beers' in rv.data

    def test_add_beer(self):
        b1 = Beer(name='Test Beer',kegged_date=1385982000,abv=5.0,ibu=45)
        db.session.add(b1)
        db.session.commit()
        rv = self.app.get('/list')
        assert 'No beers' not in rv.data
        assert 'Test Beer' in rv.data
        assert '1385982000' not in rv.data
        assert '2013-12-03' in rv.data

if __name__ == '__main__':
    unittest.main()
