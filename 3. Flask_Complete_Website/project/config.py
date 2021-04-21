
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Set the upload folder as the static folder in app directory
    UPLOAD__IMAGE_FOLDER = 'project/steg/images'
    UPLOAD__TEXT_FOLDER = 'project/countletters/textfiles'