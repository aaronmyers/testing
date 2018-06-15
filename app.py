from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import os
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MONGODB_URI']
mongo = PyMongo(app)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    value = mongo.db.testColl.find_one()

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <h2> Your query returned with {query}.</h2>
    <img src="http://loremflickr.com/600/400">


    """.format(time=the_time,query=value)

if __name__ == '__main__':
    app.run()
