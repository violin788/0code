const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function txt(inp) {
	
	fetch("test.txt")
	    .then(function (res) {
	        return res.text();
	    })
	    .then(function (data) {
	        console.log(data);
	    });	
	
//comments before final bracket
}
inp = [];
txt(inp)