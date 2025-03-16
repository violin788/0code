const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function json(inp) {

	var read = require('read-json-file');
	 
	read("output.json", function(error, data){
	    if (error) {
	        throw error;
	    }
	    console.log(data);
	    //console.log(typeof data);
	    //pri(data)

		var userObjList = JSON.parse(data);
	    var roleList = [];
	    userObjList.forEach(userObj => {
	        roleList.push(userObj.role);
	    });
	    console.log(roleList);	

	});

    //var jsonStr = '[{"role":"noi_user"},{"role":"bert_user"}]';
    
    
//comments before final bracket
}
inp = [];
json(inp)