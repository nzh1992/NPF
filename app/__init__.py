# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/11/4
Last Modified: 2022/11/4
Description: 
"""
import os

from flask import Flask

from app.settings import config_mapping
from app.extensions import db, jwt, migrate
from app.api import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_mapping['development'])

    # 注册服务
    register_extensions(app)
    register_api(app)

    return app


def register_api(app):
    """注册API"""
    api.init_app(app)


def register_extensions(app):
    """注册flask-扩展"""
    # flask-sqlalchemy
    db.init_app(app)

    # flask-jwt-extended
    jwt.init_app(app)

    # flask-migrate
    migrate.init_app(app, db)
