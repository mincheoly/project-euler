"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""




if __name__ == '__main__':

	N = 600851475143

	remainder = N

	factors = []

	while True:

		for i in xrange(2, remainder):

			if remainder % i == 0:

				remainder = remainder / i

				factors.append(i)

				break

		if i == remainder-1:

			factors.append(remainder)

			break

	print max(factors)
