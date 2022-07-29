from timezone import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=100), nullable=False)
    purchases = db.relationship('Purchases', backref='owned_user', lazy=True)


class Watch(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(length=100), nullable=False)
    image_url = db.Column(db.String(length=100), nullable=False)
    purchases = db.relationship('Purchases', backref='watch', lazy=True)

# class Watch(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(length=100), nullable=False)
#     description = db.Column(db.String(length=100), nullable=False)
#     price = db.Column(db.Float(), nullable=False)
#     case_diameter = db.Column(db.Float(), nullable=False)
#     crystal = db.Column(db.String(length=100), nullable=False)
#     water_resistance = db.Column(db.Integer(), nullable=False) #m
#     movement = db.Column(db.String(length=100), nullable=False)
#     case_thickness = db.Column(db.Float(), nullable=False) #mm
#     lugg_width = db.Column(db.Float(), nullable=False)
#     image_url = db.Column(db.String(length=100), nullable=False)
#     purchases = db.relationship('Purchases', backref='watch', lazy=True)


class Purchases(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=True)
    watch_id = db.Column(db.Integer(), db.ForeignKey('watch.id'), nullable=False)
    first_name = db.Column(db.String(length=100), nullable=False)
    last_name = db.Column(db.String(length=100), nullable=False)
    phone_number = db.Column(db.String(length=20), nullable=False)
    country = db.Column(db.String(length=100), nullable=False)
    city = db.Column(db.String(length=100), nullable=False)
    address = db.Column(db.String(length=100), nullable=False)
    date_purchased = db.Column(db.DateTime(), nullable=False)
    date_returned = db.Column(db.DateTime(), nullable=True)

    def __repr__(self):
        return f"Purchases(id={self.id}, user_id={self.user_id}, watch_id={self.watch_id}, \
            date_purchased={self.date_purchased}, date_returned={self.date_returned}), \
            first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, \
            country={self.country}, city={self.city}, address={self.address})"
