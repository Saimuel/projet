from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.security import Security

# Setup Flask application
app = Flask(__name__)
app.config.from_pyfile("config.py")

# Setup Flask-SQLAlchemy
db = SQLAlchemy(app)

# Setup Flask-Security
security = Security(app)

import projet.views, projet.models
