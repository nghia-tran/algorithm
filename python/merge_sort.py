import doctest
def merge_sort(collection):
	"""
	>>> merge_sort([12,2,2,334,3,0])
	[0, 2, 2, 3, 12, 334]
	"""
	length=len(collection)
	if length > 1: 
		midpoint= length // 2 
		left_half = merge_sort(collection[:midpoint])
		right_half = merge_sort(collection[midpoint:])
		i = 0
		j = 0
		k = 0
		left_length = len(left_half)
		right_length = len(right_half)
		while i < left_length and j < right_length:
			if left_half[i] < right_half[j]:
				collection[k] = left_half[i]
				i += 1
			else:
				collection[k] = right_half[j]
				j += 1
			k += 1 
		while i < left_length:
			collection[k] = left_half[i]
			i += 1
			k += 1
		while j < right_length:
			collection[k] = right_half[j]
			j += 1 
			k += 1
	return collection 

if __name__ == '__main__':
	doctest.testmod()
	try: 
		raw_input
	except NameError: 
		raw_input = input 
	user_input = raw_input('enter numbers seperated by comma:\n').strip()
	unsorted = [int(item) for item in user_input.split(',')]
	print(merge_sort(unsorted))