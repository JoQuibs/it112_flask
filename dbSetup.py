from main import db
from main import Cars
db.create_all()

car1 = Cars(id=1, make='Honda', model='Civic', year='2018')
car2= Cars(id=2, make='Ford', model='Mustang', year='2015')
car3= Cars(id=3, make='Chevrolet', model='Camaro', year='2010')

db.session.add(car1)
db.session.add(car2)
db.session.add(car3)
db.session.commit()