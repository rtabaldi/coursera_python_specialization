score = raw_input("Enter your test score: ")

try:
	float_score = float(score)
except:
	float_score = -1

if float_score > 0:
	if float_score < .6:
		print "F"
	elif float_score < .7:
		print "D"
	elif float_score < .8:
		print "C"
	elif float_score < .9:
		print "B"
	elif float_score <= 1:
		print "A"
	else:
		print "This number is out of range, please try again"
else:
	print "This is not a number"

#comment