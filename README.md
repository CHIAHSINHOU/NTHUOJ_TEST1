# NTHUOJ_TEST1

Please use Python to login a website. Choose a page to count how many words in it.
Any HTML tags should be ignored. 
<p>
登入網站:http://sprout.csie.org/oj/rate/<br>
我使用 Requests module 的 Session 去 修改 cookie 做登入<br>
使用 BeautifulSoup module 去解析HTML文字的部分<br>
再開一個map紀錄文字出現次數並輸出<br>
還有因為他是用js去資料庫裡抓網頁的，所以真正的網頁資料存在http://sprout.csie.org/oj/be/rate
</p>
