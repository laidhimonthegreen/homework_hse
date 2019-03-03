from bs4 import BeautifulSoup
import urllib.request

doc = urllib.request.urlopen("https://chrdk.ru/other/sygrat_v_evolyuciyu")
content = doc.read().decode("utf-8")
print (content)


soup = BeautifulSoup(content, 'html.parser')
lines = soup.get_text().split("\n")
counter = 0
lengths = []
for n in lines:
    print (len(n), counter)
    lengths = lengths.append(len(n))
    counter += 1

print (lengths)


"""
cleantext = BeautifulSoup(content, "lxml").text
"""



