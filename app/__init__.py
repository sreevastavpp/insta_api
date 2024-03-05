from flask import Flask
from app.views import bp

app = Flask(__name__)
# app.register_blueprint(bp)

app.register_blueprint(bp, url_prefix="/")
app.config["TEMPLATES_AUTO_RELOAD"] = True