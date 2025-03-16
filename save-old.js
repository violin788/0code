const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
//import Seven from 'node-7z'

	const Seven = require('node-7z');

	// Path to the directory or files you want to compress
	const sourcePath = '/path/to/source';

	// Path where you want to save the compressed file
	const outputPath = '/path/to/output/archive.7z';

	// Create a new Seven instance
	const mySeven = new Seven();

	// Compress the directory or files
	mySeven.add(sourcePath)
	    .then(() => mySeven.add(outputPath, { update: true })) // Update existing archive if exists
	    .then(() => console.log('Compression successful'))
	    .catch(err => console.error('Error compressing files:', err));




/*
function save(inp) {
	const Seven = require('node-7z');
	const fs = require('fs');
	const cwd = process.cwd();
	const lis = fs.readdirSync(cwd);
	//pri([lis])
	files = []
	for(var a=0;a<lis.length;a++){
		val = lis[a]
		if (val.includes(".")==true){
			console.log(a,val) 
			files.push(val)
		}
	}	
	output_file = cwd+"\\"+"0archive.7z"
	const myStream = Seven.add(output_file, files, {
	  recursive: true
	})
	
//comments before final bracket
}
*/
inp = [];
save(inp)