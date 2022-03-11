def roman_to_integer(s):
	''' takes in a string s of roman numerals and converts it to integers
	'''
	dic = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
	return_num = 0
	i = 0
	while i <= len(s) - 1:
		if i < len(s) - 1:
			if dic[s[i]] >= dic[s[i+1]]:
				return_num += dic[s[i]]
			elif dic[s[i]] < dic[s[i+1]]:
				return_num += dic[s[i+1]] - dic[s[i]]
				i += 1
		elif i == len(s) - 1:
			return_num += dic[s[i]]
		i += 1
	return return_num
