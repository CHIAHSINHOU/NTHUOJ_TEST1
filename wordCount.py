# -*- coding: utf8 -*-
import requests
import codecs
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def wordFreqCount(mylist):
    mydict = dict()
    for ch in mylist:
        mydict[ch] = mydict.get(ch,0)+1
    return mydict

session = requests.session()
login_data = dict(account='102062304', passwd='102062304')
session.post('http://140.114.89.25/~geniusturtle/wpta_portal/login.php', data=login_data)
r = session.get('http://140.114.89.25/~geniusturtle/wpta_portal/final.php')
r.encoding = 'utf-8'
txt = strip_tags(r.text)

wordList = [ch for ch in txt]
wordCntDict = wordFreqCount(wordList)

f = codecs.open('result.txt','w','utf-8')

for key in wordCntDict:
    if(key != ' ' and key != '\t' and key != u'　'):
        f.write(key)
        f.write(" = ")
        f.write(str(wordCntDict[key]) + "\n")
