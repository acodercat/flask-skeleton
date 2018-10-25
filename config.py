#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://codercat:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True



config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}