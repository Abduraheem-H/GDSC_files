


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum
numarray=NumArray([1,2,3,4])
print(numarray.sumRange(0,2))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
