import pytest
from fibonacci import *
from steps import *
from min_cost_stairs import *
from palindrome_integers import *

def test_palindrome_integers():
	''' test palindrom integers'''
	assert palindrome_integers(1) == False
	assert palindrome_integers(10) == False
	assert palindrome_integers(-1) == False
	assert palindrome_integers(-121) == False
	assert palindrome_integers(121) == True
	assert palindrome_integers(123454321) == True
	assert palindrome_integers(1298558921) == True

def test_fib():
	''' test fibonacci'''
	assert fib_memo(1) == 0
	assert fib_memo(5) == 3
	assert fib_memo(10) == 34
	assert fib_memo(101) == 354224848179261915075

def test_steps():
	''' testing steps '''
	assert steps(5) == 8
	assert steps(13) == 377

def test_min_cost_stairs():
	''' testing steps '''
	assert min_cost_stairs([10, 15, 20]) == 15
	assert min_cost_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
