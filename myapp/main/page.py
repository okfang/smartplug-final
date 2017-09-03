from datetime import datetime,date
from functools import wraps
from urllib import parse
import json

from flask import request, session, flash, redirect, url_for, render_template, jsonify
from flask_login import login_required

from myapp import db
from myapp.forms import AddDeviceForm
from myapp.main import main
from myapp.models import User, Device, Device_energy_info


###############   All Page  post form   ###########################

#主页
@main.route('/')
# @login_required
def index():
    return render_template('index.html')


#主页
@main.route('/home')
@login_required
def home():
    user = User.query.get(session["user_id"])
    data = {}
    data["username"]=user.username
    data["devices"] =[device.name for device in user.devices.all()]
    return render_template('home.html',data=data)

#新建设备
@main.route('/device/add', methods=['GET','POST'])
@login_required
def add_device():
    form = AddDeviceForm()
    if form.validate_on_submit():
        device = Device(category_type=form.category_type.data,
                        description=form.description.data,
                        user_id=session["user_id"],
                        begin_use_time=datetime.utcnow(),
                        status = 1)
        count = Device.query.count() + 1
        device.name = 'smartplug_{id}_for_{category}'.format(id = count, category = device.category_type)

        db.session.add(device)
        db.session.commit()
        flash('add device successfully!')
        return redirect(url_for('main.home'))
    return render_template('add_device.html', form=form)

    # device = Device(category_type=request.form['type'],
    #                 description=request.form['description'],
    #                 user_id=session["user_id"],
    #                 begin_use_time=datetime.utcnow())
    # count = Device.query.count() + 1
    # device.name = 'smartplug_{id}_for_{category}'.format(count, device.category_type)
    # db.session.add(device)
    # db.session.commit()
    # return jsonify({"code":200}),200




