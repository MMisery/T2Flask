
from townsquare.models import db,app, manager

db.init_app(app)

if __name__ == '__main__':
	manager.run()