"""

Problem 60

"""


import itertools
import math


MAX_ELEM = 500


def is_prime(n):

	for i in range(2, int(math.sqrt(n)) + 1):

		if n % i == 0:

			return False

	return True



if __name__ == '__main__':


	primes = [i for i in range(1, MAX_ELEM) if is_prime(i)]

	groups = itertools.combinations(primes, 5)

	print len(list(groups))