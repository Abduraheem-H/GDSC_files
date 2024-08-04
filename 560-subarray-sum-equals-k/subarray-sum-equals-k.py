class Solution:
    
    def subarraySum(self,nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hash_sum = {0: 1}  
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in hash_sum:
                count += hash_sum[prefix_sum - k]
            if prefix_sum in hash_sum:
                hash_sum[prefix_sum] += 1
            else:
                hash_sum[prefix_sum] = 1

        return count



#print(Solution.subarraySum([1, 1, 1], 2))  
