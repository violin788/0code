const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function client55(inp) {	
	//const fetch = require('node-fetch');
	function getData(){
		//const fetch = require('node-fetch');
		//import fetch from "node-fetch";
		const fetch2 = require('fetch');

		var url = "http://localhost:5500/";
		fetch2(url) // api for the get request
			.then(response => response.json())
			.then(data => console.log(data));
	} 

	getData() 
	
	
//comments before final bracket
}
inp = [];
client55(inp)