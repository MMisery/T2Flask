
from townsquare.views import app
from townsquare.models import db

db.init_app(app)

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		if sys.argv[1] == 'init':
			db.create_all()
	else:
		app.run()
