class Solution:
    def applyOperations( self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                nums[i-1]*=2
                nums[i]=0
        # print(nums)
        orderd=[num for num in nums if num!=0]
        orderd.extend([0]*(n-len(orderd)))

        return orderd