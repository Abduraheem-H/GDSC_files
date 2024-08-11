


class Solution:
    def applyOperations( self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                nums[i-1]*=2
                nums[i]=0
        # print(nums)
        orderd=[]
        counter=0
        for i in range(n):
            if nums[i]!=0:
                orderd.append(nums[i])
            else: 
                counter+=1
        for i in range(n-counter,n):
            orderd.append(0)

        return orderd