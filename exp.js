const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);

const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  html_code = read_txt(["earn.html"])
  //html_code = html_code.toString()
  console.log(html_code)
  //res.send(html_code)
  res.send(html_code)
})


// Middleware to parse JSON bodies
app.use(express.json());

// POST endpoint to handle incoming data

//handle_post
//app.post('/api/data', (req, res) => {
app.get('/handle_post', (req, res) => {
  // Extract data from request body
  //const { name, email } = req.body;
  console.log(req)
  // Do something with the data
  //console.log('Received data:', { name, email });

  // Respond with a success message
  res.status(200).send('Data received successfully');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
  url = "http://localhost:"+port.toString()+"/"
  command = "start "+url
  run_in_shell([command])

})