const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function gui(inp) {
	
const { QLabel, QMainWindow} = require("nodegui");
const win = new QMainWindow();
const label = new QLabel(win);
label.setText("Hello world");
label.setInlineStyle("color: green; background-color: white;");
win.show();
global.win = win;	


//comments before final bracket	
}
inp = [];
gui(inp)