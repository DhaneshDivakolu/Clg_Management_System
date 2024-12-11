from flask import Flask,render_template

app = Flask(__name__)
e_database={}
s_database={}
sb_database={}

@app.route("/",methods=["GET"])  #End Point   empty path
def homepage():
    return "<h1>Welcome To QIS College of Engineering & Technology</h1>"

@app.route("/clgreg", methods = ["GET"])
def clgregpage():
    return render_template("clgreg.html")

app.run(debug=True)