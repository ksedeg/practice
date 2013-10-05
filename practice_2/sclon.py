def sclon(m, n):
	if isinstance(m, dict):
		i = 0
		while i < 21:
			if i==1:
				m[i]='chas'
			elif i>1 and i<5:
				m[i]='chasa'
			elif (i>=5 and i<21) or (i == 0):
				m[i]='chasov'
			i+=1
		print("%s %s" % (n, m[n%20]))
	else:
		print("Error: Type must be dict")

import re
m = {}
s=""
while True:
	s = raw_input('To quit enter q. Enter number: ')
	if re.match('[0-9]+',s) is not None:
		n = int(s)
		sclon(m, n)
	elif s=='q':break; 
	else: print('Try again.')

