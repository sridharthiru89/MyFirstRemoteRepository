def add(*x):
	result = 0
	for i in x:
		result+=i
	return result


def sub(*x):
	result = 0
	for i in x:
		result-=i
	return result

  
if __name__=='__main__':
	#Below are the two test cases for the written functions
	print(add(5,10,15,0))
	print(sub(5,5,10,100))
	