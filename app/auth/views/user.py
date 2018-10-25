#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import blueprint
from app.auth.models import user


@blueprint.route('/login')
def login():
    print(user.User)
    return 'login'
