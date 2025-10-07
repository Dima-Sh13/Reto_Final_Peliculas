from movies_app.conexion import *
import sqlite3

def insert_comment(registro):
    connectInsert = ConexionBd(f"INSERT INTO movies (id, comment) VALUES (?,?);", registro) # type: ignore
    connectInsert.con.commit()
    connectInsert.con.close()

def get_name(name):
    fName = []
    for i in name:
        if i == " ":
            i = "+"
        fName.append(i)
    fName = "".join(fName)

    return fName 
            
def insert(registroForm):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("INSERT INTO movies (id, comments, rating) VALUES (?,?,?);",registroForm)
    conexion.commit()#funcion para validar el registro antes de guardarlo

    conexion.close()   
    