from timezync.database import db
from flask_marshmallow import Schema
class User(db.Model):

    """
    This models stores metadata of files uploaded for Profiles
    """
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(10), unique=True, nullable=False, default='')
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __repr__(self):
        return f'<Post "{self.name}">'
    
class UserSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'employee_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)