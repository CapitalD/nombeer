from app import db

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String)
    brews = db.relationship('Brew', backref='beer', lazy='dynamic')

    def __repr__(self):
        return '<Beer %r>' % (self.name)

class Brew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'))
    brew_date = db.Column(db.Integer)
    batch_size = db.Column(db.Float)
    abv = db.Column(db.Float)
    ibu = db.Column(db.Integer)
    kegs = db.relationship('Keg', backref='brew', lazy='dynamic')

    def __repr__(self):
        return '<Brew %r>' % (self.id)

class Keg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brew_id = db.Column(db.Integer, db.ForeignKey('brew.id'))
    kegged_date = db.Column(db.Integer)
    volume = db.Column(db.Float)
    taps = db.relationship('Tap', backref='keg', lazy='dynamic')

    def __repr__(self):
        return '<Keg %r>' % (self.id)

class Tap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keg_id = db.Column(db.Integer, db.ForeignKey('keg.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    identifier = db.Column(db.String)

    def __repr__(self):
        return '<Tap %r>' % (self.identifier)

    def is_pouring(self):
        if self.keg:
            return True
        return False

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    taps = db.relationship('Tap', backref='location', lazy='dynamic')
    
    def __repr__(self):
        return '<Location %r>' % (self.name)
