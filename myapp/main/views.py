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




###############   API     ###########################
#验证token
def api_auth(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        token = kwargs['token']
        user = User.verifg_auth_token(token)
        if user:
            return func(user.id,*args, **kwargs)
        return jsonify({'code':403, 'message':'unvalid token or token has expired'})
    return decorated_func

@main.route('/token',methods=['POST'])
def get_token():
    # print(request.get_data())
    data = request.get_json()
    email = data['email']
    password = data['password']
    print(email,password)
    user = User.query.filter_by(email=email).first()
    if user is not None:
        if user.verify_password(password):
            return jsonify({'code':200,'token':user.generate_auth_token().decode('ascii')})
    return jsonify({"code":403, "message":"unvalid username or password"})

#获取设备情况
@main.route('/device/<int:device_id>')
@api_auth
def get_device(device_id):
    device = Device.query.get(device_id)
    data = {}
    data['name'] = device.name
    data['power'] = device.power
    data['total_energy_consumption'] = device.total_energy_consumption
    return jsonify(data)

#获取用户设备列表
@main.route('/user/device/list')
@login_required
def get_user_device_list(user):
    data = {}
    data['user_id'] = user.id
    data['devices'] = [[device.name,url_for('main.get_device',device_id=device.id)] for device in user.devices]
    return jsonify(data)


#设备上传接口
@main.route('/device/info/upload', methods=['POST'])
@login_required
def upload_device_info(user_id):
    data = request.get_json()
    device_info = Device_energy_info(
        device_id = data.device_id,
        upload_time = datetime.utcnow(),
        month_energy = data.year_detail.month_list.month_list[7].energy,
        day_energy = data.mon_detail.day_list[data.time.day-1],
        current_power = data.power_current.power,
        year = data.time.year,
        month = data.time.month,
        day = data.time.day,
        hour = data.time.hour
    )

    #更新device的当前功率
    if data.device_id:
        device = Device.query.get(data.device_id)
        device.power = data.power_current.power
        device.total_energy_consumption = data.mon_detail.day_list[data.time.day-1]
        db.session.add(device)

    db.session.add(device_info)
    db.session.commit()

    return jsonify({'code':200})


@main.route('/json')
def json():
    data = {"power":456}
    return jsonify(data)

@main.route('/')
def index():
    return render_template('index.html')

###############   Page      ###########################


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
                        user_id = session["user_id"],
                        begin_use_time=datetime.utcnow())
        count = Device.query.count()+1
        device.name = 'smartplug_{id}_for_{category}'.format(count,device.category_type)

        db.session.add(device)
        db.session.commit()
        flash('add device successfully!')
        return redirect(url_for('main.home'))
    return render_template('add_device.html',form=form)

#展示设备
@main.route('/device/list', methods=['GET','POST'])
@login_required
def show_devices():
    user_id = session['user_id']
    user = None
    error = None
    devices = None
    if user_id:
        user = User.query.filter_by(id = user_id).first()
        devices = user.devices
        error = 'total '+len(devices)+' records'
    else:
        error = "no session['user_id'] please login!"
        return redirect(url_for('main.login'))
    return render_template('show_devices.html',error,devices)



