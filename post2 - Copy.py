exec(open('util.py').read())
main_page_html = load_data(["post2.html"])
from flask import Flask, request, render_template
from flask import Flask, render_template, request, jsonify
import data
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post_received = request.form['symbol']
        print(post_received)

        #get data here..and send back?
        
        to_send_back = post_received
        return(to_send_back)    
    #return render_template('index.html')
    return(main_page_html)
if __name__ == '__main__':
    #app.run(debug=True)
    port = 5000
    url = "http://localhost:"+str(port)+"/"
    subprocess_open([0,url,"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
    app.run(debug=True, port=port)
