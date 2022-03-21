def isAnagram(s, t):
	# I will use a O(N) time and O(N) space solution
	# There is a solution I can think of that may use O(N) time and O(1) space..
	# TODO to code out that more space efficient solution
	# That solution would be to binary search for element t[i] in s
	# upon finding it, remove that index from s then move on to the next i
	freq = {}
	for i in range(len(s)):
		if s[i] in freq.keys():
			freq[s[i]] += 1
		else:
			freq[s[i]] = 1
	for i in range(len(t)):
		if t[i] not in freq.keys():
			return False
		else:
			if freq[t[i]] == 1:
				del freq[t[i]]
			else:
				freq[t[i]] -= 1
	if len(freq) == 0:
		return True
	return False
