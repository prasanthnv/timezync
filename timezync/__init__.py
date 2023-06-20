from flask import Flask
from config import Config
from flask_marshmallow import Marshmallow
from timezync.database import db
from flask_migrate import Migrate
from timezync.routes import router


app = Flask(__name__)
app.config.from_object(Config)
# Initialize Flask extensions here
db.init_app(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
# Register blueprints here
# app.register_blueprint(user_bp)
router.register(app)



with app.app_context():
    db.create_all()

    # db.session.add(User('admin', 'admin@example.com'))
    # db.session.add(User('guest', 'guest@example.com'))
    # db.session.commit()

    # users = User.query.all()
    # print(users)
