import urllib
import json

serviceurl =  'http://python-data.dr-chuck.net/comments_264204.json'


url = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(data)
print json.dumps(js, indent=4)

total = 0

for item in js["comments"]:
    total += item["count"]

print total