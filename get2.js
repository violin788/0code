const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function get2(inp) {
	
	//var XMLHttpRequest = require('xhr2');
	//import fetch from "node-fetch";
	var fetch = require('node-fetch');
	fetch("https://jsonplaceholder.typicode.com/todos", {
	  method: "POST",
	  body: JSON.stringify({
	    userId: 1,
	    title: "Fix my bugs",
	    completed: false
	  }),
	  headers: {
	    "Content-type": "application/json; charset=UTF-8"
	  }
	});	
	
//comments before final bracket
}
inp = [];
get2(inp)