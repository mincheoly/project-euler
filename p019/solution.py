"""

Problem 19

"""

from datetime import datetime

if __name__ == '__main__':

	count = 0

	for year in range(1901, 2001):

		for month in range(1, 13):

			date = datetime.strptime('{} 1 {}'.format(month, year), '%m %d %Y')

			if date.weekday() == 6:

				count += 1

	print count