from flask import request
from flask_restful import Resource
from timezync.database import db
from timezync.utils.decoratos import catch_db_exceptions
from timezync.models.user import User, user_schema, users_schema
from sqlalchemy.exc import IntegrityError
from timezync.handlers.base import BaseHandler

class UserHandler(Resource):
    def __init__(self):
        BaseHandler.__init__(self, User, user_schema)

    @catch_db_exceptions
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)
    
    @catch_db_exceptions
    def post(self):
        user_data = request.get_json()

        new_user = User(name=user_data['name'], email=user_data['email'], employee_id=user_data['employee_id'], password=user_data['password'])
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)
        # return self.create(user_data)
        
        
class UserInstanceHandler(Resource):
    @catch_db_exceptions
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)
        