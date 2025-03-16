
def ser_test():


    import os
    from flask import Flask,render_template, request 

    app = Flask(__name__)
    @app.route("/ajax_code.js")
    def ajax_code_to_host():
        util_js_code = load_data(["ajax_code.js"])
        to_be_hosted = util_js_code
        return (to_be_hosted)


    @app.route("/")
    def hello_world():
        return """
    <!DOCTYPE html> 
    <html> 
    <head> 
        <title>JavaScript to Python Example</title> 
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <!--
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> 
    -->
    </head> 
    <style type="text/css">
        th, td {
          padding: 2px;
          /*
          border: 1px solid black;
          */
        }    
    </style>
    <body> 
        Type the stock symbol you want to know about.<br>
        <input type="text" id="input_symbol"><br>
        and then click the information you want to have.<br><br>
        <button id="button_prices" onclick="return_prices()">Historical Prices</button> 
        <button id="button_earnings" onclick="return_earnings()">Historical Earnings</button><br><br>
        <button id="button_earnings_prices" onclick="return_earn_prices()">Prices Around Earnings</button><br><br>
        <!--<button onclick="sendData()">inquire!</button>-->
        <a href="/about_us" target="_blank" class="block" font="6">about us</a>
        <div id="output_data1">output_data1</div>
        <div id="output_data2">output_data2</div> 
        <script> 
            function return_prices() { 
                var symbol = document.getElementById('input_symbol').value; 
                var what_to_get = 
                $.ajax({url: '/handle_post',
                        type: 'POST',
                        contentType: 'application/json', 
                        data: JSON.stringify(symbol+"-yfinance_history_corrected"),
                        success: function(response){
                            array = response
                            //return array
                            document.getElementById('output_data2').innerHTML = array;
                        },
                        error: function(error){console.log(error);}});}
                //document.getElementById('output').innerHTML = array;
        </script> 
    </body> 
    </html> 

    """
    @app.route('/handle_post', methods=['POST']) 
    def process(): 
        return "meow" # return the result to JavaScript

    if __name__=='__main__':
       port = 5000
       url = "http://localhost:"+str(port)+"/"
       command = "start "+url
       os.system(command)
       app.run(debug=True, port=port)

inp = []
ser_test()