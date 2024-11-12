from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/registration',methods=['POST'])
def registration():
    if User.validate_user(request.form):
        pw_hash=bcrypt.generate_password_hash(request.form['password'])
        data={**request.form,'password':pw_hash}
        user_id=User.create_user(data)
        session['user_id']=user_id
        return redirect ('/recipes')
    return redirect ('/')

@app.route('/login',methods=['POST'])
def login():
    data={'email':request.form['email']}
    user_in_db=User.get_by_email(data)
    if not user_in_db :
        flash("User not found",'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']) :
        flash("User not found",'login')
        return redirect('/')
    session['user_id']=user_in_db.id
    return redirect('/recipes')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
