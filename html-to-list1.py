#html-to-list1.py
import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = str(response.read().decode('UTF-8'))
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)

print(wordlist)