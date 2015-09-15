# -*- coding: utf-8 -*-
import urllib,urllib2,cookielib  
import time
from HTMLParser import HTMLParser
#deflaut
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

output = {}
#post & decode data 
def pop2():  
    url_login = 'http://140.114.89.25/~geniusturtle/wpta_portal/login.php'
    body = (  
        ('account','102062110'),  
        ('passwd','102062110'))  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))  
    urllib2.install_opener(opener)  
    req = urllib2.Request(url_login,urllib.urlencode(body))  
    u = urllib2.urlopen(req)
    url = 'http://140.114.89.25/~geniusturtle/wpta_portal/grade.php' 
    req = urllib2.Request(url)
    ori_data = urllib2.urlopen(req).read()
    ori_data = ori_data.decode('utf-8')
    parser.feed(ori_data)

#split html tag
en_data = ''
zh_data = ''
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        for c in data:
            if is_zh(c) == True:
                global zh_data
                zh_data = zh_data + c
            else:
                global en_data
                en_data = en_data + c
parser = MyHTMLParser()

#check is en & zh
def is_zh (c):
    x = ord (c)
    # Punct & Radicals
    if x >= 0x2e80 and x <= 0x33ff:
        return True
    elif x >= 0xff00 and x <= 0xffef:
        return True
    elif x >= 0x4e00 and x <= 0x9fbb:
        return True
    elif x >= 0xf900 and x <= 0xfad9:
        return True
    elif x >= 0x20000 and x <= 0x2a6d6:
        return True
    elif x >= 0x2f800 and x <= 0x2fa1d:
        return True
    else:
        return False

#word count
def count_word(string):
    been = 0
    word = 0
    if bo_zh == False:#only en need to split
        string = string.replace('\n',' ')
        string = string.replace('\t',' ')
        temp = string.split(' ')
    else:
        temp = string# if zh temp is string ,or dict
    for key in temp:
        for item in output:
            if key == item:
                count = int(output.get(item) or 0)+1
                output[item] = count
                been = 1
        if been != 1 and key != ' ' and key != '\n' and key != '\t' and key != '':
            add = {key: 1}
            output.update(add)
            word += 1
        been = 0
if __name__ == '__main__':  
    #while True:
    pop2()
time.sleep(3)

bo_zh = True
count_word(zh_data)
bo_zh = False
count_word(en_data)

#print 
for item in output:
    print '[' + item + ']' + ' : '+str(output[item]) 
    