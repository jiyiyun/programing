def fibs(n):
	"""
	This is Fibonacci Sequence
	"""
	result = [0,1]
	for i in range(n-2):
		result.append(result[-2] + result[-1])
	return result

a = int(input("Please input a int number\n"))
print("The febonacci squence of %d is \n" %a)
print( fibs(a),"\n")