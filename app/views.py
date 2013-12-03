from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from forms import AddBeerForm, AddLocationForm
from models import Beer, Location

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/list')
def list_beers():
    beers = Beer.query.order_by(Beer.kegged_date.desc()).all()
    return render_template('list_beers.html', beers=beers)

@app.route('/add', methods=['GET','POST'])
def add_beer():
    form = AddBeerForm(request.form)
    if request.method == 'POST' and form.validate(): 
        new_beer = Beer(name = form.name.data, kegged_date = form.kegged_date.data.strftime('%s'), abv=form.abv.data, ibu=form.ibu.data)
        db.session.add(new_beer)
        db.session.commit()
        flash('New beer was successfully added')
        return redirect(url_for('list_beers')) 
    return render_template('add_beer.html', form=form)

@app.route('/locations')
def list_locations():
    locations = Location.query.order_by(Location.name).all()
    return render_template('list_locations.html', locations=locations)

@app.route('/add_location', methods=['GET','POST'])
def add_location():
    form = AddLocationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_location = Location(name = form.name.data)
        db.session.add(new_location)
        db.session.commit()
        flash('New location was successfully added')
        return redirect(url_for('list_locations'))
    return render_template('add_location.html', form=form)
