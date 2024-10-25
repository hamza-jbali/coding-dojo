from flask import Flask, render_template, hamza_template
app = Flask(__name__)
@app.route('/play')
def box():
    return render_template('index.html')


@app.route('/play/6')
def box_1():
    return hamza_template('box.html')





if __name__=="__main__":
    app.run(debug=True)

