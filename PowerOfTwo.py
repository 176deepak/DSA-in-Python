#Power of Two
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x
'''

#CODE

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        twoPower = [2**i for i in range(0, 32)]
        
        if n in twoPower:
            return True
        else:
            return False
