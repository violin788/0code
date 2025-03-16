exec(open('util.py').read())
import os
from flask import Flask,render_template, request 
app = Flask(__name__,template_folder="templates") 
@app.route("/") 
def hello(): 
    html = load_data(["index2.html"])
    return (html) 
@app.route('/process', methods=['POST']) 
def process(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    #result = data['value'] * 2
    #result = data['value']
    print("input data= ",data)
    print("input data type= ",type(data))
    #to_be_returned = "bark"
    file_to_read_write = "count.txt"
    counter = int(load_data([file_to_read_write]))
    counter = counter+1
    #to_be_returned = {"value": counter}
    load_file = "earn\\"+data+"-prices_around_earnings.xls"
    stock_data = load_data([load_file])
    string = ""
    for a,val in enumerate(stock_data):
      string = string+str(val)+"\n"
    print(string)
    string = string.replace("\n","<br>")
    return_items = []
    return_items.append(load_file)
    #return_items.append(counter)
    return_items.append(string)
    return_data = ""
    for a,val in enumerate(return_items):
      return_data = return_data+str(val)+"<br>"
    print("return data= ",return_data)
    print("return data type= ",type(return_data))
    write_data([file_to_read_write,str(counter)]) 
    return return_data # return the result to JavaScript
    #return jsonify(result=result) # return the result to JavaScript 

@app.route('/handle_get', methods=['GET']) 
def handle_get(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    #result = data['value'] * 2
    #result = data['value']
    print("input data= ",data)
    print("input data type= ",type(data))
    #to_be_returned = "bark"
    file_to_read_write = "count.txt"
    counter = int(load_data([file_to_read_write]))
    counter = counter+1
    #to_be_returned = {"value": counter}
    to_be_returned = str(counter)
    print("return data= ",to_be_returned)
    print("return data type= ",type(to_be_returned))
    write_data([file_to_read_write,str(counter)]) 
    return to_be_returned # return the result to JavaScript
    #return jsonify(result=result) # return the result to JavaScript 


if __name__=='__main__':
   port = 5000
   url = "http://localhost:"+str(port)+"/"
   command = "start "+url
   os.system(command)
   app.run(debug=True, port=port)
