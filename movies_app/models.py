from movies_app.conexion import *

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
            
    