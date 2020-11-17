from ..common import jsonify, make_response
from ..common import jwt_required
from ..common import Resource, request
from ..common.path import PATH_PROFILE, PATH_AUDIO, PATH_FILE, PATH_IMAGE, PATH_MESSAGE, PATH_VIDEO
from ..common.file_format import AUDIO, IMAGE, VIDEO

from flask import send_from_directory
import os


class Download(Resource):

    @jwt_required
    def get(self):
        file_type = request.form['type']
        file_name = request.form['name']

        if file_type == "profile" and file_name in os.listdir(PATH_PROFILE):
            return send_from_directory(PATH_PROFILE, file_name)

        elif file_name.split(".")[-1] in AUDIO and file_name in os.listdir(PATH_AUDIO):
            return send_from_directory(PATH_AUDIO, file_name)

        elif file_name.split(".")[-1] in IMAGE and file_name in os.listdir(PATH_IMAGE):
            return send_from_directory(PATH_IMAGE, file_name)

        elif file_name.split(".")[-1] in VIDEO and file_name in os.listdir(PATH_VIDEO):
            return send_from_directory(PATH_VIDEO, file_name)

        elif file_name in os.listdir(PATH_FILE):
            return send_from_directory(PATH_FILE, file_name)

        return jsonify(message="your file not found")
