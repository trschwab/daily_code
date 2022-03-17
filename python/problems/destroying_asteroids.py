def asteroidsDestroyed(mass, asteroids):
	asteroids.sort()
	i = 0
	while i < len(asteroids):
		if mass >= asteroids[i]:
			mass += asteroids[i]
		else:
			return False
		i += 1
	return True
