exec(open('util.py').read())
def server2():

    shutil.copy("util.js","static\\util.js")
    #sye()
    import os
    from flask import Flask,render_template, request 
    app = Flask(__name__,template_folder="templates") 
    @app.route("/") 
    def main_page_to_host(): 
        #html = load_data(["table20.html"])
        html = load_data(["client.html"])
        to_be_hosted = html
        return (to_be_hosted) 
    @app.route("/util.js")
    def util_js_to_host():
        util_js_code = load_data(["util.js"])
        to_be_hosted = util_js_code
        return (to_be_hosted)
    @app.route('/process', methods=['POST']) 
    def process(): 
        data = request.get_json() # retrieve the data sent from JavaScript 
        print("input data= ",data)
        print("input data type= ",type(data))
        file_to_read_write = "count.txt"
        counter = int(load_data([file_to_read_write]))
        counter = counter+1
        load_file = "earn\\"+data+"-prices_around_earnings.xls"
        stock_data = load_data([load_file])
        to_be_returned = stock_data
        print("return data= ",to_be_returned)
        print("return data type= ",type(to_be_returned))
        return to_be_returned # return the result to JavaScript
      
    @app.route('/handle_get', methods=['GET']) 
    def handle_get(): 
        data = request.get_json() # retrieve the data sent from JavaScript 
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

inp = []
server2()
