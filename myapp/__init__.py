from flask import Flask
from werkzeug.utils import import_string

blueprints = [
    'myapp.main:main',
    'myapp.admin:admin'
]

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    #load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app



from myapp.main import views
