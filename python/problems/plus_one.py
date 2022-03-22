def plusOne(digits):
	if digits[-1] != 9:
		digits[-1] += 1
		return digits
	else:
		carry = 1
		i = len(digits) - 1
		while i >= 0:
			digits[i] += carry
			carry = (digits[i] - (digits[i] % 10))/10
			digits[i] = digits[i] % 10
			i -= 1
	if carry != 0:
		return [carry] + digits
	return digits
