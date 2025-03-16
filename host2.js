var http = require('http');

// An example of a web server written with Node which responds with 'Hello World'.
// To run the server, put the code into a file called example.js and execute it with the node program.
http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello World\n');
}).listen(6000);

console.log('Server running at http://127.0.0.1:8124/');
//http://localhost:6000/