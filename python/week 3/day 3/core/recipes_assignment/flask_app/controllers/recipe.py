from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User


@app.route('/recipes')
def get_all():
    if 'user_id' not in session :
        return redirect('/')
    user=User.get_one({'id':session['user_id']})
    recipes=Recipe.get_all()
    return render_template('recipes.html',user=user,recipes=recipes)



@app.route('/recipes/new')
def display():
    if 'user_id' not in session :
        return redirect('/')
    return render_template('new_recipe.html')


@app.route('/create/recipe',methods=['POST'])
def add_recipe() :
    if 'user_id' not in session :
        return redirect('/')
    if Recipe.validate_recipe(request.form):
        data={**request.form,'user_id': session['user_id']}
        recipe_id=Recipe.create_recipe(data)
        return redirect('/recipes')
    return redirect ('/recipes/new')



@app.route('/recipes/<int:id>')
def display_user(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe=Recipe.get_recipe_by_user({'id':id})
    user= User.get_one({'id':session['user_id']})
    return render_template('display_recipe.html',recipe=recipe,user=user)



@app.route('/recipe/edit/<int:id>')
def display_edit_page(id):
    if 'user_id' not in session :
        return redirect('/')
    recipe = Recipe.get_recipe_by_id({'id': id})
    print(recipe)
    return render_template('edit_recipe.html',recipe=recipe)



# @app.route('/edit/recipe')


@app.route('/recipe/delete/<int:id>')
def delete(id):
    Recipe.delete({'id': id})
    return redirect('/recipes')


@app.route('/edit/recipe/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session :
        return redirect('/')
    if Recipe.validate_recipe(request.form):
        updated_recipe = {
            'id':id,
            'name': request.form['name'],  
            'description':request.form['description'],
            'instructions': request.form['instructions'], 
            'date_made':request.form['date_made'],
            'under_30_min':request.form['under_30_min']
        }
        Recipe.update(updated_recipe) 
        return redirect('/recipes')
    return redirect('/recipe/edit/<int:id>')