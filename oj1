import requests
from BeautifulSoup import BeautifulSoup
import re
url = 'http://acm.cs.nthu.edu.tw/users/login/?next=/'

def login(username,password):   
    session = requests.session()
    get = session.get(url)
    soup = BeautifulSoup(get.text,fromEncoding='utf-8')
    for i in soup.findAll('input', attrs={'name':"csrfmiddlewaretoken"}):
        print i['value']
        csrf = i['value']
    data = {'username':username,'password':password,'csrfmiddlewaretoken':csrf}
    post = session.post(url,data=data)
    if post.ok==True:
        print "Login Successful"
    else :
         print "Login Failed"
    print "If Response = 200 means everything goes well"
    print post    
    return post.text
    
def crawl_words(words):
    web_text=""
    no_comment1 = re.sub("<!--.*-->","",words)
    no_comment = re.sub("<li class=\"dropdown nav-text\".*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*li>","",no_comment1)     
    soup1 = BeautifulSoup(no_comment,fromEncoding='utf-8')
    for i in soup1.findAll('body'):
        for tag in i.findAll('script'):
            tag.extract()
        web_text = web_text+i.text   
    print "\n\nORIGINAL TEXTS:\n\n"
    print web_text
    return web_text

def countWords(text):
    counter = {}
    print "\n\nTHE TEXTS WITHOUT NUMBERS AND PUNCTUATIONS MARKS ARE:\n\n"
    other_list=' /\\\n\t\r?.,|`<>(){}[]?!@#$%^&*;:~0123456789+-*'
    s=""
    for i in text:
        if i in other_list:
            s = s + " "
        else :
            s = s + i
    print s
    for words in s.split():
        if counter.get(words) == None:
            counter[words] = 1
        else: 
            counter[words] += 1 
    print "\n\nTHE WORDS' FREQUENCIES ARE: \n\n"
    for i in sorted(counter.keys()):
        print i + " : " + str(counter[i])

words=login("SPE103062207","SPE103062207")
web_text=crawl_words(words)
countWords(web_text)
