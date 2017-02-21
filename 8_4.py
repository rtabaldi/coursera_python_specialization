file_name = raw_input('what is your file name? ')

file_handler = open(file_name)

lst = []

for line in file_handler:
	words = line.split()

	for word in words:
		if word in lst: continue
		lst.append(word)

lst.sort()
print lst

