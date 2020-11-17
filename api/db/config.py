from ..common import app
import os

dbname = 'chat.db'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, dbname)
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['PROPAGATE_EXCEPTIONS'] = True
