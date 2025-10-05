from movies_app import app
from flask import jsonify, render_template, request, redirect
from movies_app.models import *
from config import *


@app.route("/", methods=["GET","POST"])
def index():
    
    
    if request.method == "GET":
        return render_template("Index.html")
    else:
        movieName = get_name(request.form["movieName"])
        
        return redirect(f"/movie/{movieName}")
        
    

@app.route("/movie/<idn>")
def detailde_view(idn):
    api = ConexionApi(API_KEY)
    details = api.search_by_name(idn)

    return render_template("movie_view.html", data = details)
        



