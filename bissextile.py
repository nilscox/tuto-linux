r = "est bissextile"
w = "n'est pas bissextile"

def b(a):


	if a % 4 == 0 and a % 100 != 0:
			print(a, r)

	elif a % 400 == 0 :
			print(a, r)

	else:
		print(a, w)


b(2009)
b(2092)
b(2042)
b(2012)
