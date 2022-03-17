def asteroidCollision(asteroids):
	stack = []
	i = 0
	while i < len(asteroids):
		if asteroids[i] > 0:
			stack.append(asteroids[i])
			i += 1
		elif len(stack) != 0 and stack[-1] > 0 and asteroids[i] < 0:
			if (asteroids[i] * -1) < stack[-1]:
				i += 1
			elif (asteroids[i] * -1) == stack[-1]:
				stack.pop()
				i += 1
			elif (asteroids[i] * -1) > stack[-1]:
				x = stack.pop()
		else:
			stack.append(asteroids[i])
			i += 1
	return stack
