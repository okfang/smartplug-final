from flask import Blueprint
main = Blueprint('main', __name__,template_folder='templates',static_folder='static')
from myapp.main import page
from myapp.main import api