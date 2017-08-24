from myapp import db
from datetime import datetime

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    register_time = db.Column(db.DateTime, nullable=True)
    total_enery_consumption = db.Column(db.Float, nullable=True)
    devices = db.relationship('Device',backref='user',lazy='dynamic')

    def __init__(self, user_id, password,):
        self.user_id = user_id
        self.password = password
        self.register_time =  datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.user_id

class Device(db.Model):
    __tablename__='device'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(50), nullable=True)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    power = db.Column(db.Float, nullable=True)
    total_energy_consumption = db.Column(db.Float,nullable=True)
    begin_use_time = db.Column(db.DateTime, nullable=True)
    used_time = db.Column(db.DateTime, nullable =True)
    device_energy_info_list = db.relationship('Device_energy_info', backref='device', lazy='dynamic')


    def __init__(self, category_id, user_id,decription):
        self.category_id = category_id
        self.user_id = user_id
        self.description = decription

    def __repr__(self):
        return '<Device %r, category %r, own_by_user %r>' % (self.id, self.category_id, self.user_id)


class Device_energy_info(db.Model):
    __tablename__ = "device_energy_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'),  nullable=False)
    collect_time = db.Column(db.DateTime, nullable=False)
    total_energy_consumption = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)

    def __init__(self,device_id, collect_time, total_energy_consumption, power):
        self.device_id = device_id
        self.collect_time = collect_time
        self.total_energy_consumption = total_energy_consumption
        self.power = power


class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    devices = db.relationship('Device', backref='category', lazy='dynamic')

    def __init__(self,id, type):
        self.id = id
        self.type = type

    def __repr__(self):
        return '<Category %r>' % self.type

