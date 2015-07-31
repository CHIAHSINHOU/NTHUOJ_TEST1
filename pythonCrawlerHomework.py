import urllib,urllib2,cookielib  
import time
from HTMLParser import HTMLParser

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

dedata = ''

class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		global dedata
		dedata = dedata + data
parser = MyHTMLParser()

def pop2():  
	url_login = 'http://www.manytina.lionfree.net/final/login.php'
	body = (  
		('account','aaaaa'),  
		('password','aaaaa'))  
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))  
	#opener.addheaders = [('User-agent','Opera/10.00')]  
	urllib2.install_opener(opener)  
	req = urllib2.Request(url_login,urllib.urlencode(body))  
	u = urllib2.urlopen(req)
	url = 'http://www.manytina.lionfree.net/final/hw6.php' 
	req = urllib2.Request(url)
	string = urllib2.urlopen(req).read()
	string = string.decode('utf-8')
	parser.feed(string)
										        
if __name__ == '__main__':  
#while True:
	pop2()
time.sleep(3)
output = {}
been = 0
word = 0
for i in range(len(dedata)):
	for item in output:
		if dedata[i] == item:
			count = int(output.get(item) or 0)+1
			output[item] = count
			been = 1
	if been != 1 and dedata[i] != ' ' and dedata[i] != '\n' and dedata[i] != '\t':
		add = {dedata[i]: 1}
		output.update(add)
		word += 1
	been = 0						
for item in output:
	print item + ' '+str(output[item])
