from views import db
from models import Task
from datetime import date
# create the database and the db table
db.create_all()
# insert data
db.session.add(Task("Finish this tutorial", date(2017, 11, 7), 10, 1,1,1))
db.session.add(Task("Finish Real Python", date(2018, 10, 3), 10, 1,1,1))
dbdb.session.commit()
