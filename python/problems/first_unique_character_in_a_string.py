def firstUniqChar_inefficient(s):
	dic = {}
	seen = []
	for i in range(len(s)):
		if s[i] not in dic.keys() and s[i] not in seen:
			dic[s[i]] = i
		elif s[i] in dic.keys():
			del dic[s[i]]
			seen += [s[i]]
	if len(dic) == 0:
		return -1
	return min(dic.values())
