import os
# import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# @manager.command
# def test():
#     """Runs the unit tests without coverage."""
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
