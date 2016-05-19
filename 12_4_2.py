import urllib
from BeautifulSoup import *

url = raw_input('Enter url - ')
count = raw_input('Enter Count ')
position = raw_input('Enter Position ')

count = int(count)
position = int(position)
print "Retrieving: ",url


for tag in range(count):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	url = tags[position-1].get('href',None)
	print url