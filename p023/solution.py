"""

Problem 23

"""


import math
#371115895
#298464070


def is_abundant(n):
	""" Gets all proper divisors of n. """

	divisors = set()

	for i in range(1, int(math.sqrt(n)) + 1):

		if n % i == 0:

			if i < n:

				divisors.add(i)

			if n/i < n:

				divisors.add(n/i)

	return sum(divisors) > n


if __name__ == '__main__':

	abundant_nums = [n for n in range(1, 28123+1) if is_abundant(n)]

	sum_of_abundant = set()

	for i in range(len(abundant_nums)):

		for j in range(i, len(abundant_nums)):

			sum_of_abundant.add(abundant_nums[i] + abundant_nums[j])

	not_sum_of_abundant = [n for n in range(1, 28124) if n not in sum_of_abundant]

	print sum(not_sum_of_abundant)