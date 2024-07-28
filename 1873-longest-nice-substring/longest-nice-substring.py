class Solution:
    def longestNiceSubstring(self,s: str) -> str:
        # Dynamic sliding window approach
        left = 0
        maxi = ""

        while left < len(s):
            right = len(s)
            while right > left:
                #substr = s[left:right]
                if all(
                    char.lower() in s[left:right] and char.upper() in s[left:right] for char in s[left:right]
                ) and len(s[left:right]) > len(maxi):
                    maxi = s[left:right]
                right -= 1
            left += 1
        return maxi


# print(Solution.longestNiceSubstring("XAyaAx"))  # Output: Aaa
# print("Here")
