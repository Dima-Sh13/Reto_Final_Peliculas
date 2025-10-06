import requests as req
import sqlite3
from config import ORIGIN_DATA, API_KEY



class ConexionApi():
    def __init__(self,apikey):
        self.url= ""
        self.answer = None
        self.apiKey = apikey

    def search_by_name(self,name):
        self.url = f"http://www.omdbapi.com/?t={name}&plot=full&{self.apiKey}"
        self.answer = req.get(self.url)
        self.answer = self.answer.json()
        return self.answer
    def get_recent(self, name, year):
        self.url = f"http://www.omdbapi.com/?t={name}&y={year}&plot=full&{self.apiKey}"
        self.answer = req.get(self.url)
        self.answer = self.answer.json()
        return self.answer
                      


class ConexionBd():
    def __init__(self,querySql,params=[]):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql, params)
        