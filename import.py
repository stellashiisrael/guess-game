import random
r = random.randint (1,100)

while True:
	p = input ('enter number please:')
	p = int(p)
	if p == r:
		print ('u are right')
		break
	elif p != r and p > r:
			print ('p','greater then answer')	
	elif p < r:
			print ('p','smaller then answer')