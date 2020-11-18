from .. .common import jwt_required, Resource
from .. .common import jsonify, make_response
from .. .common import get_jwt_identity, reqparse
from .. .models.user import UserModel, db
from .. .schema.user import users_schema


parser = reqparse.RequestParser()

class User(Resource):
    @jwt_required
    def get(self):
        parser.add_argument('id')

        args = parser.parse_args()
        user_id = args['id']
        current_user = UserModel.query.filter_by(ID=user_id)
        user = users_schema.dump(current_user)

        return jsonify(message=user)

    @jwt_required
    def delete(self):
        current_user = UserModel.query.filter_by(username=get_jwt_identity()).first()

        if current_user:
            db.session.delete(current_user)
            db.session.commit()

            return jsonify(message="deleted successfully")

        else:
            return make_response(jsonify(message="user dose not exists"), 402)

    @jwt_required
    def put(self):
        parser.add_argument('username')
        parser.add_argument('password')
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        parser.add_argument('profile')

        args = parser.parse_args()

        current_user = UserModel.query.filter_by(username=get_jwt_identity()).first()

        if current_user:
            if args['username'] != None:
                current_user.username = args['username']

            if args['password'] != None:
                current_user.password = args['password']

            if args['first_name'] != None:
                current_user.first_name = args['first_name']

            if args['last_name'] != None:
                current_user.last_name = args['last_name']

            if args['profile'] != None:
                current_user.profile = args['profile']

            db.session.merge(current_user)
            db.session.flush()
            db.session.commit()

            return make_response(jsonify(message='user info modyfied successfully'), 201)

        else:
            return make_response(jsonify(message='user dose not exists'), 404)

        return make_response(jsonify(message='user info modyfied successfully'), 201)
