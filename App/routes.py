from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def index():
    user = {'username': ''}
    return render_template('base.html', title='Home', user=user ""

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html
