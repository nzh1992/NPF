# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/11/4
Last Modified: 2022/11/4
Description: 
"""
import os
import configparser
from datetime import timedelta

from app.utils.path import PathUtil


class Config:
    # 配置文件路径
    sys_config_fp = os.path.join(PathUtil.get_project_root_path(), 'sys_config.ini')

    # 从sys_config.ini加载配置项
    configuration = configparser.ConfigParser()
    configuration.read(sys_config_fp)

    HOST = configuration['BaseConfig']['host']
    DEBUG = configuration['BaseConfig']['debug']
    PORT = configuration['BaseConfig']['port']

    # SQLAlchemy
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ENCODING = "utf8mb4"
    EXPLAIN_TEMPLATE_LOADING = False

    # JWT-extended
    JWT_SECRET_KEY = configuration['JWT']['jwt_secret_key']
    # flask-jwt-extended需要datetime.timedelta类型，在此处转换
    JWT_ACCESS_TOKEN_EXPIRES_SECONDS = int(configuration['JWT']['jwt_access_token_expires'])
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=JWT_ACCESS_TOKEN_EXPIRES_SECONDS)
    JWT_TOKEN_LOCATION = configuration['JWT']['jwt_token_location']
    JWT_JSON_KEY = configuration['JWT']['jwt_json_key']
    JWT_REFRESH_JSON_KEY = configuration['JWT']['jwt_refresh_json_key']


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Nzh199266!@localhost/NPF?charset=utf8mb4'


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''


config_mapping = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig
}
