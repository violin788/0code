exec(open('util.py').read())
import os
from flask import Flask
# importing Flask and other modules
from flask import Flask, request, render_template 
# Flask constructor
app = Flask(__name__)   
# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def view_form():
    #return render_template('login.html')
    #return render_template('login.html')
    html_code = load_data(["client4.html"])
    return html_code

@app.route('/', methods =["GET", "POST"])
def handle_get():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+first_name + last_name
    print(request)
    print(type(request))
    return "meow"
    #return render_template("form.html")
if __name__=='__main__':
   port = 5500
   url = "http://localhost:"+str(port)+"/"
   command = "start "+url
   os.system(command)
   app.run(debug=True, port=port)
