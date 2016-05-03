file_name = raw_input('What is the name of your file? ')
file_handler = open(file_name,'r')

counts = {}

for line in file_handler:
    if not line.startswith('From '): continue
    words = line.split()
    words = words[1]
    words = words[words.find('@')+1:len(words)]
    counts[words] = counts.get(words,0) + 1

print counts.items()
print counts
