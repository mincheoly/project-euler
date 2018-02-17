import math
import numpy as np


if __name__ == '__main__':

	n = 100

	array = np.arange(1, n+1)

	print array.sum()**2 - np.square(array).sum()

