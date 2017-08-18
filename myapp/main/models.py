from myapp import db
from datetime import datetime

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(30), nullable=False, unique=True)
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
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'), nullable=False)
    own_by_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    power = db.Column(db.Float, nullable=True)
    total_enery_consumption = db.Column(db.Float,nullable=True)
    begin_use_time = db.Column(db.DateTime, nullable=True)
    used_time = db.Column(db.DateTime, nullable =True)

    def __init__(self, category_id, own_by_user,):
        self.category_id = category_id
        self.own_by_user = own_by_user

    def __repr__(self):
        return '<Device %r, category %r>' % (self.id, self.category_id)

class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    info = db.Column(db.String(30), nullable=False)

    def __init__(self, info):
        self.info = info

    def __repr__(self):
        return '<User %r>' % self.info

