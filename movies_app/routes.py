from movies_app import app
from flask import jsonify, render_template, request, redirect
from movies_app.models import *
from config import *
from datetime import date

today = date.today()
today_str = fecha_str = today.strftime("%d-%m-%Y")


@app.route("/", methods=["GET","POST"])
def index():
    api = ConexionApi(API_KEY)
    rec =[]
    if request.method == "GET":
        #for i in ABC:
         #   rec.append(api.get_recent(i,"2025"))

            
        return render_template("index.html", recent = rec)
    else:
        if request.form["movieYear"] == "":
            movieName = get_name(request.form["movieName"])
        
            return redirect(f"movie/{movieName}")
        else:
            for i in ABC:
                rec.append(api.get_recent(i,request.form["movieYear"]))

            return render_template("index.html", recent = rec)    

    

@app.route("/movie/<idn>", methods=["GET","POST"])
def detailde_view(idn):
    api = ConexionApi(API_KEY)
    details = api.search_by_name(idn)
    
    
    bd = ConexionBd(f"SELECT * from comments where movie_id = '{details['imdbID']}'")
    listaBD = bd.res.fetchall()
    listaComments = []
    for i in listaBD:
            listaComments.append(i[2])
    
    
    
    if request.method == "POST":
        if request.form["rating"]== "":
            insert_comment([details['imdbID'],request.form["commentsInput"],request.form["commentsName"],today_str])
        
        else:
            insert_rating([request.form["movieID"], request.form["rating"]])
            print(request.form)
        
        return render_template("movie_view.html", data = details,  comments = listaComments)
    
    else:
        
        return render_template("movie_view.html", data = details, comments = listaComments)  


     



@app.route("/prueba/<id>")
def prueba(id):
    api = ConexionApi(API_KEY)
    details = api.search_by_id(id)
    return render_template("prueba.html", prueba= details['imdbID'])        
        
            
        




