from datetime import datetime
from flask import flash,redirect,url_for,render_template,session
from flask_login import login_required, login_user, logout_user
from myapp.forms import RegistrationForm, LoginForm
from myapp.auth import auth
from myapp import db
from myapp.models import User


#注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    register_time=datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)


#简单登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # g是全局本地变量
            session["user_id"] = user.id
            return redirect(url_for('main.home'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

#简单退出
@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    del session['user_id']
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))