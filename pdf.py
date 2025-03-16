exec(open('util.py').read())
def pdf(inp):
	from PyPDF2 import PdfReader
	import pyttsx3 
	engine = pyttsx3.init()
	newVoiceRate = 120
	engine.setProperty('rate',newVoiceRate)
	#load_name = "swiss"
	#load_name = "trump-carroll"
	#load_name = "constitution"
	#load_name = "buffet"
	load_name = "missouri"
	downloads_folder = "C:\\Users\\-\\Downloads\\"
	folder_list = os.listdir(downloads_folder)
	#folder = "C:\\Users\\-\\Downloads\\"
	file =downloads_folder+load_name+".pdf"
	reader = PdfReader(file)
	pages = len(reader.pages)
	print(pages)
	check = str(pages)
	digits = len(check)
	if digits<3:
		for a in range(0,3-digits):
			check = "0"+check
	print(check)
	pdf_pages = check
	for a in range(0,pages):
		if a==0:
			if load_name not in folder_list:
				new_directory = "C:\\Users\\-\\Downloads\\"+load_name
				os.mkdir(new_directory)

		#sye()
		page_number = a+1
		digits = len(str(page_number))
		page_string = str(page_number)
		if digits<3:
			for b in range(0,3-digits):
				page_string = "0"+page_string
		ram1 = reader.pages[a]
		ram2 = ram1.extract_text()
		text = ram2
		print(text)
		print (a,pages)
		#text = text.replace("_","")
		#text = text.replace("Art.","Article")
		marker = "page "+str(page_number)+"\n"
		text = marker+marker+text
		save_name = load_name+"-"+page_string+"-"+pdf_pages
		print(save_name)		
		print("    ")
		print(save_name)
		#save_file =downloads_folder+save_name+".mp3"
		save_file =downloads_folder+load_name+"\\"+save_name+".mp3"
		#"C:\\Users\\-\\Downloads\\"+load_name
		print("page "+str(page_number)+" of "+str(pages))
		engine.save_to_file(text, save_file)
		engine.runAndWait()	

inp = []
pdf(inp)