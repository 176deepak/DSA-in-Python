'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
'''

#CODE

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for i in range(len(nums)):
            unique = unique^nums[i]
        
        return unique
