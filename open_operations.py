exec(open('util.py').read())

storage = []

new = []
new.append("drive")
new.append("https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ec=asw-drive-hero-goto&ifkv=AS5LTARnSfrrHGENO20pgrR0B1yuSXJC1173OOwXpjxD2p2G3O-rTgg8Vk66Rlan5Eykn2JfO8Oc0g&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S823815728%3A1717671124532768&ddm=0")
username = "media788788"
password = "Medmed1!"
chrome_operations = []
firefox_operations = []
chrome_operations.append([key,[["esc",1,0,0]]])
chrome_operations.append([copy_paste2,[username,1]])
chrome_operations.append([key,[["esc",1,0,1]]])
chrome_operations.append([key,[["enter",1,0,5]]])
chrome_operations.append([key,[["esc",1,0,0]]])
chrome_operations.append([copy_paste2,[password,1]])
chrome_operations.append([key,[["esc",1,0,1]]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([key,[["esc",1,0,0]]])
firefox_operations.append([copy_paste2,[username,1]])
firefox_operations.append([key,[["esc",1,0,1]]])
firefox_operations.append([key,[["enter",1,0,5]]])
firefox_operations.append([key,[["esc",1,0,1]]])
firefox_operations.append([copy_paste2,[password,1]])
firefox_operations.append([key,[["esc",1,0,1]]])
firefox_operations.append([key,[["enter",1,0,0]]])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("logins")
new.append("https://docs.google.com/spreadsheets/d/1pveuTlsMCB5vKhEhwBA28IidJPkOokVk/edit#gid=1983355307")
chrome_operations = []
firefox_operations = []
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("reddit_questions")
new.append("https://docs.google.com/spreadsheets/d/1qrySuja-rx_LoHcXIoLAidd1C92hqyeouNv2O7iWnDs/edit#gid=0")
chrome_operations = []
firefox_operations = []
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("keep")
new.append("https://keep.google.com/")
chrome_operations = []
firefox_operations = []
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("speechnotes")
new.append("https://speechnotes.co/dictate/")
chrome_operations = []
firefox_operations = []
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("gmail")
#new.append("https://mail.google.com/mail/u/0/#inbox")
new.append("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AdF4I75ybEdiK7zROzr_cSPPgqOFWABKFP7-CgtueOuHzOL4af7IEBQzlZE0ymwe-kDBtLwGmH4OyA&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S2132006666%3A1722880415399812&ddm=0")
chrome_operations = []
firefox_operations = []
chrome_operations.append([hold_button,["alt","d",1,1]])
chrome_operations.append([copy_paste2,["gmail.com",1]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([hold_button,["alt","d",1,1]])
firefox_operations.append([copy_paste2,["gmail.com",1]])
firefox_operations.append([key,[["enter",1,0,0]]])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("protonmail")
new.append("https://account.proton.me/mail")
username = "violin78"
password = "viovio"
chrome_operations = []
firefox_operations = []
chrome_operations.append([copy_paste2,[username,1]])
chrome_operations.append([key,[["tab",1,0,0]]])
chrome_operations.append([copy_paste2,[password,0]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([copy_paste2,[username,1]])
firefox_operations.append([key,[["tab",1,0,0]]])
firefox_operations.append([copy_paste2,[password,0]])
firefox_operations.append([key,[["enter",1,0,0]]])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("reddit_new_notifications")
new.append("https://www.reddit.com/notifications")

"""
old login info
username = "desk246"
password = "desk1234"

current login info
email registered = davidssonbob@gmail.com
email pw = Davdav1!
"""
username = "CIA7788"
password = "mustang1"

chrome_operations = []
firefox_operations = []
#chrome_operations.append([copy_paste2,[username,1]])
chrome_operations.append([cf_et_new,["username",1,1,1]])
chrome_operations.append([copy_paste2,[username,1]])
#chrome_operations.append([copy_paste2,[username,1]])
chrome_operations.append([key,[["tab",1,0,0]]])
chrome_operations.append([copy_paste2,[password,1]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("reddit_old_notifications")
#https://old.reddit.com/login/
new.append("https://old.reddit.com/message/unread/")
chrome_operations = []
firefox_operations = []
chrome_operations.append([hold_button,["ctrl","r",1,1]])
#chrome_operations.append([key,[["enter",1,0,5]]])
#chrome_operations.append([copy_paste2,["Medmed1!",1]])
#chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("twitter_login")
new.append("https://twitter.com/i/flow/login")
chrome_operations = []
firefox_operations = []
chrome_operations.append([sle,[3]])
chrome_operations.append([cf_et_new,["apple",1,1,1]])
#chrome_operations.append([key,[["esc",1,0,1]]])
#chrome_operations.append([hold_button,["shift","tab",1,1]])
chrome_operations.append([copy_paste2,["oversight333",1]])
chrome_operations.append([key,[["enter",1,0,2]]])
chrome_operations.append([copy_paste2,["Oveove1!",1]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("messenger")
new.append("https://www.messenger.com")
chrome_operations = []
firefox_operations = []
#chrome_operations.append([copy_paste2,[username,1]])
chrome_operations.append([key,[["tab",6,0,1]]])
chrome_operations.append([copy_paste2,["violin78@protonmail.com",1]])
chrome_operations.append([key,[["tab",1,0,0]]])
chrome_operations.append([copy_paste2,["Viovio1!",1]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("chatgpt")
new.append("https://chatgpt.com/")
chrome_operations = []
firefox_operations = []
#chrome_operations.append([copy_paste2,[username,1]])
#chrome_operations.append([key,[["enter",1,0,5]]])
#chrome_operations.append([copy_paste2,["Medmed1!",1]])
#chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("atl")
new.append("https://www.atlanticunionbanksecure.com/dbank/live/app/login/consumer")
chrome_operations = []
firefox_operations = []
chrome_operations.append([cf_et_new,["username",1,1,1]])
chrome_operations.append([copy_paste2,["atlatl",1]])
chrome_operations.append([key,[["tab",2,0,1]]])
chrome_operations.append([copy_paste2,["Medmed1!",1]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

new = []
new.append("lowes")
new.append("https://www.lowes.com/u/login/oauth2/authorize?redirect_uri=https%3A%2F%2Fwww.lowes.com%2Fu%2Flogin%2Foauth2%2Fpostauthorize&scope=general-digital-access&client_id=loweswebclient&state=NExMekhzOFQ4azd4WFo1ejQ4RVlyTTJiQ0gyM0gxVW85RWVId0t5ZEcwMUh3eU1GZW55Q1Y5Z3FuV1NCNEwySw%3D%3D&code_challenge=-97sXjLwWq_WGP6TegZLkMwmS8HzF0JtzvkL8QJRHE0&code_challenge_method=S256&redirect=https%3A%2F%2Fwww.lowes.com%2Fcart")
chrome_operations = []
firefox_operations = []
chrome_operations.append([cf_et_new,["lowe's",1,1,1]])
chrome_operations.append([copy_paste2,["media788788@gmail.com",1]])
chrome_operations.append([key,[["tab",1,0,1]]])
chrome_operations.append([copy_paste2,["Medmed1!",1]])
chrome_operations.append([key,[["enter",1,0,0]]])
firefox_operations.append([])
new.append(chrome_operations)
new.append(firefox_operations)
storage.append(new)

storage.sort()