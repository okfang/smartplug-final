from myapp.main import main
from myapp import db
from flask import request, current_app, session, flash, redirect, url_for, render_template
from myapp.main.models import User
from functools import wraps
from datetime import datetime


def login_check(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if not 'logged_in' in session:
            return redirect(url_for('main.login'))
        return func(*args,**kwargs)
    return decorated_func


@main.route('/')
@login_check
def show_devices():
    return render_template('show_devices.html')

#注册
@main.route('/sigin', methods=['GET', 'POST'])
def sigin():
    error = None
    if request.method == 'POST':
        user_id =  request.form['username']
        password = request.form['password']
        user = User(user_id,password)
        db.session.add(user)
        db.session.commit()

        flash('you have sigin successfully, please login!')
        return redirect(url_for('main.login'))

    return render_template('login.html', error=error, sigin=True)


#简单登录
@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(user_id = request.form['username']).first()
        if user == None:
            error = 'Invalid username'
        elif request.form['password'] != user.password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main.show_devices'))

    return render_template('login.html', error=error)

#简单退出
@main.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main.login'))


