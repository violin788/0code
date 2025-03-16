exec(open('util.py').read())
def ser2():
    #shutil.copy("util.js","static\\util.js")
    #shutil.copy("ajax_code.js","static\\ajax_code.js")
    #sye()
    import os
    from flask import Flask,render_template, request 
    app = Flask(__name__,template_folder="templates") 
    @app.route("/ajax_code.js")
    def ajax_code_to_host():
        util_js_code = load_data(["ajax_code.js"])
        to_be_hosted = util_js_code
        return (to_be_hosted)
    @app.route("/") 
    def main_page_to_host(): 
        html = load_data(["template.html"])
        to_be_hosted = html
        return (to_be_hosted) 
    @app.route("/about_us")
    def about_us():
        html_code = load_data(["about_us.txt"])
        return (html_code)      
    #for new file copy and paste above 
    @app.route('/handle_post', methods=['POST']) 
    def process(): 
        client_post = request.get_json() # retrieve the data sent from JavaScript 
        print("input data= ",client_post)
        print("input data type= ",type(client_post))
        #load_file = "earn\\"+data+"-prices_around_earnings.xls"
        symbol = client_post[0:client_post.find("-")]
        symbol = symbol.upper()
        print ("symbol="+symbol)
        to_find = client_post[client_post.find("-")+1:len(client_post)]
        print ("to_find="+to_find)
        earn_lis = os.listdir("earn")
        load_file = ""
        for a,val in enumerate(earn_lis):
            if symbol in val:
                if to_find in val:
                    load_file = val
                    break
        #load_file = "C:\\Users\\-\\code\\earn\\"+load_file
        cwd = os.getcwd()
        load_file = cwd+"\\earn\\"+load_file
        array_in_ram= load_data([load_file])
        to_be_returned = ""
        to_be_returned = to_be_returned+"<table border=2>"
        for a,val in enumerate(array_in_ram):
            to_be_returned = to_be_returned+"<tr>"
            for b,valb in enumerate(array_in_ram[a]):
                to_be_returned = to_be_returned+"<td>"+array_in_ram[a][b]+"</td>"
            to_be_returned = to_be_returned+"</tr>"
        to_be_returned = to_be_returned+"</table>"
        #to_be_returned = []
        #for a,val in enumerate(data_in_ram):
         #   if norm in val[0]:
         #       to_be_returned.append(val)
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
