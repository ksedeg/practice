def SymGen():
	d = {"1" : [['','','','*','*','','',''],
		    ['','','*','*','*','','',''],
		    ['','','*','*','*','','',''],
		    ['','','','*','*','','',''],
		    ['','','','*','*','','',''],
		    ['','','','*','*','','',''],
		    ['','','*','*','*','*','',''],
		    ['','','*','*','*','*','','']],
		 "2" : [['','','','*','*','*','',''],
		['','','*','','','','*',''],
		['','*','','','','','*',''],
		['','','','','','','*',''],
		['','','','','','*','',''],
		['','','','*','*','','',''],
		['','','*','','','','',''],
		['','*','*','*','*','*','*','']],
	         "3" : [['','','*','*','*','*','',''],
		['','*','','','','','*',''],
		['','','','','','','*',''],
		['','','','','*','*','',''],
		['','','','','','*','',''],
		['','','','','','','*',''],
		['','*','','','','','*',''],
		['','','*','*','*','*','','']],
	         "5" : [['','','','*','*','*','*',''],
		['','','','*','','','',''],
		['','','*','','','','',''],
		['','','*','*','*','*','',''],
		['','','','','','*','',''],
		['','','','','','*','',''],
		['','','','','*','','',''],
		['','*','*','*','','','','']],
		 "4" : [['','','*','','','*','',''],
		['','','*','','','*','',''],
		['','','*','','','*','',''],
		['','','*','','','*','',''],
		['','','*','*','*','*','',''],
		['','','','','','*','',''],
		['','','','','','*','',''],
		['','','','','','*','','']],
		 "6" : [['','*','*','*','*','*','*',''],
		['','*','','','','','',''],
		['','*','','','','','',''],
		['','*','*','*','*','*','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','*','*','*','*','*','']],
		 "7" : [['','*','*','*','*','*','*',''],
		['','','','','','','*',''],
		['','','','','','*','',''],
		['','','','','*','','',''],
		['','','','','*','','',''],
		['','','','','*','','',''],
		['','','','','*','','',''],
		['','','','','*','','','']],
		 "8" : [['','*','*','*','*','*','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','*','*','*','*','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','*','*','*','*','*','']],
		 "9" : [['','*','*','*','*','*','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','*','*','*','*','*',''],
		['','','','','','','*',''],
		['','','','','','','*',''],
		['','','','','','','*',''],
		['','*','*','*','*','*','*','']],
		 "0" : [['','*','*','*','*','*','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','*','*','*','*','*','']]}
	n = raw_input('Enter digit: ')
	if d.has_key(n):
		for c in d[n]:
			s = ''
			for b in c:
				if b=='':
					s+=' '
				else:
					s += b
			print(s)
	else:
		print("Error. Check entered value.It must be a digit between 0 and 9.")
SymGen()