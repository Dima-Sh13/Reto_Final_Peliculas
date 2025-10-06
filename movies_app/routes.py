from movies_app import app
from flask import jsonify, render_template, request, redirect
from movies_app.models import *
from config import *


@app.route("/", methods=["GET","POST"])
def index():
    api = ConexionApi(API_KEY)
    
    if request.method == "GET":
        return render_template("index.html")
    else:
        movieName = get_name(request.form["movieName"])
        
        return redirect(f"movie/{movieName}")
        
    

@app.route("/movie/<idn>", methods=["GET","POST"])
def detailde_view(idn):
    api = ConexionApi(API_KEY)
    details = api.search_by_name(idn)
    print(type(details["Poster"]))
    
    if request.method == "POST":
        return render_template("movie_view.html", data = details)
    else:
        return render_template("movie_view.html", data = details)    



