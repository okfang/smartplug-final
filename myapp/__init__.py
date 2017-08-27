from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

blueprints = [
    'myapp.main:main',
    'myapp.auth:auth'
]

category_set = ["Light", "Television","air conditioning","Fridge","Computer","Fan"]

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    #load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    #flask拓展
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        db.create_all()
        #输入设备类别
        from myapp.models import Category

        if Category.query.first() is None:
            for x in category_set:
                db.session.add(Category(type=x))
            db.session.commit()
    #     category_set = Category.query.all()
    #     for category in category_set:
    #         print("get category: ",category.type)
    #         g.category_set[category.type] = category.id

    return app



from myapp.main import views
