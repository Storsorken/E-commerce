from flask import Flask, render_template, request, make_response, flash

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
    
    resp = make_response(render_template('cookie.html'))
    resp.set_cookie('userID', user)
    
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'
