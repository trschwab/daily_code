import pytest
from fibonacci import *
from steps import *
from min_cost_stairs import *
from palindrome_integers import *
from roman_to_integer import *

def test_roman_to_integers():
	''' test roman to integers '''
	assert roman_to_integer('III') == 3
	assert roman_to_integer('CM') == 900
	assert roman_to_integer('I') == 1
	assert roman_to_integer('IV') == 4
	assert roman_to_integer('MCMXCIV') == 1994
	assert roman_to_integer('LVIII') == 58
	

def test_palindrome_integers():
	''' test palindrom integers'''
	assert palindrome_integers(1) == True
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
