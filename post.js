const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function post(inp) {
	
	axios.post("https://jsonplaceholder.typicode.com/todos", {
	    userId: 1,
	    title: "Fix my bugs",
	    completed: false
	  })
	  .then((response) => console.log(response.data))
	  .then((error) => console.log(error));	
	
//comments before final bracket
}
inp = [];
post(inp)