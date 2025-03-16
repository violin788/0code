const { PythonExecutor } = require("python-spawn");

// Creating an Instance


function load_txt(input){
  const executor = new PythonExecutor();
  executor
    .executeScript("earn.py")
    .then((result) => console.log(result))
    .catch((error) => console.error(error));
}


/*
// Executing a Python Script
executor
  .executeScript("/path/to/your/script.py")
  .then((result) => console.log(result))
  .catch((error) => console.error(error));

// Executing a Python Function withing a Script
executor
  .executeScript("/path/to/your/script.py", "function_name", ["arg1", "arg2"])
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
  */