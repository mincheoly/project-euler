"""

Problem 16

"""

import math


if __name__ == '__main__':

	print reduce(lambda x,y: x+y, map(int, list(str(long(math.pow(2, 1000))))))