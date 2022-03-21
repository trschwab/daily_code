def firstUniqChar(s):
	# s is going to be an ascii character..
	# we can track the frequency in a hashmap
	# populating will take O(N) time.
	# Then we read the original string. First char with value of 1 is the solution
	
	# 128 characters in ascii
	hashmap = [0] * 128
	for i in range(len(s)):
		hashmap[ord(s[i])] += 1
	for i in range(len(s)):
		if hashmap[ord(s[i])] == 1:
			return i
	return -1

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
