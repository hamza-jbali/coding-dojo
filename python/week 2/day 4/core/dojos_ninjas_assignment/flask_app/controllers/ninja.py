from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojos_ninjas_model import Ninja 



@app.route('/ninjas')
def display():
    return render_template('ninjas.html')


@app.route('/create_ninjas',methods=['POST'])
def ninjas_creation() :
    Ninja.create_ninja(request.form)
    return redirect('/ninjas')


@app.route('/dojos/<int:id>') 
def display_ninjas() :
    all_ninjas=Ninjas.get_all()
    return render_template('ninjas.html',all_ninjas=all_ninjas)