hours = raw_input("How many hours did you work?: ")
float_hours = float(hours)

rate = raw_input("How much do you make an hour?: ")
float_rate = float(rate)

def computepay(h,r):
	overtime_rate = 1.5 * r	
	if h > 40:
		ot = h - 40
		return (r * 40) + (ot * overtime_rate)
	else:
		return h * r

pay = computepay(float_hours,float_rate)

print pay