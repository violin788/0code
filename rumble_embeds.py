exec(open('util.py').read())

array = []

new = []
new.append("Arizona")
new.append("___persons's name??___")
new.append("Explanation of Voter Fraud")
new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
array.append(new)

new = []
new.append("Arizona")
new.append("___persons's name??___")
new.append("Explanation of Voter Fraud")
new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
array.append(new)

new = []
new.append("Georgia")
new.append("___persons's name??___")
new.append("Explanation of Voter Fraud")
new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
array.append(new)

new = []
new.append("Georgia")
new.append("___persons's name??___")
new.append("Explanation of Voter Fraud")
new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
array.append(new)

new = []
new.append("Michigan")
new.append("___persons's name??___")
new.append("Explanation of Voter Fraud")
new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
array.append(new)

new = []
new.append("Nevada")
new.append("___persons's name??___")
new.append("Explanation of Voter Fraud")
new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
array.append(new)

array.sort()

html_text = "<html>\n"
current_state = ""
current_state_row = 1
new_row = 3
appends = 0

codes = []
codes.append(["new_row",])
new_row = "\n\t"
end_row = "</div>"


for a,val in enumerate(array):
	check_state = val[0]
	if check_state!=current_state:
		current_state_row = 1
		appends = 0
		row_identifier = check_state+"-"+str(current_state_row)
		html_text=html_text+"\n\t<div id=\""+row_identifier+"\" class=\"gjs-grid-row\">"
	col_identifier = 
	html_text=html_text+"\n\t<div id=\""+row_identifier+"\" class=\"gjs-grid-row\">"


	if new_row==3:
		row_identifier = state+"-"+str(current_state_row)
		html_text = html_text+"\n\t<div id=\""+row_identifier+"\" class=\"gjs-grid-row\">"
	html_text = html_text+"\n\t\t<div class=\"gjs-grid-column\">"
	html_text = html_text+"\n\t\t<div class=\"gjs-grid-column\">"



html_text = html_text+"</html>"

print(html_text)
output_file = "election3.html"
write_data([output_file,html_text])
start_file([output_file,1])