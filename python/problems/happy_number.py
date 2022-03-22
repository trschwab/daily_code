def isHappy(n):
	history = [n]
	add = 0
	while True:
		if n == 1:
			return True
		for i in range(len(str(n))):
			add += int(str(n)[i]) ** 2
		if add in history:
			return False
		history += [add]
		n = add
		add = 0
