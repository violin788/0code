const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function test2(inp) {
	

// Requiring fs module in which
// writeFile function is defined.
	const fs = require('fs')
	 
	// Data which will write in a file.
	let data = "Learning how to write in a file."
	 
	// Write data in 'Output.txt' .
	fs.writeFile('test2.txt', data, (err) => {
	 
	    // In case of a error throw err.
	    if (err) throw err;
	})
	
	
//comments before final bracket
}
inp = [];
test2(inp)