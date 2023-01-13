from flask import Flask

app = Flask(__name__)



@app.route('/fortune')
def fortune():
  return 'Fortune Teller'

@app.route('/user/<username>')
def user_info(username):
  return
  render_template('user.html',
                 user=[
                   {
"name": "Jomar",

"since": 2012    
                   },
                  {
"name": "Quiban",

"since": 2015  
                    
                  }



                   
                 ]
                 
                 
                 )
app.run(host='0.0.0.0', port=81)
