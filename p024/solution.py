"""

Problem 24

"""


import itertools


if __name__ == '__main__':

	all_perms = sorted(map(lambda x: ''.join(x), itertools.permutations('0123456789', 10)))

	print all_perms[1000000-1]