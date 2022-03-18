def isPalindrome(s):
	s = s.lower()
	if len(s) == "":
		return True
	i = 0
	j = len(s) - 1
	while i < j:
		if is_valid_alphanumeric(s[i]) != True:
			i += 1
		if is_valid_alphanumeric(s[j]) != True:
			j -= 1
		if is_valid_alphanumeric(s[i]) and is_valid_alphanumeric(s[j]):
			if s[i] != s[j]:
				return False
			else:
				i += 1
				j -= 1
	return True


def is_valid_alphanumeric(c):
	''' returns True if character c is an alphanumeric character'''
	if c in "qwertyuiopasdfghjklzxcvbnm1234567890":
		return True
	return False
