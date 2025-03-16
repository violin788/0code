exec(open('util.py').read())
import pygetwindow as gw
import pyperclip

base_url = "https://www.reddit.com/r/__category__/submit/?type=TEXT"

windows = gw.getAllWindows()
window_names = []
future_window = ""
for window in windows:
    title = window.title
    print(title)
    if "Chrome" in title and "0reddit" not in title:
    	future_window = title
    	window.activate()

open_window(["0reddit",0])
#open_window(["0reddit",0])
hold_button(["ctrl","c",1,1])
url = base_url.replace("__category__",pyperclip.paste())
open_window([future_window,1])
hold_button(["ctrl","t",1,0])
copy_paste2([url,2])
key([["enter",1,0,0]])
open_window(["0reddit",1])
key([["right",1,0,1]])
hold_button(["ctrl","c",1,1])
open_window([future_window,3])
click_logo4(["title.png",1])
hold_button(["ctrl","v",1,1])
open_window(["0reddit",1])
key([["right",1,0,1]])
key([["right",1,0,1]])
hold_button(["ctrl","c",1,1])
open_window([future_window,3])
key([["tab",2,0,1]])
hold_button(["ctrl","v",1,1])