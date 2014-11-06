#File used for some imports. Referred to when the "townsquare" folder is imported. Kind of like an index file.

from flask import Flask

#Configuration file used for app
import config


from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# Create the application
app = Flask(__name__)

# Set config on app
app.config.from_object(config)


# define our database here
db = SQLAlchemy()

#Access to views must be imported after declaring app, db, and app.config
import townsquare.views


#Attempting to set up database migrations so we can edit a model and update the database accordingly
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

