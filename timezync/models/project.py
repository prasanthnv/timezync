from timezync.database import db
from flask_marshmallow import Schema
class Project(db.Model):

    """
    This models stores metadata of files uploaded for Profiles
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    code = db.Column(db.String(225), unique=True, nullable=True)


   
    
class ProjectSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'code')

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)