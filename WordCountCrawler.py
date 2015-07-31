# -*- coding: utf8 -*-
import requests
from HTMLParser import HTMLParser
url = 'http://140.114.89.25/~geniusturtle/wpta_portal/'
s = requests.Session()
data = {
        'account': '102062326',
	'passwd': '102062326'
}
r = s.post(url+'login.php', data=data)
r = s.post(url+'demo.php')
r.encoding = 'utf-8'
cnt = 0
class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		global cnt
		cnt += len(data)-data.count(' ')-data.count('\n')-data.count('\t')
parser = MyHTMLParser()
parser.feed(r.text)
print cnt
