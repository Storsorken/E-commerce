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


class Purchases(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    watch_id = db.Column(db.Integer(), db.ForeignKey('watch.id'), nullable=False)
    date_purchased = db.Column(db.DateTime(), nullable=False)
    date_returned = db.Column(db.DateTime(), nullable=True)

    def __repr__(self):
        return f"Purchases(id={self.id}, user_id={self.user_id}, watch_id={self.watch_id}, date_purchased={self.date_purchased}, date_returned={self.date_returned})"