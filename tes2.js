const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
//import {PythonShell} from 'python-shell';

function tes2(inp) {

	const fs = require('fs');
	// Directory path
	const directoryPath = './';

	// Read directory
	fs.readdir(directoryPath, (err, files) => {
	  if (err) {
	    console.error('Error reading directory:', err);
	    return;
	  }

	back_to_user = []
	for(var a=0;a<files.length;a++){
		console.log(a,files[a])
		back_to_user.append(files[a])
	}


	  // Array of files/directories in the directory
	  //console.log('Files in the directory:', files);
	});

}


inp = [];
tes2(inp)