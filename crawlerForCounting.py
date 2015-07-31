import requests
from pyquery import PyQuery as pq

class SessionHandler():
	session = requests.Session()
	currentPage = pq
	specialTags = ['style','script','title']
	loginUrl = "http://zerojudge.tw/Login"
	logoutUrl = "http://zerojudge.tw/Logout"
	targetUrl = "http://zerojudge.tw/Submissions"
	loginToken = ""

	def goTo(self, url):
		resp = self.session.get(url);
		if (resp.status_code/100 != 2):
			resp.raise_for_status()
			return False
		else:
			print
			print ">>Get", url ,"successed."
			print
			self.currentPage = pq(resp.text)
			return True

	def parseLoginToken(self):
		self.loginToken = self.currentPage('input[name="token"]').attr('value')
		print ">>Token:", self.loginToken

	def login(self, username, password):
		if self.goTo(self.loginUrl):
			self.parseLoginToken()
			loginForm = {'account':username, 'passwd':password, 'returnPage':'/Index', 'token':self.loginToken}
			self.session.post(self.loginUrl, data=loginForm)
			self.goTo(self.targetUrl)

	def logout(self):
		resp = self.goTo(self.logoutUrl);

	def removeDataInSpecialTags(self):
		for tag in self.specialTags:
			self.currentPage(tag).remove()

	def showCleanedPage(self):
		self.removeDataInSpecialTags()
		print "================================================================="
		print "=== The contents after removing tags and comments             ==="
		print "===    and other data belonged to <title>, <script>, <style>. ==="
		print "================================================================="
		print self.currentPage.text()

class WordCounter():
	counter = {}
	def __init__(self, data):
		for x in data:
			if self.counter.get(x) == None:
				self.counter[x] = 1
			else :
				self.counter[x] += 1

	def showResult(self):
		print "========================="
		print "== Frequency analysis. =="
		print "========================="
		for x in filter(lambda s: s not in " \t\r\n", sorted(self.counter.keys())):
			print x + ":" + str(self.counter[x])

crawler = SessionHandler()
crawler.login("joypad","gggggg")
crawler.showCleanedPage()
counter = WordCounter(crawler.currentPage.text())
counter.showResult()
crawler.logout()
