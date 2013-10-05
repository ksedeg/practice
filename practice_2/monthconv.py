def MonthConv():
	dmonth={"january":1,"february":2,"march":3,"april":4,"may":5, "june":6,
		"july":7, "august":8, "september":9, "october":10, 
		"november":11, "december":12}
	m=raw_input("Please, enter month: ")
	m=m.lower()
	if dmonth.has_key(m)==True:
		print("Month number: %s" %dmonth[m])
	else:
		print("Error!Please check the entered value.")
MonthConv()
