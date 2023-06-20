from flask import request
from flask_restful import Resource
from timezync.database import db

from timezync.handlers.base import BaseHandler
from timezync.models.user import User

class UserHandler(Resource, BaseHandler):
    model = User
