class Solution:
    def minStartValue( self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        minimum_value = float("inf")
        for i in range(len(prefix_sum)):
            minimum_value = min(prefix_sum[i], minimum_value)
            
        start_value = 1 - minimum_value 
        return start_value if start_value > 0 else 1
#print(Solution.minStartValue([-3,2,-3,4,2]))
