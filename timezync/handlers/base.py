from timezync.database import db
from timezync.models.user import User, user_schema, users_schema
from sqlalchemy.exc import IntegrityError

class BaseHandler:
    def __init__(self, model, schema):
        self.model = model
        self.schema = schema
    
    def create(self, data):
        try:
            new_object = self.model(**data)
            db.session.add(new_object)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Data already exists'}, 409