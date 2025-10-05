from movies_app import app
from flask import jsonify, render_template, request
from movies_app.models import *
from config import *


@app.route("/", methods=["GET","POST"])
def index():
    api = ConexionApi(API_KEY)
    datos = api.search_by_name()
    if request.method == "GET":
        return render_template("Index.html")
  
    return render_template("index.html", data= datos)