from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
	 
# Bringing in Flask SQLAlchemy to deal with interacting with the database
from flask.ext.sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config.from_envvar('T2FLASK_SETTINGS', silent=True)


# Having the database be accessed with SQLAlchemy
db = SQLAlchemy(app)

# Creating a generic model to interact with the database. Will be extending this for more specific cases
class Person(db.Model):
	
	# Want to give the table a specific name
	__tablename__ = 'person'
	
	# Variable for the ID - setting it to be the primary key
	id = db.Column(db.Integer, primary_key=True)
	
	first_name = db.Column(db.String(100))
	middle_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	
	def __init__(self, first_name, middle_name, last_name):
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
		
	def __repr__(self):
		return '<Person %r>' % self.first_name


# Model for a volunteer. Extended from the "Person" model	
class Volunteer(Person):
	__tablename__ = 'volunteer'
	
	# ID is related to the corresponding "Person" ID
	id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
	



if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		if sys.argv[1] == 'init':
			db.create_all()
	else:
		app.run()
