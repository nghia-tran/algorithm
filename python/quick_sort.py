#!/bin/python
import doctest

def quick_sort(array):
	"""
	quick_sort 
	>>> quick_sort([1,2,3,2352,2342])
	[1, 2, 3, 2342, 2352]
	>>> quick_sort([12,2323,3,2352,2342])
	[3, 12, 2323, 2342, 2352]
	"""
	array_length = len(array)
	if array_length <= 1:
		return array
	else:
		pivot = array[0]
		lesser = [element for element in array[1:] if element <= pivot]
		greater = [element for element in array[1:] if element > pivot]
	return quick_sort(lesser) + [pivot] + quick_sort(greater)
	
if __name__ == '__main__':
	doctest.testmod()
