'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
'''

#CODE

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            Approch 1
        
            unique = 0
        
            for i in range(len(nums)):
                unique = unique^nums[i]
        
            duplicate = unique
        
            for i in range(1, len(nums)):
                duplicate = duplicate^i
            
            return duplicate    
        '''
    
        # Approch 2
    
        dupli_count = {}
    
        for i in nums:
            if i in dupli_count:
                dupli_count[i]+= 1
            else:
                dupli_count[i] = 1
    
        for i in dupli_count:
            if dupli_count[i] > 1:
                return i
    
