"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


import math


def is_prime(x):

	if x == 1:

		return False

	if x in [2, 3, 5]:

		return True

	if x % 2 == 0:

		return False

	if x % 3 == 0:

		return False

	for i in range(5, int(math.sqrt(x))+1):

		if x % i == 0:

			return False

	return True


if __name__ == '__main__':

	primes = []

	limit = 2e6
	
	for m in range(1000000):

		for a in [1, 2, 3, 5]:

			candidate = 6*m + a

			if candidate >= limit:

				break

			if is_prime(candidate):

				primes.append(candidate)

		else:

			continue

		break

	print primes[-1]

	print reduce(lambda x,y: x+y, primes)