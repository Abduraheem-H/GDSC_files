class Solution:
    def longestNiceSubstring(self,s: str) -> str:
        def is_valid(substr: str) -> bool:
            # using two pointer to loop over all possible substrings
            unique_char=set(substr)
            for char in unique_char:
                if char.lower() not in unique_char or char.upper() not in unique_char:
                    return False
            return True

        maxi = ""
        n = len(s)

        for left in range(n):
            for right in range(left + 1, n + 1):
                substr = s[left:right]
                if is_valid(substr) and len(substr) > len(maxi):
                    maxi = substr

        return maxi
