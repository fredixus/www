import os
import requests

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
  
aNames = [
"Registration: Users should be able to register for your website, providing (at minimum) a username and password.",
"Login: Users, once registered, should be able to log in to your website with their username and password.",
"Logout: Logged in users should be able to log out of the site.",
"Import: Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN number, a title, an author, and a publication year. In a Python file called import.py separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running python3 import.py to import the books into your database, and submit this program with the rest of your project code.",
"Search: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!",
"Book Page: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.",
"Review Submission: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.",
"Goodreads Review Data: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.",
"API Access: If users make a GET request to your website’s /api/<isbn> route, where <isbn> is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format"
]
aLinks = ["index","login","register"]
@app.route("/")
@app.route("/index")
def index():
    headline = "Hello, world!"
    return render_template("index.html", title="Strona Glowna",headline=headline, new_year=True,names = aNames,links = aLinks)
    #return "Project 1: TODO - with changes <br>"+ str(res.json())

@app.route("/register")
def register():
    return render_template("register.html", title="Rejestracja",links = aLinks,headline="Rejestracja")


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
    
@app.route("/notes", methods=["GET", "POST"])
def notes():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html", notes=session["notes"])
   
#afterReg
@app.route("/afterReg", methods=["GET", "POST"])
def afterReg():
    if session.get("register") is None:
        session["register"]= []
    if request.method == "POST":
        if session["register"]== []:
            id = 1
        else:
            id = session["register"][-1]['Id'] + 1
        name = request.form.get("name")
        passwd = request.form.get("pass")
        session["register"].append({"Id":id,"Name: ":name,"Pass: ":passwd})
    return render_template("afterReg.html", header = "Database snapshot",users=session["register"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("login") is None:
        session["login"] = []
    if request.method == "POST":  
        name = request.form.get("name")
        passwd = request.form.get("pass")
        session["login"].append({"Name: ":name,"Pass: ":passwd})
    return render_template("login.html", users=session["login"], title="Logowanie",links = aLinks,headline="Logowanie")
    
