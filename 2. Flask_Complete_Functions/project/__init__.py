# Flask application instance

from flask import Flask
from project.config import Config

project = Flask(__name__)

from project.arts.routes import arts
from project.home.routes import home
from project.steg.routes import steg
from project.sleepwalk.routes import sleepwalk
from project.countletters.routes import countletters


project.register_blueprint(home)
project.register_blueprint(arts)
project.register_blueprint(steg)
project.register_blueprint(sleepwalk)
project.register_blueprint(countletters)
project.config.from_object(Config)


