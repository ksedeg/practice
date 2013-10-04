def MathConst():
	dconst={"pi":3.14159265358979323846264338327950288,
		"e":2.71828182845904523536028747135266250,
		"pif":1.41421356237309504880168872420969808,
		"teod":1.73205080756887729352744634150587237,
		"delta":4.66920160910299067185320382046620161}
	s=raw_input("Please enter <constant>:<precision>: ")
	p=s.split(":")
	m=p[0]
	try:
		n=int(p[1])
	except(ValueError):
		print("Please enter correct precision")
	else:
		print("%s = %s" % (m,round(dconst[m],n)))
MathConst()
