from werkzeug.utils import secure_filename
from sqlalchemy import sql
from datetime import datetime
import os

from ..common import Resource, jwt_required
from ..common import jsonify, make_response
from ..common import reqparse, request
from ..common import get_jwt_identity
from ..common import db
from ..common.path import PATH_AUDIO, PATH_FILE, PATH_IMAGE, PATH_VIDEO

from ..models.message import MessageModel
from ..models.user import UserModel
from ..schema.message import MessageSchema
from ..schema.message import messages_schema


parser = reqparse.RequestParser()

class Message(Resource):

    @jwt_required
    def post(self):
        parser.add_argument('text')
        parser.add_argument('file_type')
        parser.add_argument('file_name')

        args = parser.parse_args()

        text = args['text']
        file_name = ''
        file_type = ''

        user = UserModel.query.filter_by(username=get_jwt_identity()).first()
        user_id = user.ID

        if args['file_type'] == 'audio' and args['file_name'] in os.listdir(PATH_AUDIO):
            file_name = args['file_name']
            file_type = args['file_type']

        elif args['file_type'] == 'video' and args['file_name'] in os.listdir(PATH_VIDEO):
            file_name = args['file_name']
            file_type = args['file_type']

        elif args['file_type'] == 'image' and args['file_name'] in os.listdir(PATH_IMAGE):
            file_name = args['file_name']
            file_type = args['file_type']
            
        elif args['file_type'] == 'file' and args['file_name'] in os.listdir(PATH_FILE):
            file_name = args['file_name']
            file_type = args['file_type']

        elif args['file_type'] == None or args['file_name'] == None:
            return make_response(jsonify(message="your file or format not found"), 404)

        elif len(args['file_type']) > 1:
            return make_response(jsonify(message="invalid type or name"), 404)

        else:
            file_name = sql.null()
            file_type = sql.null()

        new_message = MessageModel(user_id=user_id,
                                   text=text,
                                   file_name=file_name,
                                   file_type=file_type,
                                   time=datetime.now().strftime('%H:%M'))
        try:
            db.session.add(new_message)
            db.session.commit()
            return jsonify(message="message sent successfully")

        except Exception as err:
            return make_response(jsonify(message="cannot send message"), 404)

    @jwt_required
    def get(self):
        get_query = MessageModel.query.all()
        messages = messages_schema.dump(get_query)

        return jsonify(message=messages)

