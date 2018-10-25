#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import blueprint
from ... import db
from app.auth.models import User


@blueprint.route('/login')
def login():
    user = User()
    # user.email = '12121'
    # user.username = 'codercat'
    # db.session.add(user)
    # db.session.commit()
    return "login"
