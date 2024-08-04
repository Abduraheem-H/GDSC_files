class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]

        total_sum = prefix_sum[-1]

        for i in range(len(nums)):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = total_sum - prefix_sum[i]

            if left_sum == right_sum:
                return i

        return -1


#print(Solution().pivotIndex([1,7,3,6,5,6]))  
