"""

Pythagorean triplet.


"""

import sys

def is_pythagorean_triplet(a, b, c):

	return a**2 + b**2 == c**2

if __name__ == '__main__':

	for a in range(0, 400):

		for b in range(a+1, 400):

			c = 1000 - a - b

			if is_pythagorean_triplet(a, b, c):

				print 'a:', a
				print 'b:', b
				print 'c:', c

				print 'a^2 + b^2:', a**2 + b**2
				print 'c^2:', c**2

				print 'a*b*c:', a*b*c

				sys.exit(0)



