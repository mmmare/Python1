
while True:
	try:
		numbers = input('please enter values seperated by a space ').split()
		addval = sum([int(number)for number in numbers])
		addval = int(addval)
		average = addval/len(numbers)
		intva = int(numbers)
		median = sorted(intva)
		print("The mean is",average)
		
		if len(numbers)%2 == 0: 
			evenval = int(len(numbers)/2)
			evenRange = int(median[evenval])
			lowevenRange = int(median[evenval]) -1 
			print("The median is",(lowevenRange + evenRange)/2)
		else:
			oddvalueval = ((len(numbers))/2)
			print(median)
			print(median)
			oddRange = oddvalueval-.5
			intoddrange = int(oddRange)
			oddmedian = int(median[intoddrange])
		 print("The median is", oddmedian) 
		break
	except ValueError:
		print("please enter integers")

