exec(open('util.py').read())
def rumble_get_rumble_codes(inp):
	
	base_text = "array = []\narray.append(\""
	start_file(["rumble_codes.txt",1])
	copy_paste2([base_text,1])

	#cf(["monetized"])
	#key([["enter",1,1,1]])

	for a in range(0,10):
		how_many_clicks = a
		alt_win81(["All Videos",1])
		cf(["unique views"])
		key([["enter",how_many_clicks,0,1]])
		key([["esc",1,0,1]])
		hold_button(["shift","tab",1,1])
		hold_button(["shift","f10",1,1])
		key([["up",2,0,1]])
		key([["enter",1,0,1]])
		start_file(["rumble_codes.txt",1])
		hold_button(["ctrl","v",1,1])
		copy_paste2(["\",\"",1])
		alt_win81(["All Videos",1])
		#copy_paste2(["paperclip",2])

		cf(["unique views"])
		key([["enter",how_many_clicks,0,1]])
		key([["esc",1,0,1]])
		key([["tab",1,0,1]])
		key([["enter",1,0,1]])
		key([["tab",4,0,1]])
		key([["enter",1,0,1]])
		click_logo4(["iframe_url_logo.png",1])
		key([["tab",1,1,1]])
		hold_button(["ctrl","c",1,1])
		click_logo4(["close2.png",1])
		start_file(["rumble_codes.txt",1])
		hold_button(["ctrl","v",1,1])
		copy_paste2(["\")\narray.append(\"",1])
		alt_win81(["All Videos",1])
	
inp = []
rumble_get_rumble_codes(inp)

"""
https://rumble.com/embed/v4spnbx/?pub=3i4h9q
https://rumble.com/embed/v4qvth5/?pub=3i4h9q
https://rumble.com/embed/v4rayvc/?pub=3i4h9q
https://rumble.com/embed/v4r928i/?pub=3i4h9q
https://rumble.com/embed/v4r4lq6/?pub=3i4h9q
https://rumble.com/embed/v4r43g9/?pub=3i4h9q
https://rumble.com/embed/v4qvtai/?pub=3i4h9q
https://rumble.com/embed/v4qyb7l/?pub=3i4h9q
"""