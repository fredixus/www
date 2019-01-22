import os
import requests

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "uFHO4yqNDsoifSLOVF07bA", "isbns": "9781632168146"})

"""
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
"""  
  
aNames = ["Adam","Michal","Pablo"]
aLinks = ["register","Michal","index"]
@app.route("/")
@app.route("/index")
def index():
    headline = "Hello, world!"
    return render_template("index.html", title="Strona Glowna",headline=headline, new_year=True,names = aNames,links = aLinks)
    #return "Project 1: TODO - with changes <br>"+ str(res.json())

@app.route("/register")
def register():
    return render_template("register.html", title="Rejestracja",links = aLinks,headline="Rejestracja")


@app.route("/hello", methods=["GET"])
def hello():
    name = request.form.get("name") # take the request the user made, access the form,
                                    # and store the field called `name` in a Python variable also called `name`
    return render_template("hello.html",name=name)