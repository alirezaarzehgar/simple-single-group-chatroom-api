import os


PATH_UPLOAD = os.path.abspath((os.path.dirname(__file__) + '/../static'))
PATH_PROFILE = PATH_UPLOAD + '/user/profile'

PATH_MESSAGE = PATH_UPLOAD + '/message'
PATH_AUDIO = PATH_MESSAGE + '/audio'
PATH_FILE = PATH_MESSAGE + '/file'
PATH_IMAGE = PATH_MESSAGE + '/image'
PATH_VIDEO = PATH_MESSAGE + '/video'

