from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from flask_cors import CORS
blueprints = [
    'myapp.main:main'
]

category_set = ["First option", "Second option","Third option"]

db = SQLAlchemy()

bootstrap = Bootstrap()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, supports_credentials=True)

    #load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    #flask拓展
    db.init_app(app)

    with app.app_context():
        db.create_all()
        #输入设备类别
        from myapp.models import Category
        if Category.query.first() is None:
            for x in category_set:
                db.session.add(Category(type=x))
            db.session.commit()

    return app
