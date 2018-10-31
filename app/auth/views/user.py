#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import auth_blueprint
from ... import db
from flask import abort, current_app, jsonify
from app.auth.models import User


@auth_blueprint.route('/token')
def login():
    user = User()
    current_app.logger.debug('1111111111')
    # abort(403)
    # user.email = '12121'
    # user.username = 'codercat'
    # db.session.add(user)
    # db.session.commit()
    return jsonify({'a': 1})
