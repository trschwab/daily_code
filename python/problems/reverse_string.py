def reverseString(s):
	for i in range(len(s) // 2):
		temp = s[i]
		s[i] = s[-(i+1)]
		s[-(i+1)] = temp
	return s
