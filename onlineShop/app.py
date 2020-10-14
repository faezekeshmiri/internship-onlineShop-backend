from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(13), unique=True, nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, defult=datetime.utcnow)
    is_producer = db.Column(db.Boolean, nullable=False, defult=False)
    is_staff = db.Column(db.Boolean, nullable=False, defult=False)


@app.route('/<string:name>')
def hello(name):
    return "hello, "+name

if __name__ == "__main__":
    app.run(debug=True) 