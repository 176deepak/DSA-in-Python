'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
'''

#CODE

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        start = 0
        end = len(nums)-1
        mid = start+(end-start)//2
        
        while(start <= end):
            if nums[mid] == target:
                first = mid
                end = mid-1
            
            elif target > nums[mid]:
                start = mid+1
            
            elif target < nums[mid]:
                end = mid-1
            
            mid = start + (end - start)//2
        
        start = 0
        end = len(nums)-1
        mid = start+(end-start)//2
        
        while(start <= end):
            if nums[mid] == target:
                last = mid
                start = mid+1
            
            elif target > nums[mid]:
                start = mid+1
            
            elif target < nums[mid]:
                end = mid-1
            
            mid = start + (end - start)//2
        
        
        return first, last
