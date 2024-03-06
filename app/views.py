from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
import os

bp = Blueprint("app", __name__, template_folder="templates")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["image"]
        filename = secure_filename(f.filename)
        f.save(os.path.join("app/static/img", filename))
        return "File uploaded successfully"


@bp.route("/thumbnails")
def thumbnails():
    images = os.listdir("app/static/img")
    return render_template("thumbnails.html", images=images)
