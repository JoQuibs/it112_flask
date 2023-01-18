from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'My name is Jomar Quiban'


@app.route('/about')
def about():
    return 'I am a student under the program of IT Web Development, I plan to continue my bachelor degree under the program of Software Development at North Seattle College.'


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    return render_template("user.html")


@app.route('/user/<username>')
def user_info(username):
    return
    render_template('user.html',
                    user=[{
                        "name": "Jomar",
                        "since": 2012
                    }, {
                        "name": "Quiban",
                        "since": 2015
                    }])


app.run(host='0.0.0.0', port=81)
