from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
app.config['ENV'] = 'development'
# creating route
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/success")
def success():
    return "this is success"
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, port=6000)