from datetime import datetime
from flask import flash,redirect,url_for,render_template,session,request,jsonify,make_response
from flask_login import login_required, login_user, logout_user
from myapp.forms import RegistrationForm, LoginForm
from myapp import db
from myapp.models import User
from myapp.main import main


#注册
@main.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    #
    # if User.query.filter_by(email=request.form['email']).count()==0:
    #     user = User(
    #         email=request.form["email"],
    #         username=request.form["username"],
    #         password=request.form["password"],
    #         register_time=datetime.utcnow()
    #     )
    #     db.session.add(user)
    #     db.session.commit()
    #     return redirect(url_for('auth.login'))
    # else:
    #     return jsonify({'error':'email already been use!'})

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
            register_time=datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('main.login'))
    return render_template('auth/register.html',form=form)


#简单登录
@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # user = User.query.filter_by(email=request.form['email']).first()
    # if user is not None and user.verify_password(request.form['password']):
    #     session["user_id"] = user.id
    #     return redirect(url_for('main.home'))
    # return jsonify({'error':'Invalid username or password'})


    # return render_template('index.html', form=form)
    #
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # g是全局本地变量
            session["user_id"] = user.id
            response = make_response(redirect(url_for('main.home')))
            #设置cookie
            response.set_cookie('user_id',str(user.id))
            response.set_cookie('user_name',user.username)
            return response
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

#简单退出
@main.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))