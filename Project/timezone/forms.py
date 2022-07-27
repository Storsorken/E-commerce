from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email("Invalid email")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, message="Too short password")])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords not equal")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email("Invalid email")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class LogoutForm(FlaskForm):
    submit = SubmitField("Log out")


class CheckoutForm(FlaskForm):
    submit = SubmitField("Proceed to checkout")