from flask import Blueprint,render_template,request,flash,redirect
from flask_login import login_user,login_required,current_user,logout_user
from website.models import User
from website import db
from werkzeug.security import generate_password_hash,check_password_hash
from website.tokens import create_token,dec

auth = Blueprint('auth',__name__)

@auth.route('/',methods = ['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email1']
        password = request.form['password1']
        user = User.query.filter_by(email = email).first()
        if check_password_hash(user.password , password):
            login_user(user , remember = True)
            token = create_token({'email' : user.email})
            no_token = dec(token)
            return render_template('home.html', data = token , data1 = no_token)
    return render_template('login.html')


@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        new_user = User(email = email, password = generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
    return render_template('signup.html')

@auth.route('/home',methods = ['GET','POST'])
@login_required
def home():
    return render_template('home.html')

@auth.route('/logout',methods = ['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect('/logout')
