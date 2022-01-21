from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))

@app.route("/")
def hello_world():
    return render_template("link.html")

@app.route("/t")
def thandle():
    return render_template("home.html")

@app.route("/formhandle",methods=["POST","GET"])
def handlingform():
    if request.method=="POST":
        a=request.form.get("name") #get data from form
        q=User(username=a) #assign values inside table
        db.session.add(q)
        db.session.commit()
        return redirect(url_for("hello_world")) #return to home landing page
    else:
        return "<h1>wrong route call</h1>"

@app.route("/data")
def abc():
    q=User.query.all()#query to display data syntax => class.query.all() or class.query.filter_by(colname=data).first()
    return render_template("data.html",data=q)
##hello this change is from 7coder77
#plz show this in anij


if __name__=="__main__":
    app.run(debug=True)
