from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmaps = {}
        result = []
        
        for num in nums1:
            if num in hashmaps:
                hashmaps[num] += 1
            else:
                hashmaps[num] = 1
        
        for num in nums2:
            if num in hashmaps and hashmaps[num] > 0:
                result.append(num)
                hashmaps[num] -= 1
        
        return result

