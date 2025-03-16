exec(open('util.py').read())
def y2m(inp):
	fol = "E:\\Users\\-\\Downloads"
	lis = os.listdir(fol)
	ide = "y2mate.com - "

	url = input("youtube url to get mp3 for = " )
	equ = url.find("=")
	cod = url[equ+1:len(url)]
	get = ["https://www.y2mate.com/youtube/"+cod]

	print (url,cod)
	sye()


	for a,val in enumerate(lis):
		print(val)
		if ide in val:
			old = fol+"\\"+val
			new = fol+"\\"+val.replace(ide,"")
			os.rename(old, new)
	#pri(lis)

	"""
	<html>
	<body>
	youtube url to get mp3 from
	<form id="for" onchange="myFunction()">
	  <input type="text" id="sea" name="fname"><br>
	</form>
	y2mate url to get mp3 from generated below
	<p id="p1"></p>
	<script>
	function myFunction(){
	    var inp = document.getElementById("sea").value;
	    val = inp;
	    eqa = val.search("=");
	    sub = val.substring(eqa+1,val.length);
	    y2m = "https://www.y2mate.com/youtube/"+sub;
	    ray = [];
	    ray.push(val);
	    ray.push(eqa);
	    ray.push(sub);
	    ray.push(y2m);
	    out = "<a href=\""+y2m+"\">"+y2m+"</a>";
	    document.getElementById("p1").innerHTML =out;
	    }
	</script>
	</body>
	</html>
	"""


inp = []
y2m(inp)