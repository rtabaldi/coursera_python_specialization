file_name = raw_input('What is the name of your file? ')
file_handler = open(file_name,'r')

counts= {}

for line in file_handler:
    if not line.startswith('From '): continue
    words = line.split()
    words = words[1]
    counts[words] = counts.get(words,0) + 1


bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount
