from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from models import Beer, Brew, Keg, Tap, Location
from forms import BrewdayForm, AddLocationForm
from sqlalchemy import func

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/beer/<int:keg_id>')
def show_beer(keg_id):
    selected_beer = Keg.query.filter_by(id = keg_id).first_or_404()
    return render_template('show_beer.html', keg=selected_beer) 

@app.route('/ontap/')
def list_ontap():
    kegs = Keg.query.filter(Keg.tap != None).all()
    return render_template('ontap.html', kegs=kegs)

@app.route('/ontap/<int:location_id>')
def list_ontap_at_location(location_id):
    selected_location = Location.query.filter_by(id = location_id).first_or_404()
    return render_template('ontap_at.html', location=selected_location)

@app.route('/brewday/', methods=['GET','POST'])
def brewday():
    form = BrewdayForm(request.form)
    form.select_beer.choices = [(beer.id, beer.name) for beer in Beer.query.order_by('name')]
    form.select_beer.choices.append([0, "Add new..."])
    if request.method == 'POST' and form.validate(): 
        brew = Brew(brew_date = form.brew_date.data.strftime('%s'), batch_size = form.batch_size.data, abv = form.abv.data, ibu=form.ibu.data)
        if form.beer_name:
            beer = Beer(name = form.beer_name.data, description = form.beer_desc.data)
            brew.beer = beer
        else:
            brew.beer = form.select_beer.data
        db.session.add(brew)
        db.session.add(beer)
        db.session.commit()
        flash('Brewday was successfully added')
        return redirect(url_for('brewday')) 
    return render_template('brewday.html', form=form)

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
