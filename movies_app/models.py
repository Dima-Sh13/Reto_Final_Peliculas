from movies_app.conexion import *

def insert_comment(registro):
    connectInsert = ConexionBd(f"INSERT INTO movies (id, comment) VALUES (?,?);", registro) # type: ignore
    connectInsert.con.commit()
    connectInsert.con.close()