import mechanize
import cookielib
import re
import urllib
from bs4 import BeautifulSoup 
import string
import time
import os
import sys

unameminn = os.popen('uname -n')
server = "localhost"
bot_name = "k1m0ch1"
fbUser = 'USER'
fbPass = 'PASSWORD'
fbPostLink = 'http://m.facebook.com/groups/599442103451298?view=permalink&id=599448356784006'

# Browser
browser = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

# Browser options
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]

response = browser.open('http://m.facebook.com/login.php')
browser.select_form(nr=0)
browser.form['email'] = fbUser
browser.form['pass'] = fbPass
response = browser.submit()

response = browser.open(fbPostLink);
browser.select_form(nr=0)
browser.form['comment_text'] = "I'm alive at " + server + " My Name is " + bot_name
response = browser.submit()

while True:
	try:
		time.sleep(1)
		reply=False

		#using If nmapscan = true 
		#	check string by target.debug if String "Nmap Done" is valid
		#	nmapscan = False when String "Nmap Done" is valid
		#	reply=True
		#	os.system("xsltproc /var/www/k1m0ch1/Report/Nmap/"+ target +".xml -o /var/www/k1m0ch1/Report/Nmap/"+target+".html")
		#	balasan= bot_name + "("+ server +"): Scanning " + target + " are done you can check html report on http://" + server + "/k1m0ch1/Report/Nmap/" + target + ".html, XML file for this scanning is http://" + server + "/k1m0ch1/Report/Nmap/" + target + ".xml, Stdout for this scanning is http://" + server + "/k1m0ch1/Report/Nmap/" + target + ".stdout"

	    response = browser.open(fbPostLink)
	    html = BeautifulSoup(response.read())
	    nyari= html.body.find_all('div', attrs={'class':'msg'})
	    terakhir = len(nyari)
	    nama = nyari[terakhir-1].find('strong', attrs={'class':'actor'})
	    isi =  string.replace(nyari[terakhir-1].text, nama.text,'')
	    print nama.text + ' : ' + isi
	    if nama.text=="Yahya Fadhlulloh Al-Fatih" or nama.text=="Wahyu Anggana" or nama.text=="Kim Jae Dinz":
			if isi.lower() == bot_name + ":hi bot":
				balasan = 'Yes Master ' + nama.text + ' Saya ' + bot_name + ' di ' + server
				reply=True
			elif isi.lower()==bot_name + ":uname -a":
				balasan = bot_name + "("+ server +"): " + os.popen('uname -a').read()
				reply=True
			elif isi.lower()==bot_name + ":who":
				balasan = bot_name + "("+ server +"): " + os.popen('who').read()
				reply=True 
			elif isi.lower()==bot_name + ":nmap:target":
				#1. parse string to get target host
				#2. run system command
				#scanning = os.popen("nmap -sV -vv -O -oX /var/www/k1m0ch1/Report/Nmap/target.xml target > /var/www/k1m0ch1/Report/Nmap/target.stdout")
				#3. nmapscan = True
				#4. balasan = bot_name + "("+ server +"): Wait for a while for nmap scanning " + target

			if reply==True:
				print "Trying to Reply"
				browser.select_form(nr=0)
				browser.form['comment_text'] = balasan
				response = browser.submit()
	except KeyboardInterrupt:
		unameminn = os.popen('uname -n')
		server = "localhost"
		bot_name = "k1m0ch1"
		fbPostLink = 'http://m.facebook.com/groups/599442103451298?view=permalink&id=599448356784006'
		response = browser.open(fbPostLink)
		browser.select_form(nr=0)
		browser.form['comment_text'] = "I'm dead at " + server
		response = browser.submit()
		sys.exit()
