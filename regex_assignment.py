import re

open_file = raw_input('What is the name of your file? ')

file_handler = open(open_file,'r')

total = 0

for line in file_handler:
	line = line.rstrip()
	number = re.findall('[0-9]+', line)
	for num in number:
		total = total + int(num)

print total
