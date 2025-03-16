const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');
eval(utils);
//import {PythonShell} from 'python-shell';

loaded_code = html_to_javascript(["iframe_outline.html"])

console.log(loaded_code)