from flask import Blueprint

bp = Blueprint('main', __name__)

from timezync.main import routes