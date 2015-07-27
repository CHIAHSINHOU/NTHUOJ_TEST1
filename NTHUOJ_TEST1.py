import urllib2
from BeautifulSoup import BeautifulSoup

downloaded_data  = urllib2.urlopen('https://login.yahoo.com/')
data = downloaded_data.read()
new_file = open("data.txt","r+")
new_file.write(data)
new_file.close()

downloaded_data  = urllib2.urlopen('https://login.yahoo.com/')
soup = BeautifulSoup(downloaded_data,fromEncoding='utf-8')


words=""

#print soup.prettify()

for i in soup.findAll(attrs={'class':"Va(m) yucs-trigger:h_Td(u) Lts(n) Fz(13px)"}):
    words = words + i.text
for i in soup.findAll(attrs={'class':"mbr-login-signin-hd pure-u-1 mbr-text-align"}):
    words = words + i.text
for i in soup.findAll(attrs={'for':"persistent"}):
    words = words + i.text
for i in soup.findAll('button'):
    words = words + i.text
for i in soup.findAll(attrs={'class':"mbr-login-forgot-link pure-u-1"}):
    words = words + i.text
for i in soup.findAll(attrs={'class':"mbr-login-help-link pure-u-1"}):
    words = words + i.text
for i in soup.findAll(attrs={'class':"pure-button mbr-button-blue pure-u-1"}):
    words = words + i.text
for i in soup.findAll(attrs={'target':"_blank"}):
    words = words + i.text
for i in soup.findAll(attrs={'class':"info"}):
    words = words + i.text
print words
print len(words)

'''
for i in dir(BeautifulSoup):
    print i + '\n'
'''
