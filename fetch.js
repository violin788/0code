const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function fetch(inp) {
	
	fetch('https://jsonplaceholder.typicode.com/posts').then(function (response) {
		// The API call was successful!
		return response.json();
	}).then(function (data) {
		// This is the JSON from our response
		console.log(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	});
	
	
//comments before final bracket
}
inp = [];
fetch(inp)