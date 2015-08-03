# NTHUOJ_TEST1

Please use Python to login a website. Choose a page to count how many words in it.
Any HTML tags should be ignored. 


<p>
2015/8/03<br>
count the words on http://acm.cs.nthu.edu.tw/users/login/?next=/</p>

<h3>The method I use:</h3>

<p>這次是利用beautifulsoup4去抓網站資料做wordcount以及requests去做login的動作<br>
首先在function login 裏面，利用requests module get 網頁資料<br>
由於NTHUOJ需要CSRF的認証所以需要用requests.session()<br>
確保get和post的網頁裏面的csrf碼是一樣的<br>
接著去看網頁原始碼將需要post出去的資訊放在data裏面<br>
將帳密還有csrf value post 出去~~<br>
到目前為止LOGIN的動作成功了~</p>

<p>接著在function crawl_words裏面，利用re.sub()將網頁裏面一些註解的地方去除掉<br>
這部份需要利用到python的正規表示法，再來將網頁內容用bs4包起來<br>
接著對網頁內容做過慮，將body裏面的script全部去除掉</p>

<p>最後利用function countWords去做wordcount的動作就大功告成拉~</p>

<p>不足的地方：<br>
在網頁內容中有些中間沒有空白的字會變成連在一起，需要再找方法分開</p>
