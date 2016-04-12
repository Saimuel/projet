from wtforms import Form, BooleanField, TextField, PasswordField, validators


class RegistrationForm(Form):
    email = TextField('Email Address',
                      [validators.Email(
                       message="Adresse de messagerie invalide")])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    email = TextField("Email", [validators.Length(min=3, max=35)])
    password = PasswordField("Mot de passe")
