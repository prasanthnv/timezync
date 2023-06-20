from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from timezync.handlers.user import UserHandler, UserInstanceHandler

rest_bp = Blueprint('main', __name__)
api = Api(rest_bp)

api.add_resource(UserHandler, '/user')
api.add_resource(UserInstanceHandler, '/user/<int:user_id>')
