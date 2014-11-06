#Creation of URIs, passing to templates to create the frontend.

from flask import current_app, render_template

#Grabbing variable app from init file
from townsquare import app

#Grabbing Person model from models file in same directory
from .models import Person


@app.route('/')
def index():
	return "DEBUG={}".format(current_app.config.get('DEBUG'))


@app.route('/people')
def users():
	import pdb
	pdb.set_trace()
	people = Person.query.all()
	return render_template('people.html', people=people)