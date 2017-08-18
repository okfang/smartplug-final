from myapp.main import main
from myapp import db
from flask import request, current_app, session, flash, redirect, url_for, render_template
from myapp.main.models import User,Device
from functools import wraps
from datetime import datetime



def login_check(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if not 'logged_in' in session:
            return redirect(url_for('main.login'))
        return func(*args,**kwargs)
    return decorated_func


#注册
@main.route('/sigin', methods=['GET', 'POST'])
def sigin():
    error = None
    if request.method == 'POST':
        user_name =  request.form['username']
        password = request.form['password']
        user = User(user_name,password)
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
        user = User.query.filter_by(user_name = request.form['username']).first()
        if user == None:
            error = 'Invalid username'
        elif request.form['password'] != user.password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['user_id'] = user.id
            flash('You were logged in')
            return redirect(url_for('main.show_devices'))

    return render_template('login.html', error=error)

#简单退出
@main.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main.login'))

#新建设备
@main.route('/device/add', methods=['GET','POST'])
@login_check
def add_device():
    if request.method == 'POST':
        category_name = request.form['category_name']
        device_category_id = category_set[request.form['category_name']]
        device_userid = session['userid']
        device_description = 'smartplug_for_'+category_name
        if request.form['description'] != '':
            device_description = request.form['description']
        device = Device(device_category_id, device_userid, device_description)
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('main.show_devices'))

#展示设备
@main.route('/', methods=['GET','POST'])
@login_check
def show_devices():
    user_id = session['user_id']
    user = None
    error = None
    if user_id:
        user = User.query.filter_by(id = user_id).first()
    devices = user.devices
    error = 'total'+len(devices)+' records'
    return render_template('show_devices.html',error,devices)
