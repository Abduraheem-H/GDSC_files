class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hash_sum = {0: 1}  
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

        
            if mod < 0:
                mod += k

            if mod in hash_sum:
                count += hash_sum[mod]
            if mod in hash_sum:
                hash_sum[mod] += 1
            else:
                hash_sum[mod] = 1

        return count

        