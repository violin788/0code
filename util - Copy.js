
/*

cwd = process.cwd()
const files = fs.readdirSync(cwd);

user_input = prompt('what is the user input? = ');
for loop

for(var a=0;a<___.length;a++){
	console.log(a,___[a])
}

if (file1.includes(file2)==false){console.log("naw")}

*/

const prompt = require('prompt-sync')({sigint: true});
const shell = require('shelljs');
const fs = require('fs'); 

function load_libraries(inp) {
	const prompt = require('prompt-sync')({sigint: true});
	const shell = require('shelljs');
	const fs = require('fs'); 
	//bracket to end fuction}
	}

function pri(input){
	//pri([input])
	if(input.length>1){input=[input]}
	to_print = input[0]
	if(typeof to_print=="object"){
		for(var a=0;a<to_print.length;a++){
			out_string = ""
			for(var b=0;b<to_print[a].length;b++){
				out_string=out_string+to_print[a][b]+","
				//console.log(a,b,to_print[a][b])
			}
			console.log(a,out_string)
			//console.log(a,to_print[a])
		}
	}
	if(typeof to_print=="string"){
		console.log(to_print)
	}
	//bracket to end fuction}
	}

	/*
function load_data(inp) {
	//data = load_data([load_file]);
	load_file = inp[0]
	back_data = ""
	if(load_file.includes(".txt")==true){
		var readTextFile = require('read-text-file');
		var contents = readTextFile.readSync(load_file);
		back_data = contents
	}
	if(load_file.includes(".js")==true){
		var readTextFile = require('read-text-file');
		var contents = readTextFile.readSync(load_file);
		back_data = contents	
	}
	if(load_file.includes(".py")==true){
		var readTextFile = require('read-text-file');
		var contents = readTextFile.readSync(load_file);
		back_data = contents		
	}
	if(load_file.includes(".csv")==true){
		var readTextFile = require('read-text-file');
		var contents = readTextFile.readSync(load_file);
		back_data = contents		
	}
	if(load_file.includes(".xls")==true){
		//file_name = inp[0]
		var XLSX = require("xlsx");
		var workbook = XLSX.readFile(load_file);
		let worksheet = workbook.Sheets[workbook.SheetNames[0]];
		var populated_cells = []
		Object.keys(worksheet).forEach((prop)=> populated_cells.push(prop));
		var data = []
		new_row = []
		for (a=0;a<populated_cells.length;a++){
			cell_address = populated_cells[a]
			if (cell_address.includes("!")) {continue;}
			if (cell_address.includes("A")) {
				//console.log(new_row)
				if(new_row.length>0){data.push(new_row)}
				new_row = []
				//console.log(cell_address)}
			}
			//console.log(worksheet[cell_address].v)
			new_row.push(worksheet[cell_address].v);
		}
		back_data = data
		//return data		
	}
	return back_data
	//bracket to end fuction}
	}
	*/
function get_cwd(){
	//cwd = get_cwd()
	folder = (__dirname);
	return folder
//end function bracket
}

function run_python(input){
	//run_python("file.py")
	const { PythonExecutor } = require("python-spawn");
	const executor = new PythonExecutor();
	executor.executeScript(input)
//end function bracket
}

function sort_array(input){
	//new_array = sort_array([array,2])
	array = input[0]
	column_to_sort_by = input[1]
	idens = []
	for(var a=0;a<array.length;a++){
		idens.push(array[a][column_to_sort_by])
	}
	idens.sort()
	new_array = []
	for(var a=0;a<idens.length;a++){
		for(var b=0;b<array.length;b++){
			if(array[b].includes(idens[a])==true){
				new_array.push(array[b])
			}
		}
	}
	//console.log(new_array)
	return new_array
//end function bracket	
}

function gen_table_html(input){
	//html_text = gen_table_html([array])
	text = ""
	text = text+"<table>"
	array = input[0]
	for(var a=0;a<array.length;a++){
		text = text+"<tr>"
		for(var b=0;b<array[a].length;b++){
			text = text+"<td>"+array[a][b].toString()+"</td>"
		}
		text = text+"</tr>"
	}
	text = text+"</table>"
	return text
}


function read_txt(input){
	//back = read_txt(["file.txt"])
	const filePath = input[0];
	const contents = fs.readFileSync(filePath, 'utf8');
	return contents
//bracket to end fuction
}


/*

def load_data(inp):
	#data = load_data([load_file])
	load_file = inp[0]
	print("load_file = "+str(load_file))
	loaded_data = ""
	if ".xls" in load_file:
		import xlrd
		workbook = xlrd.open_workbook(load_file)
		sheet1 = workbook.sheet_by_index(0)	
		new_data = []
		for rowNumber in range(sheet1.nrows):
		    row = sheet1.row_values(rowNumber)
		    check = row[::-1]
		    new_row = []
		    for a,val in enumerate(check):
		    	if len(val)==0:
		    		continue
		    	new_row.append(val)
		    new_row = new_row[::-1]
		    new_data.append(new_row)
		loaded_data = new_data
	if ".csv" in load_file:
		def read_csv(inp):
			import csv
			file = inp[0]
			back = []
			with open(file, newline='') as f:
			    reader = csv.reader(f)
			    for row in reader:
			        #print(row)	
				    back.append(row)
			return back
		#file = load_file
		loaded_data = read_csv([load_file])
		#pri(back)
	if ".json" in load_file:
		with open(load_file, 'r') as f:
			loaded_data = json.load(f)
	if ".txt" in load_file or ".py" in load_file or ".js" in load_file or ".html" in load_file:
		text = open(load_file, "r")
		loaded_data = text.read()
	return loaded_data

*/


function load_data(input){
	//back = load_data(["earn.html"])
	file_to_load = input[0]
	load_text = 0
	var text_yes = [".txt",".html",".js",".py"]
	for(var a=0;a<text_yes.length;a++){
		val = text_yes[a]
		if (file_to_load.includes(val)==true){
			load_text=1
			break
		}
	}
	if(load_text==1){
		//const filePath = input[0];
		const encoding = 'utf-8';
		const contents = fs.readFileSync(file_to_load, encoding);		
		//console.log(contents)
		return contents
	}
	if (file_to_load.includes(".xls")==true){
		//file_name = inp[0]
		var XLSX = require("xlsx");
		var workbook = XLSX.readFile(file_to_load);
		let worksheet = workbook.Sheets[workbook.SheetNames[0]];
		var populated_cells = []
		Object.keys(worksheet).forEach((prop)=> populated_cells.push(prop));
		var data = []
		new_row = []
		for (a=0;a<populated_cells.length;a++){
			cell_address = populated_cells[a]
			if (cell_address.includes("!")) {continue;}
			if (cell_address.includes("A")) {
				//console.log(new_row)
				if(new_row.length>0){data.push(new_row)}
				new_row = []
				//console.log(cell_address)}
			}
			//console.log(worksheet[cell_address].v)
			new_row.push(worksheet[cell_address].v);
		}
		back_data = data
		//return data		
		return back_data

	}	
	if (file_to_load.includes(".csv")==true){
		load_text=1
		//break
	}	
//bracket to end function
}


function start_file(input){
	//start_file(["firefox_lnk"])
	file_to_start = input[0]
	const { exec } = require('child_process');
	exec(file_to_start, (error, stdout, stderr) => {
	  if (error) {
	    console.error(`exec error: ${error}`);
	    return;
	  }
	  console.log(`stdout: ${stdout}`);
	  console.error(`stderr: ${stderr}`);
	});
//bracket ending function
}

function run_in_shell(input){
	//run_in_shell([command])
	command = input[0]
	const { exec } = require('child_process');
	//const command = "";
	exec(command, (error, stdout, stderr) => {
	  if (error) {
	    console.error(`exec error: ${error}`);
	    return;
	  }
	  console.log(`stdout: ${stdout}`);
	  console.error(`stderr: ${stderr}`);
	});
//end bracket
}

function end(){
	process.exit();
}


function gen_file_list(input){
	//files = gen_file_list([cwd])
	directory = input[0]
//end bracket
}

function replace2(input){
	//back = replace2([string,what_to_replace,replace_with_what])
	//back = replace2([text,"abc","123"])
	original_string = input[0]
	what_to_replace = input[1]
	replace_with_what = input[2]
	let regex = new RegExp(what_to_replace,'g');
	// Replace all occurrences
	let modifiedString = original_string.replace(regex, replace_with_what);
	return modifiedString

}

function iframe_generator(input){
	iframe_outline = `
	__title__
	<br>
	<iframe 
	    class="rumble" 
	    width="640" 
	    height="360" 
	    src="https://rumble.com/embed/__rumble_code__/?pub=3i4h9q" 
	    frameborder="0" 
	    allowfullscreen
	    loading="lazy"

	    >
	</iframe><br>`
	//new_html_code = iframe_generator([rumble_code,explanation])
	rumble_code = input[0]
	explanation = input[1]	
	//file_to_load = "iframe_outline.html"
	//html_loaded = read_txt([file_to_load])	
	//new_code = html_loaded.replace("\"","\\\"")
	new_code = iframe_outline
	new_code = replace2([new_code,"\"","\\\""])
	new_code = replace2([new_code,"__rumble_code__",rumble_code])
	new_code = replace2([new_code,"__title__",explanation])
	//__rumble_code__
	console.log(new_code)
	//console.log(html_to_load)
	return new_code
//end bracket
}

