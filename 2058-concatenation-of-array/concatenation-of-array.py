class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # [1,2,1]
        array = [0] * (len(nums) * 2)
        
        pointer = 0
        for i in range(len(array)):
            #print(nums[pointer])
            array[i]=nums[pointer]
            pointer += 1
            if i == len(nums) - 1:
                pointer = 0
        return array
#print(Solution.getConcatenation([1,2,3]))