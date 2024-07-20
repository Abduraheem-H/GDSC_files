class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #[0,1,2,2,3,0,4,2]
        left=0
        for right in range(len(nums)):
            if val!=nums[right]:
                nums[left]=nums[right]
                left+=1
        return left

        