const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function replit(inp) {
	
	const axios = require('axios');
	const fs = require('fs');

	const API_KEY = 'media788788@gmail.com';
	const REPL_ID = 'Medmed1!';
	const FILE_PATH = 'tes.txt';

	async function uploadFile() {
	    try {
	        const fileData = fs.readFileSync(FILE_PATH);

	        const response = await axios.post(`https://replit.com/data/repls/${REPL_ID}/upload`, fileData, {
	            headers: {
	                'Content-Type': 'application/octet-stream',
	                'Authorization': `Bearer ${API_KEY}`
	            }
	        });

	        console.log('File uploaded successfully:', response.data);
	    } catch (error) {
	        console.error('Error uploading file:', error.response ? error.response.data : error.message);
	    }
	}

	uploadFile();
	
	
//comments before final bracket
}
inp = [];
replit(inp)