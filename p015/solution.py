"""

Problem 15

"""

from scipy.misc import comb


NUM_BLOCKS = 20

GRID_SIZE = NUM_BLOCKS + 1


# Depth first search is too slow, but good exercise
def traverse(row, col):

	if row + 1 <= GRID_SIZE  - 1 and col + 1 <= GRID_SIZE - 1:

		return traverse(row+1, col) + traverse(row, col+1)

	elif row + 1 > GRID_SIZE - 1 and col + 1 <= GRID_SIZE - 1:

		return traverse(row, col+1)

	elif row + 1<= GRID_SIZE  - 1 and col + 1 > GRID_SIZE - 1:

		return traverse(row+1, col)

	else:

		return 1

if __name__ == '__main__':

	print 'size:', NUM_BLOCKS

	print int(comb(NUM_BLOCKS*2, NUM_BLOCKS))