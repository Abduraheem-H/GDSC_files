class Solution:
    def findMaxAverage(self,nums: List[int], k: int) -> float:
        max_average = float('-inf')
        current_sum = sum(nums[:k])
        max_average = current_sum / k
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            current_average = current_sum / k
            max_average = max(max_average, current_average)
            #print(max_average)
        
        return max_average
