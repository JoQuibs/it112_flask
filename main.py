from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'My name is Jomar Quiban'


@app.route('/about')
def about():
    return 'I am a student under the program of IT Web Development, I plan to continue my bachelor degree under the program of Software Development at North Seattle College.'


app.run(host='0.0.0.0', port=81)
