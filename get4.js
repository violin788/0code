import fetch from "node-fetch";
// API for get requests
let fetchRes = fetch(
"https://jsonplaceholder.typicode.com/todos/1");
    
// FetchRes is the promise to resolve
// it by using.then() method
fetchRes.then(res =>
    res.json()).then(d => {
        console.log(d)
    })