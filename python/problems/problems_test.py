import pytest
from fibonacci import *
from steps import *
from min_cost_stairs import *
from palindrome_integers import *
from roman_to_integer import *
from two_sum import two_sum
from add_two_numbers import *
from two_sum_IV import *
from range_sum_of_bst import *
from fizz_buzz import *
from valid_parentheses import *

def test_isValidParentheses():
	''' test isValidParentheses '''
	assert isValidParentheses("()") == True
	assert isValidParentheses("()[]{}") == True
	assert isValidParentheses("(]") == False
	assert isValidParentheses("({})") == True
	assert isValidParentheses("]") == False

def test_fizzBuzz():
	''' test fizzBuzz'''
	assert fizzBuzz(3) == ["1","2","Fizz"]
	assert fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
	assert fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

def test_range_sum_of_bst():
	''' test range_sum_of_bst '''
	low = 7
	high = 15
	a = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
	b = Solution_range_sum_of_bst()
	assert b.rangeSumBST(a, low, high) == 32

def test_two_sum_iv():
	''' test two sum IV'''
	a = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
	b = Solution_two_sum_IV()
	assert b.findTarget(a, 5) == True

def test_add_two_numbers():
	''' test add two numbers '''
	a = sll_node(2, sll_node(4, sll_node(3)))
	b = sll_node(5, sll_node(6, sll_node(4)))
	c = sll_node(7, sll_node(0, sll_node(8)))
	assert compare_sll(add_two_numbers(a, b), c)

def compare_sll(a, b):
	while a and b:
		print(a.val)
		print(b.val)
		if a.val != b.val:
			return False
		a = a.next_node
		b = b.next_node
	return True

def test_two_sum():
	''' test two sum '''
	assert two_sum([2, 7, 11, 15] ,9) == [0, 1]
	assert two_sum([3, 2, 4], 6) == [1, 2]
	assert two_sum([3, 3], 6) == [0, 1]
		

def test_roman_to_integers():
	''' test roman to integers '''
	assert roman_to_integer('III') == 3
	assert roman_to_integer('CM') == 900
	assert roman_to_integer('I') == 1
	assert roman_to_integer('IV') == 4
	assert roman_to_integer('MCMXCIV') == 1994
	assert roman_to_integer('LVIII') == 58
	
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
