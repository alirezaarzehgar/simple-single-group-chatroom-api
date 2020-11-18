from flask import (Flask, jsonify,
                   request, make_response)

from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import (create_access_token, JWTManager,
                                jwt_required, get_jwt_identity)


app = Flask(__name__)
main_api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
