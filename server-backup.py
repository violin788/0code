exec(open('util.py').read())
def ser2():
    shutil.copy("util.js","static\\util.js")
    #sye()
    import os
    from flask import Flask,render_template, request 
    app = Flask(__name__,template_folder="templates") 
    @app.route("/") 
    def main_page_to_host(): 
        #html = load_data(["table20.html"])
        #html = load_data(["client.html"])
        #html = load_data(["client2.html"])
        html = load_data(["ajax.html"])
        to_be_hosted = html
        return (to_be_hosted) 
    @app.route("/util.js")
    def util_js_to_host():
        util_js_code = load_data(["util.js"])
        to_be_hosted = util_js_code
        return (to_be_hosted)
    @app.route('/process', methods=['POST']) 
    def process(): 
        client_post = request.get_json() # retrieve the data sent from JavaScript 
        print("input data= ",client_post)
        print("input data type= ",type(client_post))
        file_to_read_write = "count.txt"
        counter = int(load_data([file_to_read_write]))
        counter = counter+1
        #load_file = "earn\\"+data+"-prices_around_earnings.xls"
        load_file = "earn\\""dev.xls"
        data_in_ram = load_data([load_file])
        norm = client_post.upper()
        to_be_returned = []
        for a,val in enumerate(data_in_ram):
            if norm in val[0]:
                to_be_returned.append(val)
        #stock_data = load_data([load_file])
        #to_be_returned = send_back
        print("return data= ",to_be_returned)
        print("return data type= ",type(to_be_returned))
        return to_be_returned # return the result to JavaScript
    if __name__=='__main__':
       port = 5000
       url = "http://localhost:"+str(port)+"/"
       command = "start "+url
       os.system(command)
       app.run(debug=True, port=port)

inp = []
ser2()
