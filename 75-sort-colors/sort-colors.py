from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
       count_red=nums.count(0)
       count_blue=nums.count(2)
       count_white=nums.count(1)

       nums[0:count_red]=[0]*count_red
       nums[count_red:count_white + count_red]=[1]*count_white
       nums[count_white + count_red:count_blue + count_white+count_red]=[2]*count_blue
      # print(nums)

