//http://localhost:5000/
/*
url = "http://localhost:5000/"
fetch(url) // api for the get request
    .then(response => response.json())
    .then(data => console.log(data));
    */

//const jsonData = { key1: 'value1', key2: 'value2' };

// Set up options for the fetch request
const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json' // Set content type to JSON
  },
  //body: JSON.stringify(jsonData) // Convert JSON data to a string and set it as the request body
  //body: JSON.stringify("blk")
  //body: JSON.stringify("XOM-yfinance_history_corrected")
  body: JSON.stringify("XOM-yfinance_history_corrected")
};

//url = "http://localhost:5000/"
url = "http://localhost:5000/handle_post"
// Make the fetch request with the provided options
fetch(url, options)
  .then(response => {
    // Check if the request was successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the response as JSON
    return response;
    //return response;
  })
  .then(data => {
    // Handle the JSON data
    console.log(data.json());
    //console.log(data.value);
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetch error:', error);
  });