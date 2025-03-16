
const prompt = require('prompt-sync')({sigint: true});
const shell = require('shelljs');
const fs = require('fs'); 
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);


file_name = prompt('what is name of new .js file? = ');
new_file = file_name+".js";
console.log(new_file);
text = ""
text = text+"const fs = require('fs');\n"
text = text+"const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);\n"
text = text+"function ___(inp) {\n"
text = text+"\t\n"
text = text+"\t\n"
text = text+"\t\n"
text = text+"//comments before final bracket\n"
text = text+"}\n"
text = text+"inp = [];\n"
text = text+"___(inp)"
text = text.replace("___", file_name)
text = text.replace("___", file_name)

fs.writeFileSync(new_file,text); 
file_to_open = "C:\\Users\\--\\code\\"+new_file
//shell.exec(new_file);
console.log(file_to_open)
start_file([file_to_open])