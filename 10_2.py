file_name = raw_input('Enter the file name: ')
file_handler = open(file_name,'r')

counts = {}
for line in file_handler:
    if not line.startswith('From '): continue
    words = line.split()
    words = words[5]
    hour = words.split(':')
    hour = hour[0]
    counts[hour] = counts.get(hour,0) + 1

lst = []
for k,v in counts.items():
    lst.append( (k,v) )

lst.sort()

for k,v in lst:
    print k,v
