from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
class Ninja :
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.dojo_id=data['dojo_id']



    @classmethod
    def get_all(cls):
        query="SELECT * FROM ninjas ;"
        results=connectToMySQL(DB).query_db(query)
        ninjas_list=[]
        for row in results :
            dojos_list.append(cls(row)) 
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_ninja(cls,data ):
        query="INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        id = connectToMySQL(DB).query_db(query,data)
        return id 

