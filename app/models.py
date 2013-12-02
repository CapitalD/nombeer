from app import db

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    kegged_date = db.Column(db.Integer)
    abv = db.Column(db.Float)
    ibu = db.Column(db.Integer)

    def __repr__(self):
        return '<Beer %r>' % (self.name)
