from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models.db import db  # ✅ only import db from db.py
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

from server.config import SQLALCHEMY_DATABASE_URI, SECRET_KEY, JWT_SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    # Register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.appearance_controller import appearance_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production