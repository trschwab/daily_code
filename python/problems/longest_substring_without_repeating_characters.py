def lengthOfLongestSubstring(s):
	i = 0
	left = 0
	dic = {}
	top_length = 0
	while i <= len(s)-1:
		if s[i] in dic:
			while s[i] in dic.keys():
				if len(dic) > top_length:
					top_length = len(dic)
				del dic[s[left]]
				left += 1
			dic[s[i]] = i
			i += 1
		else:
			dic[s[i]] = i
			i += 1
			if len(dic) > top_length:
				top_length = len(dic)
	if top_length == 0 and len(s) > 0:
		return len(s)
	return top_length
