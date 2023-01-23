from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class games(db.Model):
    id = db.Column('game_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    console = db.Column(db.String(50))
    player = db.Column(db.String(200))
    price = db.Column(db.String(10))


def __init__(self, name, console, player, price):
    self.name = name
    self.console = console
    self.player = player
    self.price = price


@app.route('/')
def index():
    return 'My name is Jomar Quiban'

@app.route('/games')
def show_all():
    return render_template('show_all.html', game=games.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form[
                'console'] or not request.form['player']:
            flash('Please enter all the fields', 'error')
        else:
            game = games(request.form['name'], request.form['console'],
                               request.form['player'], request.form['price'])

            db.session.add(game)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)


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
