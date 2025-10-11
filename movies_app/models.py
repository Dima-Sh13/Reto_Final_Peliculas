from movies_app.conexion import *
import sqlite3
import datetime


def get_name(name):
    fName = []
    for i in name:
        if i == " ":
            i = "+"
        fName.append(i)
    fName = "".join(fName)

    return fName 
            
def insert_comment(registroForm):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    
    res = cur.execute(f"INSERT INTO comments (movie_id, comment, user, date) VALUES ('{registroForm[0]}', '{registroForm[1]}', '{registroForm[2]}', '{registroForm[3]}')")
   
    conexion.commit()

    conexion.close()   

   
def insert_rating(registroForm):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    
    res = cur.execute(f"INSERT INTO ratings (movie_id, rating) VALUES ('{registroForm[0]}', '{registroForm[1]}')")
   
    conexion.commit()

    conexion.close()    
      