"""

Problem 25

"""

if __name__ == '__main__':


	seq = [1, 1]

	while len(str(seq[-1])) < 1000:

		seq.append(seq[-1] + seq[-2])

	print seq

	print len(seq)
