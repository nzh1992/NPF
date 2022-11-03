# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/11/4
Last Modified: 2022/11/4
Description: 
"""
from flask_restx import Api


api = Api(
    title='NPF API',
    version='1.0',
    security='Bearer Auth',
    authorizations={
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a jwt with ** Bearer token"
        }
    }
)