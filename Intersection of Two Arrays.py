'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''

#CODE

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        intersection = []
                    
        while (i < n and j < m):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i+= 1
                j+= 1
            
            elif nums1[i] < nums2[j]:
                i+= 1
            
            else:
                j+= 1
        
        res = list(set(intersection))
        return res
