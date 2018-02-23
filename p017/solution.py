"""

Problem 17

"""

under_twenty = [
	'', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
	'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def num_to_english(num):

	if num == 1000:

		return 'one thousand'

	elif num < 20:

		return under_twenty[num]

	elif num < 100:

		return tens[int(str(num)[0])] + ' ' + under_twenty[int(str(num)[1])]

	elif num % 100 == 0:

		return under_twenty[int(str(num)[0])] + ' hundred'

	elif num < 120:

		return 'one hundred and ' + under_twenty[int(str(num)[1:])]

	elif num < 1000:

		return under_twenty[int(str(num)[0])] + ' hundred and ' + num_to_english(int(str(num)[1:]))

	else:

		print 'i just cant'
		raise Exception


if __name__ == '__main__':

	MAX_NUM = 1000

	numbers = range(1, MAX_NUM + 1)

	english = map(lambda x: x.replace(' ', ''), map(num_to_english, numbers))

	lengths = map(len, english)

	print sum(lengths)
