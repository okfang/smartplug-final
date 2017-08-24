from flask import Flask, g
from werkzeug.utils import import_string
from flask_sqlalchemy import SQLAlchemy
from myapp.main.models import Category

blueprints = [
    'myapp.main:main',
    'myapp.admin:admin'
]

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    #load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        # 获取所有设备类型
        category_set = Category.query.all()
        for category in category_set:
            print("get category: ",category.type)
            g.category_set[category.type] = category.id

    return app



from myapp.main import views
