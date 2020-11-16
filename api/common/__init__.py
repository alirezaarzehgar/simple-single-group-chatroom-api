from flask import Flask, jsonify, request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
main_api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

