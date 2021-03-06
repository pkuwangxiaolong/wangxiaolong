#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Evan
# @Date:   2016-01-10 10:53:47
# @Last Modified by:   Evan
# @Last Modified time: 2016-01-11 21:16:27

import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()