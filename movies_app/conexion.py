from requests import request
import sqlite3
from config import ORIGIN_DATA



class ConexionApi():
    pass


class ConexionBd():
    def __init__(self,querySql,params=[]):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql, params)
        