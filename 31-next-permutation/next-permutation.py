class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        left = len(nums) - 1

        while left > 0 and nums[left - 1] >= nums[left]:
            left -= 1

        if left > 0:
            mini = float("inf")
            mini_index = left

            for right in range(left, len(nums)):
                if nums[right] > nums[left - 1]:
                    mini = min(mini, nums[right])
                    if mini == nums[right]:
                        mini_index = right
            nums[left - 1], nums[mini_index] = nums[mini_index], nums[left - 1]

        pivot = left
        end = len(nums) - 1

        while pivot < end:
            nums[end], nums[pivot] = nums[pivot], nums[end]
            pivot += 1
            end -= 1

        print(nums)

        """
        Do not return anything, modify nums in-place instead.
        """
