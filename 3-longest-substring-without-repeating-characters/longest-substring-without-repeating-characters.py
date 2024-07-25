class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Input: s = "abcabcbb"
        left = 0
        right = 0
        maxi = 0

        while right < len(s):
            if len(set(s[left : right + 1])) == (right - left + 1):
               
                maxi = max(maxi, right - left + 1)
                
                right += 1
            else:
               
                left += 1

        return maxi



