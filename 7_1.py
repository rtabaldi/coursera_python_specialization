file_name = raw_input('what is your files name? ')

file_handler = open(file_name)

for word in file_handler:
	word = word.rstrip()
	print word.upper()