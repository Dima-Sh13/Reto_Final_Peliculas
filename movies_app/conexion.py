import requests as req
import sqlite3
from config import ORIGIN_DATA, API_KEY



class ConexionApi():
    def __init__(self,apikey):
        self.url= ""
        self.answer = None
        self.apiKey = apikey

    def get_name(self, name):
        fName = []
        for i in name:
            if i == " ":
                i = "+"
            fName.append(i)
        fName = "".join(fName)

        return fName

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
    def search_by_year(self,name,year):
        self.url = f"http://www.omdbapi.com/?t={name}&y={year}&plot=full&{self.apiKey}" 
        self.answer = req.get(self.url)
        self.answer = self.answer.json()
        return self.answer                
    def search_by_id(self,id):
        self.url = f"http://www.omdbapi.com/?i={id}&plot=full&{self.apiKey}"
        self.answer = req.get(self.url)
        self.answer = self.answer.json()
        return self.answer    


class ConexionBd():
    def __init__(self,querySql,params=[]):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql, params)

    def insert_comment(self, registroForm):
        self.res = self.cur.execute(f"INSERT INTO comments (movie_id, comment, user, date) VALUES ('{registroForm[0]}', '{registroForm[1]}', '{registroForm[2]}', '{registroForm[3]}')")
        self.con.commit()
        self.con.close()    
        
    def insert_rating(self, registroForm):
        self.res = self.cur.execute(f"INSERT INTO ratings (movie_id, rating) VALUES ('{registroForm[0]}', '{registroForm[1]}')")
        self.con.commit()
        self.con.close()
        
       
    
    
