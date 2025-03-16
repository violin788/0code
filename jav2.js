var XLSX = require("xlsx");
var workbook = XLSX.readFile("ear-11-28.xlsx");

/*
ans = "<img src=\"cat.jpg\" onmouseover=\"edit(this)\">"
ans2=ans.search("cat.jpg")
if(ans2>=0){ans3=ans.replace("cat","cat2")}
if(ans2<0){ans3=ans.replace("cat2","cat")}
*/

console.log(workbook)
