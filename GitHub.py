from flask import Flask,render_template,request
import requests
app = Flask(__name__)
base_url="https://api.github.com/users/"


@app.route("/",methods = ["GET","POST"])
def home():
    if request.method =="POST":
        githubname = request.form.get("githubname")
        responce = requests.get(base_url + githubname)
        userinfo = responce.json()
        return render_template("index.html",profile = userinfo)
    else:

        return render_template("index.html",methods = ["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True)