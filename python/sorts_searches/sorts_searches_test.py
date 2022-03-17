import pytest
from merge import *
from merge_sort import *
from quicksort import *
from binary_search import *

def test_binary_search_recursive():
	''' test of a binary search recursive '''
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert binary_search_recursive(a, 0, len(a), 5) == 5
	assert binary_search_recursive(a, 0, len(a), 0) == 0
	assert binary_search_recursive(a, 0, len(a), 9) == 9
	assert binary_search_recursive(a, 0, len(a), 1) == 1
	assert binary_search_recursive(a, 0, len(a), 8) == 8
	assert binary_search_recursive(a, 0, len(a), 10) == -1


def test_quick_sort_non_integer_list():
	''' test merge of b_list without integers'''
	with pytest.raises(TypeError):
		merge_sort([1, 3, 5, [1, 2], 7, 9, 2, 4, 'B', 8, 10])

def test_quick_sort_negative():
	''' test merge of negative integers'''
	assert merge_sort([-1, 1, 3, 5, 7, 9, -2, 2, 4, 6, 8, 10]) == [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_cuick_sort_single():
	''' test merge of a single element'''
	assert merge_sort([10]) == [10]

def test_merge_b_non_integer_list():
	''' test merge of b_list without integers'''
	with pytest.raises(TypeError):
		merge([1, 3, 5, 7, 9], [2, 4, 'B', 8, 10])


def test_merge_a_non_integer_list():
	''' test merge of a_list without integers'''
	with pytest.raises(TypeError):
		merge([1, 3, 5, 'A', 9], [2, 4, 6, 8, 10])

def test_merge_miscellaneous_types():
	''' confirms our list has integers'''
	with pytest.raises(TypeError):
		merge(['a', [1, 2,], 'd'], ['t', {'test': 1}])

def test_merge_negative():
	''' test merge of negative integers'''
	assert merge([-1, 1, 3, 5, 7, 9], [-2, 2, 4, 6, 8, 10]) == [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge_b_large():
	''' test merge of a small list and a large list'''
	assert merge([1], [2, 4, 6, 8, 10]) == [1, 2, 4, 6, 8, 10]

def test_merge_a_large():
	''' test merge of a large list and a small list'''
	assert merge([1, 3, 5, 7, 9], [2]) == [1, 2, 3, 5, 7, 9]

def test_merge_equal_length():
	''' test merge of two similar length lists of integers'''
	assert merge([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge_lower_left():
	''' test the merge of two lists, left list all smaller than right list
	'''
	assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_sort_non_integer_list():
	''' test merge of b_list without integers'''
	with pytest.raises(TypeError):
		merge_sort([1, 3, 5, [1, 2], 7, 9, 2, 4, 'B', 8, 10])

def test_merge_sort_negative():
	''' test merge of negative integers'''
	assert merge_sort([-1, 1, 3, 5, 7, 9, -2, 2, 4, 6, 8, 10]) == [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge_sort_single():
	''' test merge of a single element'''
	assert merge_sort([10]) == [10]

