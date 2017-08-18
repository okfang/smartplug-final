from myapp import create_app
from flask import current_app
import config
from myapp import db
from myapp.main.models import Category

category_set={'Aircondition':1, 'light':2, 'television':3,'computer':4,'other':5}

app = create_app('config')

with app.app_context():
    db.create_all()
    for key in category_set:
        print("key:"+key+" value:",category_set[key])
        db.session.add(Category(category_set[key], key))
    db.session.commit()

app.run(debug=True)

