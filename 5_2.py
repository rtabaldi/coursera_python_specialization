largest = None
smallest = None

num_list = []

while True:
	num = raw_input("Enter a number and hit enter.  When are you finished entering numbers type done: ")
	if num == 'done':
		break
	else:
		try:
			num = int(num)
		except:
			print "Invalid input.  Enter a number"
			continue
		num_list.append(num)

print num_list


for n in num_list:
	if smallest is None:
		smallest = n
	elif n < smallest:
		smallest = n
	
print "The smallest number is ", smallest

for i in num_list:
	if largest is None:
		largest = i
	elif i > largest:
		largest = i

print "The largest number is ", largest
