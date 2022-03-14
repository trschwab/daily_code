def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""
	prefix = strs[0]
	for i in range(1, len(strs)):
		while index_of(prefix, strs[i], 0) == False:
			prefix = prefix[:-1]
	return prefix


def index_of(a, b, n):
	''' checks to see if string a exists in string b at index n'''
	if len(a) > len(b):
		return False
	for i in range(len(a)):
		if a[i] != b[i + n]:
			return False
	return True
