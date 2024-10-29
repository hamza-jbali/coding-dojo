from flask import Flask, render_template 
app =Flask(__name__)
@app.route('/')
def index():
    users = [
        {'first_name' : 'hamza', 'last_name' : 'jbali'},
        {'first_name' : 'youssef', 'last_name' : 'jbali'},
        {'first_name' : 'maram', 'last_name' : 'ayari'},
        {'first_name' : 'wala', 'last_name' : 'nasri'}
        ]
    return render_template('index.html',users=users)
if __name__=='__main__':
    app.run(debug=True)