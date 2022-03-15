def strStr(haystack, needle):
	if needle == "":
		return 0
	if len(needle) > len(haystack):
		return -1
	i = 0
	j = len(needle)
	while j <= len(haystack):
		if haystack[i:j] == needle:
			return i
		i += 1
		j += 1
	if j == len(haystack) and needle in haystack:
		return 0
	return -1
