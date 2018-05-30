#!/bin/python

def quick_sort(array):
	array_length = len(array)
	if array_length <= 1:
		return array
	else:
		pivot = array[0]
		lesser = [element for element in array[1:] if element <= pivot]
		greater = [element for element in array[1:] if element > pivot]
	return quick_sort(lesser) + [pivot] + quick_sort(greater)
	
if __name__ == '__main__':
	try:
		raw_input
	except NameError:  
		raw_input  = input
	user_input = raw_input("please enter numbers seperated by comma\n").strip()
	unsorted = [int(item) for item in user_input.split(',')]
	print(quick_sort(unsorted))
		