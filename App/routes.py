from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    user = {'username': ''}
    return render_template('base.html', title='Home', user=user ""
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
