from ..common import jsonify, Resource

class Home(Resource):
    def get(self):
        return jsonify(message='hello world')

