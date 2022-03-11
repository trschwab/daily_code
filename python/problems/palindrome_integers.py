def palindrome_integers(x):
	if x == 0:
		return True
	if x < 0 or x % 10 == 0 :
		return False

	reverse = 0
	while (x > reverse):
		pop = x % 10
		x = x // 10
		reverse = (reverse * 10) + pop

	if x == reverse or x == reverse // 10:
		return True

	return False
