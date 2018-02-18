"""

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?

"""

if __name__ == '__main__':

	n_max = 19

	factor = 9699690

	for seed in xrange(1, 1000000):

		candidate = seed * factor

		passed = True

		for divisor in range(1, n_max+1):

			if candidate % divisor != 0:

				passed = False

		if passed:

			print candidate

			break