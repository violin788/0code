const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function get(inp) {
	
	// Instantiating new XMLHttpRequest() method
	var XMLHttpRequest = require('xhr2');
	let xhr = new XMLHttpRequest();
	 
	// open() method to pass request
	// type, url and async true/false 
	xhr.open('GET',
	    'https://jsonplaceholder.typicode.com/users/2', true);
	 
	// onload function to get data 
	xhr.onload = function () {
	    if (this.status === 200) {
	    	back = JSON.parse(this.responseText)
	        //console.log(JSON.parse(this.responseText));
	        console.log(back)
	    }
	}
	 
	// Send function to send data
	xhr.send()	
	
//comments before final bracket
}
inp = [];
get(inp)