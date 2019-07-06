# app/__init__.py

import os
from flask import Flask, request, render_template, session,g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Creating instances for the extensions we're using
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()




def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app) # bind database to flask app
    bootstrap.init_app(app) # intialize bootstrap
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main # import blueprint
    app.register_blueprint(main) # register blueprint

    from app.auth import authentication # import blueprint
    app.register_blueprint(authentication) # register blueprint



    return app
