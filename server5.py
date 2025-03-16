# import flast module
from flask import Flask
# instance of flask application
app = Flask(__name__)
# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return "<p>hello world!</p>"
@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
    	return "test"
if __name__ == '__main__':  
   #app.run()
   app.run(debug=True, port=5000)