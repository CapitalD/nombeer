from flask.ext.wtf import Form
from wtforms import Form, TextField, FloatField, DateField, IntegerField, SelectField, validators

class PackdayForm(Form):
    select_brew = SelectField('Brew', coerce=int)

class BrewdayForm(Form):
    brew_date = DateField('Brew Date')
    select_beer = SelectField('Beer', coerce=int)
    beer_name = TextField('Beer Name', [
        validators.InputRequired()
    ])
    beer_desc = TextField('Description')
    batch_size = FloatField('Batch Size')
    abv = FloatField('ABV', [
        validators.NumberRange(min=0, max=100)
    ])
    ibu = IntegerField('IBU', [
        validators.NumberRange(min=0, max=1000)
    ])


class AddLocationForm(Form):
    name = TextField('Name', [
        validators.InputRequired()
    ])
    tap1_name = TextField('Tap 1', [
        validators.InputRequired()
    ])
