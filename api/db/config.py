from ..common import app
import os

dbname = 'test.db'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, dbname)
app.config['JWT_SECRET_KEY'] = 'secret'
