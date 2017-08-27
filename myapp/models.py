from flask_login import UserMixin
from myapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from myapp import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask import current_app

#用户
class User(UserMixin,db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True,index=True)
    username = db.Column(db.String(64), nullable=False,index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False)
    total_enery_consumption = db.Column(db.Float, nullable=True)
    region = db.Column(db.String(64), nullable=True)
    location = db.Column(db.String(64), nullable=True)
    devices = db.relationship('Device',backref='user',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self,expiration = 600):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verifg_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token but expired
        except BadSignature:
            return None
        user = User.query.get[data['id']]
        return user


    # def __init__(self, user_id, password,):
    #     self.user_id = user_id
    #     self.password = password
    #     self.register_time =  datetime.utcnow()


#flask_login 回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#设备
class Device(db.Model):
    __tablename__='device'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(50), nullable=True)
    category_type = db.Column(db.String(30),db.ForeignKey('category.type'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    power = db.Column(db.Float, nullable=True)
    total_energy_consumption = db.Column(db.Float,nullable=True)
    begin_use_time = db.Column(db.DateTime, nullable=True)
    used_time = db.Column(db.DateTime, nullable =True)
    device_energy_info_list = db.relationship('Device_energy_info', backref='device', lazy='dynamic')


    # def __init__(self, category_id, user_id,decription):
    #     self.category_id = category_id
    #     self.user_id = user_id
    #     self.description = decription

#设备提交上传信息
class Device_energy_info(db.Model):
    __tablename__ = "device_energy_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'),  nullable=False)
    collect_time = db.Column(db.DateTime, nullable=False)
    total_energy_consumption = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)

    # def __init__(self,device_id, collect_time, total_energy_consumption, power):
    #     self.device_id = device_id
    #     self.collect_time = collect_time
    #     self.total_energy_consumption = total_energy_consumption
    #     self.power = power


#设备类型
class Category(db.Model):
    __tablename__='category'
    type = db.Column(db.String(30),unique=True, primary_key=True,nullable=False)
    devices = db.relationship('Device', backref='category', lazy='dynamic')

    # def __init__(self,id, type):
    #     self.id = id
    #     self.type = type

