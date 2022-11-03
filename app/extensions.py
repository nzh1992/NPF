# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/11/4
Last Modified: 2022/11/4
Description: flask扩展
"""
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()