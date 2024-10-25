from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello"

@app.route('/Dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:number>/<string:word>')
def repeat_word(number, word):
    return (word + " ") * number
app.run(debug=True, host="localhost", port=8000)
