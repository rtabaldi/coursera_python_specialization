	file_name = raw_input('what is the file name? ')

file_handler = open(file_name,'r')

count = []

for line in file_handler:
	if not line.startswith('From '): continue
	words = line.split()
	count.append(words)
	print words[1]

print "There were",len(count),"lines in the file with From"\
" as the first word"
