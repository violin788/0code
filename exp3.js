const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function exp3(inp) {
	const express = require('express');
	const app = express();
	const PORT = 3000; // Or any port of your choice
	app.get('/ajax_code.js', (req, res) => {
		html_code = read_txt(["ajax_code.js"])
		res.send(html_code)
	})
	app.get('/', (req, res) => {
	  html_code = read_txt(["earn3.html"])
	  console.log(html_code)
	  res.send(html_code)
	})

	app.use(express.json());

	app.get('/handle_post', (req, res) => {
		//obj1 = JSON.parse(req)
		//obj2 = JSON.parse(res)
		//obj1 = JSON.parse(req);
		//obj2 = JSON.parse(res);
		console.log(req)
		console.log(res)
		res.status(200).send('Data received successfully');
	});
	// Start the server
	app.listen(PORT, () => {
	  console.log(`Server is running on port ${PORT}`);
	  url = "http://localhost:"+PORT.toString()+"/"
	  command = "start "+url
	  run_in_shell([command])
	});	
//comments before final bracket
}
inp = [];
exp3(inp)