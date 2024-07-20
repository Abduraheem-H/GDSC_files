class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      #[0,0,1,1,1,2,2,3,3,4]
      
      count=0
      for i in range(1,len(nums)):
        
        if nums[i]!=nums[i-1]:
            nums[count]=nums[i-1]
            count+=1
        if i==len(nums)-1:
            nums[count]=nums[i]
            count+=1
            
        else: continue
        return count