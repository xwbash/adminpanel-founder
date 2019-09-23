#admin panel
import requests
import os
import time
def clst():
	try:
		os.system("cls")
	except:
		os.system("clear")
def me():
	print("""
	script created by bash.
	instagram: yigitaydn.py
		""")
clst()
me()
panels = open("admin.txt","r")
panel = []
panels = panels.read().splitlines()
for i in panels:
	panel.append(i)
website = input("~# input the website.: ")
headers = requests.utils.default_headers()
headerz = open("headers.txt","r")
for i in headerz:
	headers.update({"User-Agent":i})
headerz.close()
w = 0
while True:
	time.sleep(2) #dont remove this the web site can be block you.
	try:
		site = website+"/"+panel[w]
		r = requests.get(site)
		if r.status_code == 200:
			clst()
			print("[+] admin panel founded.: "+site)
			me()
			break
		else:
			w += 1
	except IndexError:
		clst()
		print("[-] we cannot find the admin panel.")
		break