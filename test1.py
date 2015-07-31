import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

path='http://sprout.csie.org/oj'
login_uri='/be/sign'
session=requests.Session()

def login(email,password):
    url=path+login_uri
    data={
        'reqtype':'signin',
        'mail':email,
        'pw':password,
    }
    rel=session.post(url,data=data)
    if rel.text[0]=='E':
        print 'Login Failed'
    else:
        print 'Login Successful'

def count_word(s):
    list='~`!@#$%^&*(){}[]_-+=|\\\"\'<>,.?:;/'
    s2=''
    for i in s:
        if i in list:
            s2+=' '
        else:
            s2+=i
    s_split=s2.split()
    p={}
    for i in s_split:
        p[i]=p.get(i,0)+1
    f=open("count_word.txt","w")
    for i in p:
        f.write(i+' : '+str(p[i])+'\n')
        #print i+' : '+str(p[i])
    f.close()

def get_soup(url):
    rel=session.get(url)
    rel.raise_for_status()
    return BeautifulSoup(rel.text,'html.parser')

email=''
password=''
if login(email,password):
    url='http://sprout.csie.org/oj/rate/'
    soup=get_soup(url)
    urlbe='http://sprout.csie.org/oj/be/rate'
    soup2=get_soup(urlbe)
    count_word(soup.select('body')[0].text+' '+soup2.select('tbody')[0].text)
