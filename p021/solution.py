"""

Problem 21

"""


import math


def sum_proper_divisors(n):
	""" Gets all proper divisors of n. """

	divisors = set()


	for i in range(1, int(math.sqrt(n)) + 1):

		if n % i == 0:

			if i < n:

				divisors.add(i)

			if n/i < n:

				divisors.add(n/i)

	return sum(divisors)


if __name__ == '__main__':

	amicable_nums = set()

	for a in range(1, 10000):

		b = sum_proper_divisors(a)

		if a == sum_proper_divisors(b) and a != b:

			print a, b

			if a < 10000:

				amicable_nums.add(a)

			if b < 10000:

				amicable_nums.add(b)

	print sorted(list(amicable_nums))

	print sum(amicable_nums)

