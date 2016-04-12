from projet import app, db
from flask import render_template, request, redirect, url_for
from projet.forms import RegistrationForm, LoginForm
from projet.models import User


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            return redirect(url_for('home'))
        else:
            return render_template("login.html", form=form)
    else:
        return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.email.data, form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return redirect(url_for('login'))
    return render_template('register.html', form=form)
