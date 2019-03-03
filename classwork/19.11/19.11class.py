"""
проверка на основную или импортированную:
новое требование к домашним работам

if __name__ == "__main__":
    main()


 учимся доставать тексты
 """

import urllib.request
doc = urllib.request.urlopen("http://site.com")
content = doc.read().decade("utf-8")
print (doc.info())

#ascii однобайтный метод кодирования
#еще есть cp1251

#подделывание
user_agent = "Mozilla/S.O...." #представиться браузером
req = urllib.request.Request("http://site.com", headers = {"User-Agent": user_agent})
doc = urllib.request.urlopen(req)
content = doc.read().decade("utf-8")

#регулярки
#заголовок
<title>(+?)</title>
&amp:
s = "$nbsp,"
import html
s = html.unescape(s)

#притворяемся медленным (можно поженить с random)
import time
time.sleap(2)

