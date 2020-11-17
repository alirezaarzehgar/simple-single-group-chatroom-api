from api.common import app, main_api
import api.cli.commands
import api.db.config

# database config
import api.models.user
import api.models.message

# routes
from api.route.user.register import Register
from api.route.user.login import Login
from api.route.user.user import User
from api.route.upload import Upload
from api.route.download import Download
from api.route.message import Message

# add resources
main_api.add_resource(Register, '/api/register')
main_api.add_resource(Login, '/api/login')
main_api.add_resource(User, '/api/user')
main_api.add_resource(Upload, '/api/upload')
main_api.add_resource(Download, '/api/download')
main_api.add_resource(Message, '/api/message')


if __name__ == '__main__':
    app.run()

