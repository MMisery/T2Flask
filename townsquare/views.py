#Creation of URIs, passing to templates to create the frontend.

from flask import current_app, render_template, Flask
from .models import Person

#App being set in the views file
app = Flask(__name__)

@app.route('/')
def index():
	return "DEBUG={}".format(current_app.config.get('DEBUG'))


@app.route('/people')
def users():
	people = Person.query.all()
	return render_template('people.html', people=people)