from .. .common import jsonify, create_access_token
from .. .common import Resource, make_response
from .. .common import reqparse
from .. .models.user import UserModel


parser = reqparse.RequestParser()

class Login(Resource):
    def post(self):
        parser.add_argument('username')
        parser.add_argument('password')

        args = parser.parse_args()

        dose_exist = UserModel.query.filter_by(username=args['username'],
                                               password=args['password']).first()

        if dose_exist:
            access_token = create_access_token(identity=args['username'])
            return make_response(jsonify(message="login succeeded", access_token=access_token), 202)

        return make_response(jsonify(message="bad username or password"), 403)

