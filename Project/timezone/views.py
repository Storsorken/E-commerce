from timezone.models import User
from timezone import app, db
from flask import flash, redirect, render_template, request, url_for
from timezone.forms import RegistrationForm, LoginForm
from flask_login import login_required, login_user, logout_user
from timezone.models import Watch
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')
            print("did not work")

    if form.errors != {}:
        for err_msg in form.errors.values():
            print(err_msg)
            flash(err_msg)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password_hash=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You have successfully registered! You are now log in.')
        return redirect(url_for('index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            print(err_msg)
            flash(err_msg)

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/product_details')
def product_details():
    return render_template('product_details.html')


@app.route('/shop')
@login_required
def shop():
    watches = Watch.query.all()
    return render_template('shop.html', watches=watches)
