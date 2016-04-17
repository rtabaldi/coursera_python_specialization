hours = raw_input("How many hours did you work?: ")
float_hours = float(hours)

pay_rate = 10.5

overtime_rate = 1.5 * pay_rate

if float_hours > 40:
	ot = float_hours - 40
	print "You made",(pay_rate * 40) + (ot * overtime_rate)
else:
	print "You made",pay_rate * float_hours