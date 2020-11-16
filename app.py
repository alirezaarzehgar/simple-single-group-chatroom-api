from api.common import app, main_api
import api.cli.commands
import api.db.config

# routes
from api.route.home import Home


# add resources
main_api.add_resource(Home, '/api')


if __name__ == '__main__':
    app.run()

