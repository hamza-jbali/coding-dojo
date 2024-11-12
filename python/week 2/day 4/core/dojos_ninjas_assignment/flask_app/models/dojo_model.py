from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB 


class Dojo : 
    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL(DB).query_db(query)
        dojos_list=[]
        for row in results :
            dojos_list.append(cls(row)) 
        return dojos_list

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_dojo(cls,data ):
        query="INSERT INTO dojos (name) VALUES (%(name)s)"
        id = connectToMySQL(DB).query_db(query,data)
        return id 







