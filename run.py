from myapp import create_app, db
from flask_script import Manager, Shell

app = create_app('config')

manager = Manager(app)

def make_shell_context():
    return dict(app = app, db = db)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    ''' Run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)
    # manager.run(commands='runserver')
