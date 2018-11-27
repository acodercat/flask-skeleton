#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

view_blueprint = Blueprint('view_blueprint', __name__)

from . import user