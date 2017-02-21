file_name = raw_input('what is your files name? ')

file_handler = open(file_name)

count = 0
total = 0

for word in file_handler:
	word = word.rstrip()
	if word.startswith('X-DSPAM-Confidence:'):
		count = count + 1
		word = float(word[word.find('0'):len(word)])
		total = total + word

print 'Average Spam Confidence: ',(total/count)