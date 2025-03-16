// Execute the file content as JavaScript code

const xlsx = require('xlsx');
const path = require('path');

/**
 * Loads data from an Excel file and returns it as an array.
 * @param {string} filePath - The path to the Excel file.
 * @param {boolean} [asArray=true] - If true, returns data as an array of arrays. If false, returns data as an array of objects.
 * @returns {Array} - The data read from the Excel file.
 */

function end(){process.exit(0);}

function load_data(filePath, asArray = true) {
    try {
        // Ensure the file path is absolute
        filePath = path.resolve(filePath);

        // Read the Excel file
        const workbook = xlsx.readFile(filePath);

        // Get the first sheet (you can adjust this to select a specific sheet)
        const sheetName = workbook.SheetNames[0];
        const sheet = workbook.Sheets[sheetName];

        // Convert the sheet to JSON
        const data = asArray 
            ? xlsx.utils.sheet_to_json(sheet, { header: 1 }) // Array of arrays
            : xlsx.utils.sheet_to_json(sheet); // Array of objects

        return data;
    } catch (error) {
        console.error('Error reading the Excel file:', error);

        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                console.error('Error reading the file:', err);
                return;
            }
            console.log('File content:', data);
        });

        //throw error; // Rethrow the error after logging
    }
}

// Example usage:
// const data = load_data('path/to/your/file.xlsx');
// console.log(data);


/*
eval(fileContent);

const xlsx = require('xlsx');
const csvParse = require('csv-parse/lib/sync');


const xlsx = require('xlsx');
const path = require('path');

// Path to your Excel file
const filePath = path.join(__dirname, 'example.xlsx'); // Replace with your file path

// Read the Excel file
const workbook = xlsx.readFile(filePath);

// Get the first sheet (you can get other sheets using sheet names or indexes)
const sheetName = workbook.SheetNames[0];
const sheet = workbook.Sheets[sheetName];

// Convert the sheet to JSON (array of arrays or array of objects)
const data = xlsx.utils.sheet_to_json(sheet, { header: 1 }); // Use `header: 1` for array of arrays

console.log(data);



function loadData(inp) {
    const loadFile = inp[0];
    let loadedData = '';

    if (path.extname(loadFile) === '.xls' || path.extname(loadFile) === '.xlsx') {
        // Load Excel file
        const workbook = xlsx.readFile(loadFile);
        const sheet1 = workbook.Sheets[workbook.SheetNames[0]];
        const data = xlsx.utils.sheet_to_json(sheet1, { header: 1 });
        
        // Process data to remove empty values
        const newData = data.map(row => {
            const newRow = row.filter(val => val !== '');
            return newRow;
        });
        
        loadedData = newData;
    } else if (path.extname(loadFile) === '.csv') {
        // Load CSV file
        const fileContent = fs.readFileSync(loadFile, 'utf8');
        const records = csvParse(fileContent, { delimiter: ',' });
        loadedData = records;
    } else if (path.extname(loadFile) === '.json') {
        // Load JSON file
        const fileContent = fs.readFileSync(loadFile, 'utf8');
        loadedData = JSON.parse(fileContent);
    } else if (['.txt', '.py', '.js', '.html'].includes(path.extname(loadFile))) {
        // Load text file
        loadedData = fs.readFileSync(loadFile, 'utf8');
    }

    return loadedData;
}

// Example usage:
// console.log(loadData(['path/to/your/file.xlsx']));
*/