def spin(array, cnt):
	return array[-1 * cnt:] + array[:-1 * cnt]


def exchange(array, first, second):
	swap = array[first]
	array[first] = array[second]
	array[second] = swap
	return array


def partner(array, first, second):
	first = array.index(first)
	second = array.index(second)
	return exchange(array, first, second)


if __name__ == "__main__":
	array = list('abcdefghijklmnop')
	for input_command in input().split(','):
		if not input_command:
			continue
	
		if input_command[0] is 's':
			target = int(input_command[1:])
			array = spin(array, target)
		elif input_command[0] is 'x':
			first, second = map(int, input_command[1:].split('/'))
			array = exchange(array, first, second)
		elif input_command[0] is 'p':
			first, second = input_command[1:].split('/')
			array = partner(array, first, second)
		else:
			raise Exception()
	print(''.join(array))
