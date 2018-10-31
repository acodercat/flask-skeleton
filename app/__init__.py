#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # db.create_all()

    from app.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app