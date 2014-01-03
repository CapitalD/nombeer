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

    def is_kegged(self):
        if self.kegs.count() > 0:
            return True
        return False

    def __repr__(self):
        return '<Brew %r>' % (self.id)

class Keg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brew_id = db.Column(db.Integer, db.ForeignKey('brew.id'))
    kegged_date = db.Column(db.Integer)
    volume = db.Column(db.Float)
    tap = db.relationship('Tap', backref='keg', uselist=False)

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

    def number_of_taps(self):
        return len(self.taps.all())

    def column_span(self):
        req_taps = self.number_of_taps()
        for case in switch(req_taps):
            if case(1):
                return 12
                break
            if case(2):
                return 6
                break
            if case(3):
                return 4
                break
            if case(4):
                return 3
                break
            if case(6):
                return 2
                break
            if case():
                return 12

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
