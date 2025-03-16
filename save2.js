const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
//import Seven from 'node-7z'
function save2(inp) {

	cwd = process.cwd()
	const sourcePath = cwd;
	const outputPath = cwd+'\\archive.7z';
	const archivePath = cwd+'\\archive.7z';
	const { exec } = require('child_process');

	const files = fs.readdirSync(cwd);

	//command = `7z a "${outputPath}"`
	files_2 = []
	for(var a=0;a<files.length;a++){
		val = files[a]
		if (val.includes(".")) {
		    //files_2.push(val);
			//command = command+ ` "${val}"`
			const filePathToAdd = val;
			const command = `7z a "${archivePath}" "${filePathToAdd}"`;
			console.log(a,"doing command")
			// Execute the command
			exec(command, (error, stdout, stderr) => {
			    if (error) {
			        console.error(`Error adding file to the archive: ${error.message}`);
			        return;
			    }
			    if (stderr) {
			        console.error(`7z command stderr: ${stderr}`);
			        return;
			    }
			    console.log(`File ${filePathToAdd} added to the archive ${archivePath} successfully.`);
			});

		}
	}




//comments before final bracket
}

inp = [];
save2(inp)