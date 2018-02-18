import time
import math

def is_prime(x):

	if x % 2 == 0:

		return False

	if x % 3 == 0:

		return False

	for i in range(3,int(math.sqrt(x))+1):

		if x % i == 0:

			return False

	return True



if __name__ == '__main__':

	start = time.time()

	desired_order = 10001

	idx = 5

	prime_count = 3

	while True:

		idx += 1

		if is_prime(idx):

			print idx

			prime_count += 1

			if prime_count == desired_order:

				print time.time()-start

				break

