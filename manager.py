#!/usr/bin/env python3

from app import app, db, manager
from app.auth.models import User, Role
from flask_script import Shell

def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)

manager.add_command("shell", Shell(make_context = make_shell_context))

if __name__ == '__main__':
    manager.run()
