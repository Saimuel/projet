import os

# Flask configurations
DEBUG = True
SECRET_KEY = "sweet prince"

# Flask-SQLAlchemy configurations
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Secutiry configurations
SECURITY_PASSWORD_HASH = "bcrypt"
