import datetime
import json
from timezone.models import User
from timezone import app, db
from flask import flash, redirect, render_template, request, url_for, jsonify, session
from timezone.forms import RegistrationForm, LoginForm, LogoutForm, CartForm, CheckoutForm
from flask_login import login_required, login_user, logout_user, current_user
from timezone.models import Watch, Purchases, User
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
    form = CartForm()
    return render_template('cart.html', form=form)


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    checkout_form = CheckoutForm()
    cart_form = CartForm()

    if cart_form.validate_on_submit():
        print("THIS IS CODE FOR THE CART FORM")
        cart = request.form['cart']
        cart = json.loads(cart)
        if cart == []:
            flash('Your cart is empty!')
            return redirect(url_for('cart'))

        total_cost = 0
        cart_items = []
        for item in cart:
            watch = Watch.query.get(item['id'])
            cart_items.append((watch.id, watch.name, watch.price, item['quantity']))
            total_cost += watch.price * item['quantity']
        session["cart_items"] = cart_items
        session.modified = True
        session.permanent = False

        return render_template('checkout.html', cart_items=cart_items, total_cost=total_cost, form=checkout_form)
    
    return redirect(url_for('cart'))


@app.route('/make_purchase', methods=['POST'])
def make_purchase():
    form = CheckoutForm()
    print(request.form)
    if form.validate_on_submit():
        cart_items = session.get("cart_items")
        curr_time = datetime.datetime.now()
        userID = current_user.id if current_user.is_authenticated else None
        for watch in cart_items:
            purchase = Purchases(user_id=userID, watch_id=watch[0], first_name=form.first_name.data,
                                last_name=form.last_name.data, phone_number=form.phone_number.data,
                                country=form.country.data, city=form.city.data, address=form.address.data,
                                date_purchased=curr_time, date_returned=None)
            db.session.add(purchase)
            print("Added purchase")
        db.session.commit()
        flash('Thank you! Your order has been placed!')
        flash('You will recieve a confirmation email shortly')
        return redirect(url_for('confirmation'))

    # show errors if form is not valid
    for field, errors in form.errors.items():
        print(field, errors)

    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return(redirect(url_for('logout')))
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


@app.route('/logout', methods=["GET", "POST"])
def logout():
    form = LogoutForm()
    if form.validate_on_submit():
        logout_user()
        return redirect(url_for('login'))

    return render_template('logout.html', form=form)
    

@app.route('/product_details')
def product_details():
    return render_template('product_details.html')


@app.route('/shop')
@login_required
def shop():
    watches = Watch.query.all()
    return render_template('shop.html', hero_area=True, watches=watches)


@app.route('/items/<int:watch_id>')
def item(watch_id):
    watch = Watch.query.get_or_404(watch_id)
    watch_dict = {
        'id': watch.id,
        'name': watch.name,
        'price': watch.price,
        'description': watch.description,
        'image_url': watch.image_url
    }
    return jsonify(watch_dict)

