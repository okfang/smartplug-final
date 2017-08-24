from myapp import create_app
from flask import current_app
import config
from myapp import db
from myapp.main.models import Category



app = create_app('config')

app.run(debug=True)

