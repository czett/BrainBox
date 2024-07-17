from flask import Flask, render_template, redirect, url_for, session, request
import string, random

app = Flask(__name__)
app.secret_key = [random.choice(string.ascii_letters) for i in range(24)]

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")
    if not session:
        return redirect("/")
    

@app.route("/login/<a>/process", methods=["POST"])
def process_login(a):
    #if not session:
    #    return redirect("/")
    
    user = request.form["un"]
    password = request.form["pw"]

    if a == "l":
        return "login"
    else:
        return "register"

if __name__ == "__main__":
    app.run(debug=True, port=5000)