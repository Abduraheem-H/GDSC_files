

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and nums[j] < nums[i]:
                    count[i] += 1
        return count
