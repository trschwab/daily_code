# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
# The earliest known reference to the sieve is in Nicomachus of Gerasa's Introduction to Arithmetic, an early 2nd cent. CE book, which describes it and attributes it to Eratosthenes of Cyrene, a 3rd cent. BCE Greek mathematician.


def sieve(n):
	''' calculates prime numbers up to n '''
	l = list(range(n+1))
	i = 2
	j_multiple = 2
	while i <= n:
		if l[i] == False:
			i += 1
		else:
			j = i
			while j*j_multiple <= n:
				l[j*j_multiple] = False
				j_multiple += 1
			j_multiple = 2
			i += 1
	return l

def sieve_prime_only(n):
	l = sieve(n)
	r_list = []
	for i in range(2, len(l)):
		if l[i] != False:
			r_list += [l[i]]
	return r_list

#print(sieve(100))
#print(sieve_prime_only(100))
