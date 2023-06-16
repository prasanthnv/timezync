from timezync.database import db

class User(db.Model):
    """
    This models stores metadata of files uploaded for Profiles
    """
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))

    def __repr__(self):
        return f'<Post "{self.title}">'