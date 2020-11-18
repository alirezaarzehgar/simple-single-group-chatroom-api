from .. .common import (db, reqparse,
                        Resource, jsonify,
                        make_response)

from .. .models.user import UserModel


parser = reqparse.RequestParser()

class Register(Resource):
    def post(self):
        try:
            parser.add_argument('username')
            parser.add_argument('password')
            parser.add_argument('first_name')
            parser.add_argument('last_name')
            parser.add_argument('profile')

            args = parser.parse_args()
            dose_exist = UserModel.query.filter_by(username=args['username']).first()

            if dose_exist:
                return make_response(jsonify(message='user already in use'), 409)

            new_user = UserModel(username=args['username'],
                                 password=args['password'],
                                 first_name=args['first_name'],
                                 last_name=args['last_name'],
                                 profile=args['profile'])
            db.session.add(new_user)
            db.session.commit()

            return make_response(jsonify(message='user created successfully'), 201)

        except:
            db.create_all()
            return make_response(jsonify(message="Internal server error mybe database problem"), 500)
