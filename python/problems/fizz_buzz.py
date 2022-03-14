def fizzBuzz(n):
	r_list = [0] * n
	for i in range(1,len(r_list)+1):
		if i % 3 == 0 and i % 5 == 0:
			r_list[i-1] = "FizzBuzz"
		elif i % 3 ==0:
			r_list[i-1] = "Fizz"
		elif i % 5 == 0:
			r_list[i-1] = "Buzz"
		else:
			r_list[i-1] = str(i) #'"' + str(i) + '"'
	return r_list
            
