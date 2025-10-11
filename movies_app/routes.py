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
            #movieName = get_name(request.form["movieName"])
            movieName = api.get_name(request.form["movieName"])
            return redirect(f"movie/name/{movieName}")
        else:
            movieYear = int(request.form["movieYear"])
            if movieYear < 1920 or movieYear > 2025:
                movieYear = 2025
            for i in ABC:
                rec.append(api.get_recent(i,str(movieYear)))

    return render_template("index.html", recent = rec)    

    

@app.route("/movie/name/<idn>", methods=["GET","POST"])
def detailde_view(idn):
    api = ConexionApi(API_KEY)
    details = api.search_by_name(idn)
    
    try:
        bd = ConexionBd(f"SELECT * from comments where movie_id = '{details['imdbID']}'")
        listaBD = bd.res.fetchall()
        listaComments = []
        for i in listaBD:
            listaComments.append([i[2],i[3],i[4]])
    except Exception as e:
        return render_template("error.html")
        #listaComments= [["Hmmm.Something went wrong. Try again pls"]]
    
    
    
    
    if request.method == "POST":
        if request.form["rating"]== "":
            bd.insert_comment([details['imdbID'],request.form["commentsInput"],request.form["commentsName"],today_str])
            return redirect(f"/movie/name/{idn}")
        
        else:
            bd.insert_rating([request.form["movieID"], request.form["rating"]])
            return redirect(f"/movie/name/{idn}")
        
        return render_template("movie_view.html", data = details,  comments = listaComments)
    
    else:
        
        return render_template("movie_view.html", data = details, comments = listaComments)  


     



@app.route("/movie/id/<idn>")
def prueba(idn):
    api = ConexionApi(API_KEY)
    details = api.search_by_id(idn)
    bd = ConexionBd(f"SELECT * from comments where movie_id = '{details['imdbID']}'")
    listaBD = bd.res.fetchall()
    listaComments = []
    for i in listaBD:
            listaComments.append([i[2],i[3],i[4]])
    
    
    
    if request.method == "POST":
        if request.form["rating"]== "":
            bd.insert_comment([details['imdbID'],request.form["commentsInput"],request.form["commentsName"],today_str])
            return redirect(f"/movie/name/{idn}")
        else:
            bd.insert_rating([request.form["movieID"], request.form["rating"]])
            return redirect(f"/movie/name/{idn}")
        
        return render_template("movie_view.html", data = details,  comments = listaComments)
    
    else:
        
        return render_template("movie_view.html", data = details, comments = listaComments)        
        
            
        




