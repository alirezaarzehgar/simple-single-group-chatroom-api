import os
from werkzeug.utils import secure_filename

from ..common import jwt_required, request
from ..common import Resource, jsonify
from ..common import make_response
from ..common.path import PATH_AUDIO, PATH_FILE, PATH_IMAGE, PATH_MESSAGE, PATH_PROFILE, PATH_VIDEO
from ..common.file_format import IMAGE, VIDEO, AUDIO


class Upload(Resource):
    def post(self):
        file_type = request.form['type']

        if 'file' in request.files:
            file_path = request.files['file']
            filename = secure_filename(file_path.filename)

            if file_type == 'profile':
                final_path = os.path.join(PATH_PROFILE, filename)

            elif file_type == 'image' and filename.split(".")[-1] in IMAGE:
                final_path = os.path.join(PATH_IMAGE, filename)

            elif  file_type == 'video' and filename.split(".")[-1] in VIDEO:
                final_path = os.path.join(PATH_VIDEO, filename)

            elif file_type == 'audio' and filename.split(".")[-1] in AUDIO:
                final_path = os.path.join(PATH_AUDIO, filename)

            else:
                final_path = os.path.join(PATH_FILE, filename)

            file_path.save(final_path)

            return jsonify(message="uploaded file successfully")

        else:
            return make_response(jsonify(message="missing file"), 404)

