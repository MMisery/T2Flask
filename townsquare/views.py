#Creation of URIs, passing to templates to create the frontend.

from .models import app, Person

@app.route('/')
def index():
	return "DEBUG={}".format(current_app.config.get('DEBUG'))


@app.route('/people')
def users():
	import pdb
	pdb.set_trace()
	people = Person.query.all()
	return render_template('people.html', people=people)