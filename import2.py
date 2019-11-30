import random
r = random.randint (1,100)
count = 0
while True:
	count += 1 # count = count + 1
	p = input ('enter number please:')
	p = int(p)
	if p == r:
		print ('u are right')
		print ( 'this is the ' , count , ' times u guess ')
		break
	elif p > r:
		print ( ' greater then answer ')
	elif p < r:
		print ( ' smaller then answer ')
	print ( 'this is the' , count , ' times u guess ') 