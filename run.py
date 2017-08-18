from myapp import create_app
from flask import current_app
import config
from myapp import db

app = create_app('config')

# with app.app_context():
#     db.create_all()

app.run(debug=True)

