exec(open('util.py').read())
main_page_html = load_data(["stock_new.html"])
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle POST request
        name = request.form['name']  # Access form data
        # Process the data (e.g., save to database, perform calculations)
        return("ye")
        #return 'Hello, {}! Your data has been processed.'.format(name)
    else:
        # Handle GET request
        #return render_template('index.html')
        return(main_page_html)
if __name__ == '__main__':
    #app.run(debug=True)
    port = 5000
    url = "http://localhost:"+str(port)+"/"
    subprocess_open([0,url,"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
    app.run(debug=True, port=port)
