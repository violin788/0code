const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'},
  body: JSON.stringify("TSLA-yfinance_history_corrected")};
url = "http://localhost:5000/handle_post"
fetch(url, options)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');}
    return response;})
  .then(data => {
    console.log(data.json());})
  .catch(error => {
    console.error('Fetch error:', error);});