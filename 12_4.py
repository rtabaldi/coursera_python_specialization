import urllib
from BeautifulSoup import *

url = raw_input('Enter url - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')

total = 0

for tag in tags:
	content = tag.contents[0]
	total = total + int(content)

print total