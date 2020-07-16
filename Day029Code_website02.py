#100DaysOfCode 029/100 - Website continued
#
#  20200716 - 100DaysOfCode 029/100 - Website
#
#
#
#
################################################################################
#  import the Flask class object from the flask library
#  render_template will use HTML in the TEMPLATES folder
#  Folder layout and naming is important
from flask import Flask, render_template
#  create a variable to store the flask object
app=Flask(__name__)
#  need a decoratoer (?)
#  this is the storage locaton "/" means home page
@app.route('/')
#  function to define the webpage
def home():
    return render_template("home.html")
#  add an about page
@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)

#Save and run - the site is live on the local host - localhose:5000 in browser
