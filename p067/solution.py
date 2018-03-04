"""

Problem 67

"""

import numpy as np

if __name__ == '__main__':

	optimal_sums = []

	with open('p067_triangle.txt', 'r') as f:

		layers = [map(int, line.rstrip('\n').split(' ')) for line in f]

	for layer in layers:

		if len(layer) == 1:

			optimal = np.array(layer)

		else:

			optimal = np.zeros(len(layer))

			prev_optimal = optimal_sums[-1]

			for idx, val in enumerate(prev_optimal):

				optimal[idx] = max(val + layer[idx], optimal[idx])

				optimal[idx+1] = max(val + layer[idx+1], optimal[idx+1])

		optimal_sums.append(np.array(optimal))

	print 'Solution:', max(optimal_sums[-1])