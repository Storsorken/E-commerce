from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
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


class CartForm(FlaskForm):
    submit = SubmitField("Proceed to checkout")


class CheckoutForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired(), Length(max=100)])
    last_name = StringField("Last name", validators=[DataRequired(), Length(max=100)])
    phone_number = StringField("Phone number", validators=[DataRequired(), Length(max=20)])
    email = StringField("Email", validators=[DataRequired(), Length(max=150), Email("Invalid email")])
    country = SelectField("Country", choices=["US", "UK", "Netherlands", "France", "Sweden"], validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    postal_code = StringField("Postal code", validators=[DataRequired()])
    submit = SubmitField("Proceed to payment")