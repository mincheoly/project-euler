"""

Problem 22

"""

import string
import numpy as np


letter_to_val = dict(zip(list(string.ascii_uppercase), range(1, 27)))

def compute_val(name):

	return sum(map(lambda x: letter_to_val[x], name))


if __name__ == '__main__':

	with open('p022_names.txt', 'r') as f:

		names = sorted(map(lambda x: x.strip('"'), f.readline().split(',')))

	name_scores = np.array(map(compute_val, names))

	position_scores = np.array(range(1, len(names)+1))

	print (name_scores * position_scores).sum()