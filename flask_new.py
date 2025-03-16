
exec(open('util.py').read())
from flask import Flask
app = Flask(__name__)
@app.route('/')
def __main__():
	html_code="""
<!DOCTYPE html> 
<html> 
<head> 
    <title>JavaScript to Python Example</title> 
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> 
</head> 
<body> 
    What stock do you want to know about?<br>
    <input type="text" id="input_symbol"> 
    <button onclick="sendData()">inquire!</button> 
    <div id="dev">dev</div>
    <div id="dev2">dev2</div> 
    <script> 
        function sendData() { 
            var value = document.getElementById('input_symbol').value; 
            $.ajax({url: '/process',
                    type: 'POST',
                    contentType: 'application/json', 
                    data: JSON.stringify(value),
                    success: function(response) {
                    array = response
                    //return array
                    document.getElementById('dev').innerHTML = array;
                    //sorted_data = sort_array([stock_data]);
            },error: function(error){console.log(error);}});} 
            //document.getElementById('output').innerHTML = array;
    </script> 
</body> 
</html> 
"""
	return html_code
@app.route('/cia')
def cia():
	html_code="""
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
The CIA will get you!<br>
<img src="cia/cia.png" alt="Example Image" width="300" height="300">
<script type="text/javascript">

</script>
</html>
"""
	return html_code

if __name__=='__main__':
   port = 5000
   url = "http://localhost:"+str(port)+"/"
   command = "start "+url
   os.system(command)
   app.run(debug=True, port=port)
       