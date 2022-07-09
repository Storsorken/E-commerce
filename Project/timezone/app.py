from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/product_details')
def product_details():
    return render_template('product_details.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')
