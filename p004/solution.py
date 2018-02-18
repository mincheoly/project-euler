"""

A palindromic number reads the same both ways.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

palindromes = []

def is_palindrome(x):

	if len(x) == 1:

		return True

	if len(x) == 2:

		return x[0] == x[1]

	else:

		if x[0] == x[-1]:

			return is_palindrome(x[1:-1])

		return False

if __name__  == '__main__':

	N = 1000

	for i in range(N):

		for j in range(N):

			num = i*j

			if is_palindrome(str(num)):

				palindromes.append(num)

	print max(palindromes)