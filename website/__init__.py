from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user
import os


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdhfjsdgfhjgsdffshfkj'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    
    from website import auth
    from website import models

    app.register_blueprint(auth.auth,prefix='/')
    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

def create_db(app):
    path = 'database/users.db'
    if not os.path.exists(path):
        db.create_all(app=app)

