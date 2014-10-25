#Creation of URIs, passing to templates to create the frontend.


from flask import current_app, render_template, Flask
from .models import Person
import config

# Create the application
app = Flask(__name__)

# Set config on app
app.config.from_object(config)



@app.route('/')
def index():
	return "DEBUG={}".format(current_app.config.get('DEBUG'))


@app.route('/people')
def users():
	import pdb
	pdb.set_trace()
	people = Person.query.all()
	return render_template('people.html', people=people)