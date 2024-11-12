from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash



class Recipe :
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date_made=data['date_made']
        self.under_30_min=data['under_30_min']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.poster=""

    @classmethod
    def get_all(cls):
        query="SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"
        results= connectToMySQL(DB).query_db(query)
        recipes=[]
        for row in results :
            recipe = cls(row)
            recipe.poster=f"{row['first_name']}"
            recipes.append(recipe)
        return recipes


    @classmethod
    def create_recipe(cls,data):
        query="INSERT INTO recipes (name,description,instructions,date_made,under_30_min,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30_min)s,%(user_id)s);"
        result=connectToMySQL(DB).query_db(query,data)
        return result



    @classmethod
    def get_recipe_by_user(cls,data):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id=users.id WHERE recipes.id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        user=cls(results[0])
        user.poster=results[0]['first_name']+" "+results[0]['last_name']
        return user


    @classmethod
    def get_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        recipe = Recipe(results[0])
        return recipe


    @staticmethod
    def validate_recipe( data ):
        is_valid = True
        if len(data['name'])< 3 :
            is_valid=False
            flash("name must contain at least 3 chracaters","name_validation")
        if len(data['description'])<3:
            is_valid=False
            flash("location must contain at least 3 chracaters","description_validation")
        if len(data['instructions'])<3:
            id_valid=False
            flash("Instructions must contain at least 3 characters","instructions_validation")
        return is_valid


    @classmethod
    def update(clas,data) :
        query="UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under_30_min=%(under_30_min)s WHERE  id=%(id)s ; "
        return connectToMySQL(DB).query_db(query,data)



    @classmethod
    def delete(clas,data) :
        query="DELETE FROM recipes WHERE id=%(id)s ;"
        return  connectToMySQL(DB).query_db(query,data)