from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#HW3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'

db = SQLAlchemy(app)


class Car(db.Model):
  id = db.Column('car_id', db.Integer, primary_key=True)
  make = db.Column(db.String(100))
  model = db.Column(db.String(100))
  year = db.Column(db.String(50))

  def __repr__(self):
    return '<Car %r>' % self.make


# create / use the database
with app.app_context():
  db.create_all()


@app.route('/list')
def list():
  return render_template('list.html', car=Car.query.all())


#HW1
@app.route('/')
def index():
  return 'My name is Jomar Quiban'


@app.route('/about')
def about():
  return 'I am a student under the program of IT Web Development, I plan to continue my bachelor degree under the program of Software Development at North Seattle College.'


#HW2
@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
  # if POST, calculate fortune based on submission
  # pass calculated fortune to template for display
  if request.method == 'POST':
    # what color & number were submitted?
    color = request.form.get('color')
    number = request.form.get('number')
    username = request.form.get('user')
    # If color blue and number 3 then the fortune is gonna be lucky
    if color == 'blue' and number == '1':
      fort = 'LUCKY'
    elif color == 'blue' and number == '2':
      fort = 'UNLUCKY'
    elif color == 'blue' and number == '3':
      fort = 'HALF LUCKY'
    elif color == 'blue' and number == '4':
      fort = 'HALF LUCKY'
    elif color == 'blue' and number == '5':
      fort = 'LUCKY'
    elif color == 'purple' and number == '1':
      fort = 'LUCKY'
    elif color == 'purple' and number == '2':
      fort = 'MUCH LUCKY'
    elif color == 'purple' and number == '3':
      fort = 'VERY LUCKY'
    elif color == 'purple' and number == '4':
      fort = 'REALLY LUCKY'
    elif color == 'purple' and number == '5':
      fort = 'LUCKY'
    elif color == 'yellow' and number == '1':
      fort = 'UNLUCKY'
    elif color == 'yellow' and number == '2':
      fort = ' HALF LUCKY'
    elif color == 'yellow' and number == '3':
      fort = 'LUCKY'
    elif color == 'yellow' and number == '4':
      fort = 'UNLUCKY'
    elif color == 'yellow' and number == '5':
      fort = 'ALMOST UNLUCKY'
    elif color == 'orange' and number == '1':
      fort = 'ALMOST LUCKY'
    elif color == 'orange' and number == '2':
      fort = 'LUCKY'
    elif color == 'orange' and number == '3':
      fort = 'VERY LUCKY'
    elif color == 'orange' and number == '4':
      fort = 'NOT REALLY LUCKY'
    elif color == 'orange' and number == '5':
      fort = 'LUCKY'
  else:
    fort = None
  return render_template("fortune.html", fortune=fort, user=username)


app.run(host='0.0.0.0', port=81)
