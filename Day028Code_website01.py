#100DaysOfCode 028/100 - Website
#
#  20200713 - 100DaysOfCode 028/100 - Website - with flask
#               this a very simple site with 7 lines of code on the local host.
#               Code was expanded to add a home and about page
#
################################################################################
#  import the Flask class object from the flask library
from flask import Flask
#  create a variable to stor the flask object
app=Flask(__name__)
#  need a decoratoer (?)
#  this is the storage locaton "/" means home page
@app.route('/')
#  function to define the webpage
def home():
    return "Home page content goes here"
#  add an about page
@app.route('/about/')
def about():
    return "This is the about page"

if __name__=="__main__":
    app.run(debug=True)

#Save and run - the site is live on the local host - localhose:5000 in browser
