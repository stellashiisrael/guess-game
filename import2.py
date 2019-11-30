import random
start = input('Please decide the random number range（starting）:')
end = input('Please decide the random number range（endging）:')
start = int(start)
end = int(end)

r = random.randint (start,end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input ('enter number please:')
	num = int(num)
	if num == r:
		print ('u are right')
		print ( 'this is the ' , count , ' times u guess ')
		break
	elif num > r:
		print ( num, ' is greater then answer ')
	elif num < r:
		print ( num ,' is smaller then answer ')
	print ( 'this is the' , count , ' times u guess ') 