import pytest
from fibonacci import *
from steps import *

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
