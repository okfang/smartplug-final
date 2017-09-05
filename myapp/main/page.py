from flask import render_template
from myapp.main import main


###############   All Page  post form   ###########################

#主页
@main.route('/')
def index():
    return render_template('index.html')

