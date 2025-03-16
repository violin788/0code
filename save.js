const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
//import Seven from 'node-7z'
function save(inp) {

	cwd = process.cwd()
	const sourcePath = cwd;
	// Path where you want to save the compressed file
	//const outputPath = '/path/to/output/archive.7z';
	const outputPath = cwd+'\\archive.7z';
	const { exec } = require('child_process');

	// Path to the directory or files you want to compress
	//const sourcePath = '/path/to/source';

	// Path where you want to save the compressed file
	//const outputPath = '/path/to/output/archive.7z';

	// 7z command to compress the source files/directory to the output archive
	const command = `7z a ${outputPath} ${sourcePath}`;

	// Execute the 7z command as a child process
	exec(command, (error, stdout, stderr) => {
	    if (error) {
	        console.error(`Compression failed: ${error}`);
	        return;
	    }
	    console.log(`Compression successful. Output: ${stdout}`);
	});


/*
const { exec } = require('child_process');

// Paths to the files you want to compress
const file1 = '/path/to/file1.txt';
const file2 = '/path/to/file2.txt';

// Path where you want to save the compressed file
const outputPath = '/path/to/output/archive.7z';

// Construct the command to compress using 7z
const command = `7z a "${outputPath}" "${file1}" "${file2}"`;

// Execute the 7z command as a child process
exec(command, (error, stdout, stderr) => {
    if (error) {
        console.error(`Compression failed: ${error}`);
        return;
    }
    console.log(`Compression successful. Output: ${stdout}`);
});
*/


//comments before final bracket
}

inp = [];
save(inp)