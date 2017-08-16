from myapp.main import main

@main.route('/')
def index():
    return "main index"
