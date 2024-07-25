class Solution:
    def minSubArrayLen( self, target:int, nums:List[int]) -> int:
        # target = 7, nums = [2,3,1,2,4,3]
        left = 0
        right = 1
        min_length = float("inf")
        current_sum = nums[left]

        while left <= right and right < len(nums):
            if current_sum >= target:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1
            else:
                current_sum += nums[right]
                right += 1

        while current_sum >= target and left < len(nums):
            min_length = min(min_length, right - left)
            current_sum -= nums[left]
            left += 1
        if min_length != float("inf"):
            return min_length
        else:
            return 0