""" 

Problem 14

"""


import time


def generate_collatz(x):

	current = x

	count = 1

	while current != 1:

		if current % 2 == 0:

			current = current /2

		else:

			current = 3*current + 1

		count += 1

	return count


if __name__ == '__main__':

	start = time.time()

	max_ind = 1

	running_max = 0

	for i in range(1,1000000):

		collatz_count = generate_collatz(i)

		if collatz_count > running_max:

			running_max = collatz_count

			max_ind = i

	print time.time() - start

	print running_max

	print max_ind