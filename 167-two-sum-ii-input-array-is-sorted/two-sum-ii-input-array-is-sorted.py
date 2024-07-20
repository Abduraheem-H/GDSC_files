class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,7,11,15], target = 9
        leftptr=0
        rightptr=len(numbers)-1
        for i in range(len(numbers)):
            
            if numbers[leftptr]+numbers[rightptr]>target:
                rightptr-=1
            elif numbers[leftptr]+numbers[rightptr]<target:
                leftptr+=1
            
        return[leftptr+1, rightptr+1]
        
        