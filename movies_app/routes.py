from movies_app import app
from flask import jsonify, render_template, request
from movies_app.models import *
from config import *


@app.route("/")
def index():
    return render_template("index.html")