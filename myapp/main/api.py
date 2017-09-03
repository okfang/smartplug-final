from datetime import datetime,date
from functools import wraps
import random
import json as json2

from flask import request, session, flash, redirect, url_for, render_template, jsonify, make_response, Response

from myapp import db
from myapp.main import main
from myapp.models import User, Device, Device_energy_info,Category
import config


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

###############   API     ###########################

@main.route('/user/info')
def get_user_info():
    data = {}
    user = User.query.get(config.USER_ID)
    devices = user.devices.all()
    total_consumption = sum([device.total_energy_consumption for device in devices])
    total_power = sum([device.power for device in devices])
    data['consumption'] = str(total_consumption)+' KWH'
    data['plugnumber'] = len(devices)
    data["power"] = str(sum([device.power for device in devices])) + ' W'
    return jsonify(data), 200

@main.route('/user/plugs')
def get_plugs():
    devicelist = Device.query.all()
    data = []
    for device in devicelist:
        data.append({'name' :device.name ,'id':device.id,'type':device.category_type,'description':device.description,'consumption':device.total_energy_consumption, 'power':device.power})
    # data = [{'name' :'plug1' ,'id':'asdkfbee33','type':'what?','description':'天王盖地虎','consumption':'100kwh'},
    #         {'name' :'plug2' ,'id':'asdkfbee33','type':'what?','description':'宝塔镇河妖','consumption':'122kwh'},
    #         {'name' :'plug3' ,'id':'asdkfbee33','type':'what?','description':'左青龙右白虎','consumption':'233kwh'}
    # ]
    response = make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response, 200

@main.route('/user/daily/powerchart')
def get_daily_powerchart():
    device_info_list = Device_energy_info.query.filter_by(device_id=config.DEVICE_ID).order_by(Device_energy_info.id.desc()).limit(5).all()
    print(device_info_list)
    data = {}
    data["data"] = [device_info.current_power for device_info in device_info_list][::-1]
    data["label"] = ["%d:%d:%d"%(device_info.hour, device_info.min, device_info.sec) for device_info in device_info_list][::-1]

    response = make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response, 200


@main.route('/user/daily/linechart')
def get_daily_linechart():
    data = {}
    data["labels"] = ["{h}:00".format(h=i) for i in range(1,25)]
    data['datasets'] = []
    user = User.query.get(config.USER_ID)
    devices = user.devices.all()
    labels = ['Total']
    labels.extend([device.category_type for device in devices])

    for i in range(len(labels)):
        data['datasets'].append({  'label' :labels[i],'backgroundColor' : '#00FF00', 'borderColor' : 'palette.transparent',  'data' :[str(random.randint(0, 20)) for i in range(len(data['labels']))] })
    # data = {
    #     'labels' : ['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00'],
    #     'datasets' :[
    #                 {  'label' : 'Total', 'backgroundColor' : '#00FF00', 'borderColor' : 'palette.transparent', 'data' : [
    #                 '0.1', '0.2', '3.1', '4.5', '5.8', '1.2', '1.1']},
    #                 {'label' : 'Light', 'backgroundColor' : '#FF0000', 'borderColor' : 'palette.transparent', 'data' : [
    #                 '1', '2', '3', '4', '3', '2', '1']},
    #                 {'label' : 'Computer', 'backgroundColor' : '#7D26CD', 'borderColor' : 'palette.transparent', 'data' : [
    #                 '5', '4', '3', '2', '1', '4', '5']}
    #     ]
    # }
    response =  make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response,200

@main.route('/user/monthly/linechart')
def get_monthly_linechart():
    data = {}
    data["labels"] = ["{h}:00".format(h=i) for i in range(1, 25)]
    data['datasets'] = []
    user = User.query.get(config.USER_ID)
    devices = user.devices.all()
    labels = ['Total']
    labels.extend([device.category_type for device in devices])

    for i in range(len(labels)):
        data['datasets'].append({'label': labels[i], 'backgroundColor': '#00FF00', 'borderColor': 'palette.transparent',
                                 'data': [str(random.randint(0, 20)) for i in range(len(data['labels']))]})
    response =  make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response,200

@main.route('/data/map')
def get_map():
    data = {
        'ViewX' : '58.404',
        'ViewY' : '15.598',
        'ViewScale' : '16',
        'MyposX' : '58.4042552',
        'MyposY' : '15.5989675',
        'MyInfo' : 'I am here',
        # 0:{'posX': '58.40425', 'posY': '15.59896', 'Rad': '12', 'FillOpcity': '0.4', 'FillColor': '#F00000',
        #      'Info': 'color:#F00000'},
        # 1:{'posX': '58.40436', 'posY': '15.59895', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F20000',
        #      'Info': 'color:#F20000'},
        # 2:{'posX': '58.40447', 'posY': '15.59893', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F40000',
        #      'Info': 'color:#F40000'},
        # 3:{'posX': '58.40424', 'posY': '15.59894', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F60000',
        #      'Info': 'color:#F60000'},
        # 4:{'posX': '58.40453', 'posY': '15.59894', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F80000',
        #      'Info': 'color:#F80000'},
        # 5:{'posX': '58.40410', 'posY': '15.59892', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#FA0000',
        #      'Info': 'color:#FA0000'},
        # 6:{'posX': '58.40481', 'posY': '15.59891', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#FC0000',
        #      'Info': 'color:#FC0000'}
    }
    for i in range(200):
        data[i] = {'posX': str(round(random.uniform(58.40,58.41),5)), 'posY':str(round(random.uniform(15.59,15.61),5)), 'Rad': str(random.randint(10,40)), 'FillOpcity': '0.4', 'FillColor': '#F00000',
             'Info': 'color:#F00000'}
    response = make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response, 200



@main.route('/user/daily/pipechart')
def get_daily_pipechart():
    user = User.query.get(config.DEVICE_ID)
    devices = user.devices.all()
    data = {}
    data["labels"] = [device.category_type for device in devices]
    data["datasets"] = {}
    backgroundColor = ['#FF0000', '#00FF00', '#C0FFEE', '#EEFF0C', '#ABCDEE','#BCDEEF', '#BEEFEE']
    data['datasets']['label'] = 'color'
    data['datasets']['backgroundColor'] = backgroundColor[:len(data["labels"])]
    data['datasets']['data'] = [random.randint(1,10) for x in range(len(data["labels"]))]
    # data = {
    #     'labels': ['Light', 'Computers', 'Television', 'Refrige', 'Air-Conditioner', 'Micro-wave', 'Fans'],
    #     'datasets': {
    #         'label': '颜色们',
    #         'backgroundColor': ['#FF0000', '#00FF00', '#C0FFEE', '#EEFF0C', '#ABCDEE',
    #                             '#BCDEEF', '#BEEFEE'],
    #         'data': ['0.4', '0.2', '3.1', '8', '5.8', '1.2', '2.0']
    #     }
    # }
    response = make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response, 200

@main.route('/user/monthly/pipechart')
def get_monthly_pipechart():
    user = User.query.get(config.USER_ID)
    devices = user.devices.all()
    data = {}
    data["labels"] = [device.category_type for device in devices]
    data["datasets"] = {}
    backgroundColor = ['#FF0000', '#00FF00', '#C0FFEE', '#EEFF0C', '#ABCDEE', '#BCDEEF', '#BEEFEE']
    data['datasets']['label'] = 'color'
    data['datasets']['backgroundColor'] = backgroundColor[:len(data["labels"])]
    data['datasets']['data'] = [random.randint(1, 10) for x in range(len(data["labels"]))]

    response = make_response(json2.dumps(data))
    response.headers["mimetype"] = 'application/json'
    return response, 200

#新建设备接口
@main.route('/devcie/add',methods=['POST'])
def add_device():
    data = request.get_json()
    print(data)
    device = Device(category_type=data["type"],
                    description=data['description'],
                    user_id=config.USER_ID,
                    begin_use_time=datetime.utcnow(),
                    status=1)
    count = Device.query.count() + 1
    device.name = data["name"]
    # device.name = 'smartplug_{id}_for_{category}'.format(id=count, category=device.category_type)
    db.session.add(device)
    db.session.commit()

    response = make_response(json2.dumps({"code":200}))
    response.headers["mimetype"] = 'application/json'
    return response, 200


#手机设备上传接口
@main.route('/upload', methods=['POST'])
def upload_device_info():
    data = request.get_json()
    device_info = Device_energy_info(
        device_id = data["device_id"],
        upload_time = datetime.utcnow(),
        month_energy = data["year_detail"]["month_list"][0]["energy"],
        day_energy = data["mon_detail"]["day_list"][0]['energy'],
        current_power = data["power_current"]["power"],
        year = data["time"]["year"],
        month = data["time"]["month"],
        mday = data["time"]["mday"],
        wday=data["time"]["wday"],
        hour = data["time"]["hour"],
        min = data["time"]["min"],
        sec = data["time"]["sec"]
    )
    db.session.add(device_info)

    #更新device的状态和当前功率和当前总耗电量
    if data["device_id"] is not None:

        device = Device.query.get(data["device_id"])
        #更新当前设备的功率
        device.power = data["power_current"]["power"]
        #计算设备总消耗/千瓦时
        device.total_energy_consumption += device.power*10/3600000
        db.session.add(device)
    db.session.commit()

    return jsonify({'code':200}),200

@main.route('/location', methods=['POST'])
def get_location():
    data = request.get_json()
    user = User.query.get(config.USER_ID)
    user.longitude = data["longitude"]
    user.latitude = data["latitude"]
    db.session.add(user)
    db.session.commit()
    return jsonify({'code':200})

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
