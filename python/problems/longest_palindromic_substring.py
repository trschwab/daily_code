def longestPalindrome(s):
	if len(s) == 1:
		return s[0]
	longest = ""
	for i in range(len(s)):
		# odd
		j = i
		k = i
		while j >= 0 and k < len(s):
			if s[j] == s[k]:
				if len(s[j:k+1]) > len(longest):
					longest = s[j:k+1]
				j -= 1
				k += 1
			else:
				j = -1
		j = i
		k = i + 1
		while j >= 0 and k < len(s):
			if s[j] == s[k]:
				if len(s[j:k+1]) > len(longest):
					longest = s[j:k+1]
				j -= 1
				k += 1
			else:
				j = -1
	return longest
