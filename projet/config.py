import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname, 'app.db')
SECURITY_PASSWORD_HASH = "bcrypt"
DEBUG = True
SECRET_KEY = "sweet prince"
SQLALCHEMY_TRACK_MODIFICATIONS = False
