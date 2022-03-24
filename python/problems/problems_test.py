import pytest
from problems_test_imports import *

def test_reverse():
	''' test reverse '''
	assert reverse(123) == 321
	assert reverse(-123) == -321
	assert reverse(120) == 21

def test_longestPalindrome():
	''' test longestPalindrome '''
	assert longestPalindrome("babad") in ["aba", "bab"]
	assert longestPalindrome("cbbd") == "bb"

def test_generate():
	''' test generate '''
	assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
	assert generate(1) == [[1]]

def test_majorityElement():
	''' test majorityElement '''
	assert majorityElement([3, 2, 3]) == 3
	assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

def test_titleToNumber():
	''' test titleToNumber '''
	assert titleToNumber('A') == 1
	assert titleToNumber('AB') == 28
	assert titleToNumber('ZY') == 701
	
def test_isHappy():
	''' test isHappy '''
	assert isHappy(19) == True
	assert isHappy(2) == False

def test_plusOne():
	''' test plusOne '''
	assert plusOne([1,2,3]) == [1, 2, 4]
	assert plusOne([4,3,2,1]) == [4, 3, 2, 2]
	assert plusOne([9]) == [1, 0]

def test_containsDuplicate():
	''' test containsDuplicate '''
	assert containsDuplicate([1,2,3,1]) == True
	assert containsDuplicate([1,2,3,4]) == False
	assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

def test_missingNumber():
	''' test missingNumber '''
	assert missingNumber([3, 0, 1]) == 2
	assert missingNumber([0, 1]) == 2
	assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8

def test_moveZeroes_inefficient():
	''' test moveZeroes_inefficient '''
	assert moveZeroes_inefficient([0,1,0,3,12]) == [1, 3, 12, 0, 0]
	assert moveZeroes_inefficient([0]) == [0]

def test_isPowerOfThree_mod():
	''' test isPowerOfThree_mod '''
	assert isPowerOfThree_mod(27) == True
	assert isPowerOfThree_mod(0) == False
	assert isPowerOfThree_mod(9) == True

def test_isPowerOfThree_inefficient():
	''' test isPowerOfThree_inefficient '''
	assert isPowerOfThree_inefficient(27) == True
	assert isPowerOfThree_inefficient(0) == False
	assert isPowerOfThree_inefficient(9) == True

def test_reverseString():
	''' test reverseString '''
	assert reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
	assert reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]

def test_hammingWeight_inefficient():
	''' test hammingWeight_inefficient '''
	assert hammingWeight_inefficient("00000000000000000000000000001011") == 3
	assert hammingWeight_inefficient("00000000000000000000000010000000") == 1
	assert hammingWeight_inefficient("11111111111111111111111111111101") == 31


def test_isAnagram():
	''' test isAnagram '''
	assert isAnagram("anagram","nagaram") == True
	assert isAnagram("rat","car") == False

def test_singleNumber():
	''' test singleNumber '''
	assert singleNumber([2,2,1]) == 1
	assert singleNumber([4,1,2,1,2]) == 4
	assert singleNumber([1]) == 1

def test_firstUniqChar():
	''' test first uniq char '''
	assert firstUniqChar("leetcode") == 0
	assert firstUniqChar("loveleetcode") == 2
	assert firstUniqChar("aabb") == -1

def test_firstUniqChar_inefficient():
	''' test inefficient first uniq char '''
	assert firstUniqChar_inefficient("leetcode") == 0
	assert firstUniqChar_inefficient("loveleetcode") == 2
	assert firstUniqChar_inefficient("aabb") == -1

def test_removeDuplicates():
	''' test removeDuplicates '''
	a = [1, 1, 2]
	b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	assert a[:removeDuplicates(a)] == [1, 2]
	assert b[:removeDuplicates(b)] == [0, 1, 2, 3, 4]

def test_getIntersectionNode():
	''' test getIntersectionNode '''
	a = [4,1,8,4,5]
	b = [5,6,1,8,4,5]

def test_isPalindrome():
	''' test isPalindrome'''
	assert isPalindrome("A man, a plan, a canal: Panama") == True
	assert isPalindrome("race a car") == False
	assert isPalindrome(" ") == True

def test_climbingStairs():
	''' test climbingStairs '''
	assert climbStairs(2) == 2
	assert climbStairs(3) == 3
	assert climbStairs(4) == 5
	assert climbStairs(5) == 8

def test_asteroidsDestroyed():
	''' test asteroidsDestroyed '''
	assert asteroidsDestroyed(10, [3,9,19,5,21]) == True
	assert asteroidsDestroyed(5, [4,9,23,4]) == False

def test_asteroidCollision():
	''' test asteroid collision '''
	assert asteroidCollision([5,10,-5]) == [5, 10]
	assert asteroidCollision([8,-8]) == []
	assert asteroidCollision([10,2,-5]) == [10]
	assert asteroidCollision([-2,-1,1,2]) == [-2, -1, 1, 2]

def test_mySqrt():
	''' test mySqrt '''
	assert mySqrt(4) == 2
	assert mySqrt(8) == 2
	assert mySqrt(25) == 5
	assert mySqrt(36) == 6
	assert mySqrt(0) == 0
	assert mySqrt(1) == 1
	assert mySqrt(2) == 1
	assert mySqrt(3) == 1

def test_mergeKLists():
	''' test mergeKLists '''
	a = ListNode_mergeKLists(1, ListNode_mergeKLists(4, ListNode_mergeKLists(5)))
	b = ListNode_mergeKLists(1, ListNode_mergeKLists(3, ListNode_mergeKLists(4)))
	c = ListNode_mergeKLists(2, ListNode_mergeKLists(6))
	d = ListNode_mergeKLists(1, ListNode_mergeKLists(1, ListNode_mergeKLists(2, ListNode_mergeKLists(3, ListNode_mergeKLists(4, ListNode_mergeKLists(4, ListNode_mergeKLists(5, ListNode_mergeKLists(6))))))))
	assert mergeKLists([a, b, c]).get_arr() == d.get_arr()

def test_strStr():
	''' test strStr '''
	assert strStr("hello","ll") == 2
	assert strStr("aaaaa", "bba") == -1
	assert strStr("", "") == 0
	assert strStr("a", "a") == 0
	assert strStr("abc", "c") == 2

def test_mergeTwoLists():
	''' test of mergeTwoLists '''
	l1 = ListNode_merge_two_sorted_lists(1, ListNode_merge_two_sorted_lists(2, ListNode_merge_two_sorted_lists(4)))
	l2 = ListNode_merge_two_sorted_lists(1, ListNode_merge_two_sorted_lists(3, ListNode_merge_two_sorted_lists(4)))
	l3 = ListNode_merge_two_sorted_lists(1, ListNode_merge_two_sorted_lists(1, ListNode_merge_two_sorted_lists(2, ListNode_merge_two_sorted_lists(3, ListNode_merge_two_sorted_lists(4, ListNode_merge_two_sorted_lists(4))))))
	assert mergeTwoLists(l1, l2).get_arr() == l3.get_arr()

def test_lengthOfLongestSubstring():
	''' test lengthOfLongestSubstring'''
	assert lengthOfLongestSubstring("abcabcbb") == 3
	assert lengthOfLongestSubstring("bbbbb") == 1
	assert lengthOfLongestSubstring("pwwkew") == 3

def test_longestCommonPrefix():
	''' test longestCommonPrefix'''
	assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
	assert longestCommonPrefix(["dog","racecar","car"]) == ""

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
