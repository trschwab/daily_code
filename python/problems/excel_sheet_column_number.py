def titleToNumber(columnTitle):
	add = 0
	i = len(columnTitle) - 1
	x = 0
	while i >= 0:
		add += (26 ** x) * (ord(columnTitle[i]) - ord('A') + 1)
		x += 1
		i -= 1
	return add
