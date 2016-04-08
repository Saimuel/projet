from projet import db, security
from flask.ext.security import SQLAlchemyUserDatastore, UserMixin, RoleMixin
import passlib


class User(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Integer)
    properties = db.relationship('Property', backref='user',
                                lazy='dynamic')
    role = db.relationship('Role', backref='user', lazy='dynamic')

    def __init__(self, email, password):
        self.email = email
        self.password = passlib.hash.bcrypt.encrypt(password)

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(255))
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<User %r>' % self.username

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security.datastore = user_datastore


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tenants = db.relationship('Tenant', backref='property', lazy='dynamic')
    expenses = db.relationship('Expense', backref='property', lazy='dynamic')

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return '<User %r>' % self.address


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    payments = db.relationship('Payment', backref='tenant', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'))

    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

    def __repr__(self):
        return '<Payment %r>' % self.id


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    description = db.Column(db.String(200))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))

    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __repr__(self):
        return '<Expense %r>' % self.id
