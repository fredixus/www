import os
import requests
import importCSV as IM
import comments as CS
import simplehash as SH

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))

res =  requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "uFHO4yqNDsoifSLOVF07bA", "isbns": "9781632168146"})

def getBookInfoFromApiISBN(isbn):
    return requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "uFHO4yqNDsoifSLOVF07bA", "isbns": str(isbn)}).json()

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
alinksy = ["index","search","notes","logout","register"]

@app.route("/")
@app.route("/index")
def index():
    headline = "Book page - browse your books."
    if (session["login"] != []):
        us = str(session["login"][0]['Name'])
        login=True
        links = alinksy
    else:
        links = aLinks
        us = ""
        login=False
        
    return render_template("index.html", title="Book page",headline=headline,username=us,names = aNames,links = links,login=login)
    #return "Project 1: TODO - with changes <br>"+ str(res.json())

@app.route("/register")
def register():
    return render_template("register.html", title="Register",links = aLinks,headline="Register")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html", notes=session["notes"],links = alinksy,headline="Put your notes")

@app.route("/afterReg", methods=["GET", "POST"])
def afterReg():

    if session.get("register") is None:
        session["register"]= []
    if request.method == "POST":
        if session["register"]== []:
            idVal = 1
        else:
            idVal = session["register"][-1]['Id'] + 1
        name = request.form.get("name")
        passwd = request.form.get("pass")
        if name != "" and name != "":
            session["register"].append({"Id":idVal,"Name":name,"Pass":passwd})
    return render_template("afterReg.html", header = "Database snapshot",users=session["register"][-1]['Name'])

@app.route("/login", methods=["GET", "POST"])
def login():
    name = ""
    passwd = ""
    logined = False
    title = "Try to log in"
    test =  "Try to log in"
    
    if session.get("login") is None:
        session["login"]= []
        name = ""
        passwd = ""
        
    if request.method == "POST" and session.get("login") == []:
        name = request.form.get("name")
        passwd = request.form.get("pass")
        
    if name != "":
      for user in session["register"]:
          if name == user['Name'] and passwd == user['Pass']:
              session["login"].append({"Id":user['Id'],"Name":name})#,"Pass: ":passwd
              test = title = "Successful login" 
              logined = True
              break
          else:
              test = title = "Unsuccessful login" 
              logined = False 
            
    return render_template("login.html", users=session["login"],logined=logined, title=title+str(logined),links = aLinks,headline=test)

@app.route("/users")
def users():
    return render_template("users.html", header = "Users in Data Base",title="Users in DB",links = alinksy,users=session["register"])

@app.route("/search")
def search():
    return render_template("search.html", header = "Find",links = alinksy)

@app.route("/afterSearch", methods=["GET", "POST"])
def afterSearch():
    res = []
    #Get from search
    isbn = request.form.get("isbn")
    title = request.form.get("title")
    author = request.form.get("author")
    i,t,a = [],[],[]

    if (isbn!="") or (title!="") or (author!=""):
        i = IM.check(isbn,IM.liblary)
        t = IM.checkTitle(title,IM.liblary)
        a = IM.checkAuthor(author,IM.liblary)

    if (isbn!="") and (title!=""):res = i + t
    if (isbn!="") and (author!=""):res = i + a
    #need review - check logic
    if (title!="") and (author!=""):
        res = IM.checkTitleAndAuthor(title,author,IM.liblary)
    if (isbn!="") and (title=="") and (author==""):res = i
    if (isbn=="") and (title!="") and (author==""):res = t
    if (isbn=="") and (title=="") and (author!=""):res = a
    if (isbn!="") and (title!="") and (author!=""):res = i + t + a
    if (isbn=="") and (title=="") and (author==""):res = {'Sorry':'we don\'t find anything'}
    x = len(res)
    if res == "" or x == 0 :
        res = [{"Sorry we can't find anything":":-("}]
    return render_template(
    "afterSearch.html",
    resultOfFind = res,
    isbnOfBook = i,
    title = "Search books: "+str(x),
    author = a,
    links = alinksy
    )

@app.route("/book/<string:nbISBN>", methods=['GET', 'POST'])
def book(nbISBN):
    #currentBook = res.json()
    currentBook = getBookInfoFromApiISBN(nbISBN)
    #currentBook = getBookInfoFromApiISBN(nbISBN)
    #currentBook = book1
    newBook = IM.check(nbISBN,IM.liblary)
    getComFromBook = CS.check(nbISBN,CS.liblary)
    return render_template(
        "book.html",
        header = newBook[0]['title'],
        title = newBook[0]['title']+' - '+newBook[0]['author']+' - '+newBook[0]['isbn']+' - '+newBook[0]['year'],
        author =  newBook[0]['author'],
        year = newBook[0]['year'],
        links = alinksy,
        idOfBook=currentBook['books'][0]['id'],
        isbnOfBook=newBook[0]['isbn'],
        isbn=currentBook['books'][0]['isbn13'],
        rat1 = currentBook['books'][0]['reviews_count'],
        rat2 = currentBook['books'][0]['work_ratings_count'],
        rat3 = currentBook['books'][0]['average_rating'],
        reviews = getComFromBook,
        )

@app.route("/api/<string:nbISBN>", methods=['GET', 'POST'])
def api(nbISBN):
    newBook = IM.checkSingle(nbISBN,IM.liblary)
    if newBook!=False:
        currentBook = getBookInfoFromApiISBN(newBook[0]['isbn'])
        obj = {'title':newBook[0]['title'],'author': newBook[0]['author'],'year':newBook[0]['year'],'isbn':newBook[0]['isbn'],'reviews_count':currentBook['books'][0]['reviews_count'],'average_score':currentBook['books'][0]['average_rating']}
    else:
        obj = "404 error"    
    return  f"{obj}"
    
@app.route("/delete", methods=['GET', 'POST'])
def delete():
    del session["register"][0]
    return "Usuwam"
   
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    del session["login"][0]
    logout  = True
    return render_template("login.html", users=session["login"], logined = False, logout=logout,title="Login",links = aLinks,headline="Logout")
                                            
    