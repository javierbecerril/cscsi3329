# app.py file for Flask app

from flask import Flask
from flask import render_template

##from flask import 

# Create the app
app = Flask(__name__)

# Create a homepage for the app
@app.route("/")
# When we go to our.URL.com/
    # Then flask will run this function below
    # In our function, we will "return"
    # the HTML that we want flask to serve
def base():
  return render_template("base.html")

@app.route("/aboutMe")
def aboutMe():
  return render_template("aboutMe.html")
