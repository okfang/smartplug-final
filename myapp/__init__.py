from flask import Flask
from werkzeug.utils import import_string
from flask_sqlalchemy import SQLAlchemy

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

    return app



from myapp.main import views
