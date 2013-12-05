from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from models import Beer, Brew, Keg, Tap, Location
from forms import AddBeerForm, AddLocationForm

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/beer/<int:keg_id>')
def show_beer(keg_id):
    selected_beer = Keg.query.filter_by(id = keg_id).first_or_404()
    return render_template('show_beer.html', keg=selected_beer) 

@app.route('/ontap/')
def list_ontap():
    pouring = Keg.query.join(Tap, (Tap.keg_id == Keg.id)).all()
    return render_template('ontap.html', pouring=pouring)

@app.route('/ontap/<int:location_id>')
def list_ontap_at_location(location_id):
    pouring = Keg.query.join(Tap, (Tap.keg_id == Keg.id)).filter(Tap.location_id == location_id).all()
    loc_name = Location.query.filter_by(id = location_id).first_or_404()
    return render_template('ontap.html', pouring=pouring, location=loc_name)

#@app.route('/list')
#def list_beers():
#    beers = Beer.query.order_by(Beer.kegged_date.desc()).all()
#    return render_template('list_beers.html', beers=beers)

#@app.route('/add', methods=['GET','POST'])
#def add_beer():
#    form = AddBeerForm(request.form)
#    if request.method == 'POST' and form.validate(): 
#        new_beer = Beer(name = form.name.data, kegged_date = form.kegged_date.data.strftime('%s'), abv=form.abv.data, ibu=form.ibu.data)
#        db.session.add(new_beer)
#        db.session.commit()
#        flash('New beer was successfully added')
#        return redirect(url_for('list_beers')) 
#    return render_template('add_beer.html', form=form)

#@app.route('/locations')
#def list_locations():
#    locations = Location.query.order_by(Location.name).all()
#    return render_template('list_locations.html', locations=locations)

#@app.route('/add_location', methods=['GET','POST'])
#def add_location():
#    form = AddLocationForm(request.form)
#    if request.method == 'POST' and form.validate():
#        new_location = Location(name = form.name.data)
#        db.session.add(new_location)
#        db.session.commit()
#        flash('New location was successfully added')
#        return redirect(url_for('list_locations'))
#    return render_template('add_location.html', form=form)
