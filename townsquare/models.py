#Backend of the application, setting up the database and establishing the ORM.

from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime

#Grabbing db variable from init file
from . import db

class Person(db.Model):

	"""
	Generic model to interact with the database.
	Will be extending this for more specific cases
	"""

	# Variable for the ID - setting it to be the primary key
	id = Column(Integer, primary_key=True)

	first_name = Column(Unicode(100))
	middle_name = Column(Unicode(100))
	last_name = Column(Unicode(100))
	#email = Column(Unicode(100))

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __repr__(self):
		return '<Person %r>' % self.first_name


class Volunteer(Person):

	"""
	Model for a volunteer. Extended from the "Person" model
	"""

	# ID is related to the corresponding "Person" ID
	id = Column(Integer, ForeignKey('person.id'), primary_key=True)
	signup_date = Column(DateTime)
	birth_date = Column(DateTime)
	#Date Signed Waiver and Code of Conduct
	legal_date = Column(DateTime)
