import pytest
from merge import *

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
