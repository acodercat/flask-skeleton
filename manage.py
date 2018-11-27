                    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app, db
from flask_migrate import Migrate, upgrade
import os


app = create_app(os.getenv('FLASK_ENV') or 'default')
migrate = Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
#     return dict()
