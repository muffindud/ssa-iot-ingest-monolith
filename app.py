from os import environ
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from routes.iot.auth import iot_auth_bp
from routes.iot.ingest import iot_ingest_bp
from routes.user.auth import user_auth_bp
from routes.user.access import user_access_bp


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)

app.register_blueprint(iot_auth_bp, url_prefix='/iot/auth')
app.register_blueprint(iot_ingest_bp, url_prefix='/iot/ingest')
app.register_blueprint(user_access_bp, url_prefix='/user/access')
app.register_blueprint(user_auth_bp, url_prefix='/user/auth')
