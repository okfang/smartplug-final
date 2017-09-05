from myapp import create_app

app = create_app('config')

if __name__ == '__main__':
    # manager.run()
    app.run(host='0.0.0.0',debug=True)
    # manager.run(commands='runserver')
