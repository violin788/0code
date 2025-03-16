const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'},
  body: JSON.stringify("TSLA-yfinance_history_corrected")};
url = "http://localhost:5000/handle_post"
fetch(url, options)
  .then(response => {
    dis = response
    //display = response.json()
    //display2 = display.toString()
    console.log(dis)
    if (!response.ok) {
      throw new Error('Network response was not ok');
  	}
    return response;})
  .then(data => {
    //code or whatever here..
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });