import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_264200.xml'

address = raw_input('Enter location ')

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print "Count:", len(counts)


totalSum = 0
for num in counts:
	totalSum += int(num.text)

print totalSum



