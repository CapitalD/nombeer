from flask.ext.wtf import Form
from wtforms import Form, TextField, FloatField, DateField, IntegerField, validators

class AddBeerForm(Form):
    name = TextField('Name', [
        validators.InputRequired()
    ])
    kegged_date = DateField('Date Kegged')
    abv = FloatField('ABV', [
        validators.NumberRange(min=0, max=100)
    ])
    ibu = IntegerField('IBU', [
        validators.NumberRange(min=0, max=1000)
    ])
