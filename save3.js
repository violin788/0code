const { exec } = require('child_process');
// Path to your 7z executable (make sure 7z is installed on your system)
const sevenZPath = '/path/to/7z';
// Path to your 7z archive
const archivePath = 'path/to/archive.7z';
// Path to the file you want to add to the archive
const filePathToAdd = 'path/to/file.txt';
// Construct the command to add the file to the archive
const command = `"${sevenZPath}" a "${archivePath}" "${filePathToAdd}"`;
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
