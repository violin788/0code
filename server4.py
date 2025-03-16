exec(open('util.py').read())
# import flask module
from flask import Flask
 
# instance of flask application
app = Flask(__name__)
 
# home route that returns below text 
# when root url is accessed
data = load_data(["sho.txt"])
@app.route("/")
def output_to_user():
    #return "<p>meow, World!</p>"
    return data
 
if __name__ == '__main__':
    #app.run(debug=True, port=8001)
    app.run(debug=True, port=4000)
    #http://127.0.0.1:4000/